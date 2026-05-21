<div align="center">

# Cursos e Manutenções Residenciais

Plataforma de cursos online para ensinar manutenção domiciliar com videoaulas interativas, certificação profissional e simulador de precificação.

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-local-lightblue?style=flat-square&logo=sqlite)](https://sqlite.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat-square&logo=bootstrap)](https://getbootstrap.com)

</div>

---

## Equipe — Grupo Matemáticos

| Nome | RA |
|---|---|
| Pedro Augusto Brito Castilho Pereira | 100954 |
| Gustavo Mattos da Silva | 99242 |
| João Pedro de Jesus Narcizo | 100006 |
| Ronald Viana Araújo | 102648 |

---

## Sobre o Projeto

**Tema:** Plataforma de Cursos Online

O projeto capacita pessoas a realizarem manutenções residenciais — seja na própria casa ou atuando como prestador de serviços — combatendo a escassez de mão de obra qualificada.

### Funcionalidades

- Videoaulas interativas com questão obrigatória para avançar
- Dois perfis de aluno: "Própria casa" e "Prestador de serviços"
- Lista de materiais com links de compra por curso
- Simulador de precificação para serviços
- Certificado digital gerado ao concluir 100% do curso
- Modo offline via PWA *(em desenvolvimento)*

**Cursos disponíveis:** Pintura Básica · Elétrica Básica · Hidráulica · Carpintaria · Instalação de Móveis

---

## Como Rodar

**Pré-requisito:** Python 3.x instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/gmattosoft/matematicos.git
cd matematicos

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute o servidor
python app.py
```

Acesse em: **http://127.0.0.1:5000**

> O banco de dados SQLite é criado automaticamente na primeira execução.

---

## Estrutura do Projeto

```
cursos_residenciais/
├── app.py                  ← Servidor Flask (rotas, modelos, lógica)
├── requirements.txt        ← Dependências Python
├── cursos_residenciais.db  ← Banco SQLite (gerado automaticamente)
└── templates/
    ├── base.html           ← Layout base compartilhado
    ├── home.html           ← Página inicial
    ├── cadastro.html       ← Cadastro de aluno
    ├── login.html          ← Login
    ├── dashboard.html      ← Painel de cursos
    ├── video_aula.html     ← Player de vídeo + questão
    ├── simulador.html      ← Simulador de precificação
    └── certificado.html    ← Certificado de conclusão
```

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python + Flask |
| Banco de dados | SQLite |
| Frontend | Jinja2 Templates + Bootstrap 5 |
| Vídeos | YouTube embed |

---

<div align="center">
  <sub>Projeto acadêmico — Grupo Matemáticos · FECAF</sub>
</div>
