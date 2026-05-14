Nome do grupo: Matemáticos

Integrantes:

-Pedro Augusto Brito Castilho Pereira (100954)

-Gustavo Mattos da Silva (99242)

-João Pedro de Jesus Narcizo (100006)

-Ronald Viana Araújo (102648)


Nome do projeto: Cursos e Manutenções Residenciais


Tema escolhido: Plataforma de Cursos Online


Descrição inicial: Plataforma de cursos online para ensinar manutenção domiciliar com videoaulas interativas, questões obrigatórias e certificação profissional. Oferece lista de materiais com links de afiliados, simulador de precificação para serviços e modo offline via PWA. O projeto capacita alunos a fazerem manutenção em suas próprias casas ou atuarem como prestadores de serviço, combatendo a escassez de mão de obra qualificada.

# Cursos e Manutenções Residenciais

## Como rodar

### 1. Instale as dependências
```bash
pip install -r requirements.txt
```

### 2. Execute o servidor
```bash
python app.py
```

### 3. Acesse no navegador
```
http://127.0.0.1:5000
```

---

## Estrutura do projeto

```
cursos_residenciais/
├── app.py                  ← Servidor Flask (rotas, modelos, lógica)
├── requirements.txt        ← Dependências
├── cursos_residenciais.db  ← Banco SQLite (criado automaticamente)
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

## Funcionalidades

- Cadastro e login de alunos
- Dois tipos de perfil: "Própria casa" e "Prestador"
- Cursos disponíveis: Pintura Básica e Elétrica Básica
- Videoaulas com questão obrigatória para avançar
- Simulador de precificação de serviços
- Certificado gerado ao atingir 100% de progresso
