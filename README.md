# gerenciador_bd

Projeto Python para conexão e manipulação de um banco de dados PostgreSQL via `psycopg2`, sem ORM — SQL puro.

Desenvolvido como projeto prático de estudos de backend.

---

## Tecnologias

- Python 3
- PostgreSQL
- psycopg2
- python-dotenv

---

## Como configurar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador_bd.git
   cd gerenciador_bd
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install psycopg2 python-dotenv
   ```

4. Configure as variáveis de ambiente:
   ```bash
   cp .env.example .env
   ```
   Edite o `.env` com suas credenciais do PostgreSQL.

5. Execute o projeto:
   ```bash
   python main.py
   ```

---

## Estrutura

```
gerenciador_bd/
├── conexao.py       # Função de conexão com o banco
├── operacoes.py     # Funções de SELECT, INSERT, UPDATE, DELETE
├── main.py          # Ponto de entrada da aplicação
├── .env.example     # Exemplo de variáveis de ambiente
└── README.md
```

---

## Autor

**Yan Guilherme**

[![GitHub](https://img.shields.io/badge/GitHub-Yan--Guilherme29-181717?style=flat&logo=github)](https://github.com/Yan-Guilherme29)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-yan--guilherme--dev--backend-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/yan-guilherme-dev-backend)