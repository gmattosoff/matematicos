# -*- coding: utf-8 -*-
"""Sistema - Cursos e Manutenções Residenciais"""

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
import os
import random

app = Flask(__name__)
app.secret_key = "chave_secreta_para_teste_qa_2025"

# Banco de dados SQLite (arquivo gerado na pasta do projeto)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'cursos_residenciais.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ============================================================
# MODELOS
# ============================================================

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    tipo_aluno = db.Column(db.String(50), nullable=False)
    cursos_concluidos = db.Column(db.String(500), default="")
    progresso = db.Column(db.Integer, default=0)


class VideoAula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    curso = db.Column(db.String(100), nullable=False)
    url_video = db.Column(db.String(500), nullable=False)
    questao = db.Column(db.String(500), nullable=False)
    resposta_correta = db.Column(db.String(200), nullable=False)
    ordem = db.Column(db.Integer, default=0)


# ============================================================
# INICIALIZAÇÃO DO BANCO
# ============================================================

def init_db():
    db.create_all()
    if VideoAula.query.count() == 0:
        aulas = [
            VideoAula(titulo="Introdução à Pintura Residencial", curso="Pintura Básica",
                      url_video="https://www.youtube.com/embed/dQw4w9WgXcQ",
                      questao="Qual o primeiro passo antes de pintar uma parede?",
                      resposta_correta="Limpar e lixar a parede", ordem=1),
            VideoAula(titulo="Preparação da Parede", curso="Pintura Básica",
                      url_video="https://www.youtube.com/embed/dQw4w9WgXcQ",
                      questao="Qual material é usado para corrigir imperfeições na parede?",
                      resposta_correta="Massa corrida", ordem=2),
            VideoAula(titulo="Introdução à Elétrica Residencial", curso="Elétrica Básica",
                      url_video="https://www.youtube.com/embed/dQw4w9WgXcQ",
                      questao="O que deve ser desligado antes de qualquer reparo elétrico?",
                      resposta_correta="Disjuntor geral", ordem=1),
        ]
        for aula in aulas:
            db.session.add(aula)
        db.session.commit()
        print("✅ Dados de exemplo inseridos!")


# ============================================================
# ROTAS
# ============================================================

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    erro = None
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        senha_raw = request.form.get('senha', '')
        tipo = request.form.get('tipo', '')

        if not nome:
            erro = "O campo nome é obrigatório."
        elif '@' not in email:
            erro = "E-mail inválido."
        elif not tipo:
            erro = "Selecione o tipo de aluno."
        elif Aluno.query.filter_by(email=email).first():
            erro = "E-mail já cadastrado."
        else:
            senha = hashlib.sha256(senha_raw.encode()).hexdigest()
            db.session.add(Aluno(nome=nome, email=email, senha=senha, tipo_aluno=tipo))
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('cadastro.html', erro=erro)


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = hashlib.sha256(request.form.get('senha', '').encode()).hexdigest()
        aluno = Aluno.query.filter_by(email=email, senha=senha).first()
        if aluno:
            session['usuario_id'] = aluno.id
            session['usuario_nome'] = aluno.nome
            session['usuario_email'] = aluno.email
            session['usuario_tipo'] = aluno.tipo_aluno
            return redirect(url_for('dashboard'))
        erro = "E-mail ou senha inválidos."
    return render_template('login.html', erro=erro)


@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    aluno = db.session.get(Aluno, session['usuario_id'])
    return render_template('dashboard.html', progresso=aluno.progresso)


@app.route('/video_aula/<curso>', methods=['GET', 'POST'])
def video_aula(curso):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    aula = VideoAula.query.filter_by(curso=curso, ordem=1).first()
    if not aula:
        return redirect(url_for('dashboard'))

    total_aulas = VideoAula.query.filter_by(curso=curso).count()
    erro = None

    if request.method == 'POST':
        resposta = request.form.get('resposta', '').strip()
        if resposta.lower() == aula.resposta_correta.lower():
            aluno = db.session.get(Aluno, session['usuario_id'])
            aluno.progresso = min(aluno.progresso + 20, 100)
            db.session.commit()
            return redirect(url_for('dashboard'))
        erro = "Resposta incorreta! Tente novamente."

    return render_template('video_aula.html', curso=curso, aula=aula,
                           total_aulas=total_aulas, erro=erro)


@app.route('/simulador', methods=['GET', 'POST'])
def simulador():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    resultado = None
    erro = None

    if request.method == 'POST':
        try:
            horas = float(request.form.get('horas', 0))
            materiais = float(request.form.get('materiais', 0))
            deslocamento = float(request.form.get('deslocamento', 0))

            if horas < 0:
                erro = "As horas trabalhadas devem ser maiores que zero."
            elif materiais < 0:
                erro = "O custo de materiais não pode ser negativo."
            elif deslocamento < 0:
                erro = "O deslocamento não pode ser negativo."
            else:
                total = (horas * 50.0) + materiais + deslocamento
                resultado = f"{total:.2f}"
        except ValueError:
            erro = "Insira valores numéricos válidos."

    return render_template('simulador.html', resultado=resultado, erro=erro)


@app.route('/certificado')
def certificado():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    aluno = db.session.get(Aluno, session['usuario_id'])
    if aluno.progresso < 100:
        return redirect(url_for('dashboard'))
    codigo = f"CR-{aluno.id}-{random.randint(1000, 9999)}"
    return render_template('certificado.html', nome=aluno.nome, codigo=codigo)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == '__main__':
    with app.app_context():
        init_db()
    print("\n" + "=" * 50)
    print("🚀 Sistema Cursos e Manutenções Residenciais")
    print("=" * 50)
    print("🔗 Acesse: http://127.0.0.1:5000")
    app.run(debug=True)
