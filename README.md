# Gerenciador BD

Sistema de linha de comando para gerenciar **funcionários, projetos e tarefas**, feito em **Python puro** com **PostgreSQL**, sem ORM. O projeto pratica o ciclo completo de um CRUD (criar, listar, atualizar e deletar) com um banco relacional de verdade, chaves estrangeiras e tratamento de erros.

> Projeto de estudos de backend e base do curso **"Python + PostgreSQL: Seu Primeiro Projeto de Portfólio"**.

---

## Funcionalidades

- CRUD completo para as três tabelas: funcionários, projetos e tarefas
- Menu interativo no terminal, com 13 opções
- Listagens ordenadas por `id`
- Aviso claro quando o `id` informado não existe (em atualizações e exclusões)
- Confirmação antes de deletar (Sim = 1 | Não = 0), repetida até a resposta ser válida
- Leitura segura de números: entradas como `abc` não derrubam o programa
- Consultas parametrizadas (`%s`), que protegem contra SQL injection
- Credenciais do banco fora do código, em variáveis de ambiente (`.env`)
- Script `setup.sql` que cria as tabelas e insere dados de exemplo

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.12 | Linguagem do projeto (versão em que foi testado) |
| PostgreSQL | Banco de dados relacional |
| psycopg2 | Conexão entre Python e PostgreSQL |
| python-dotenv | Leitura das credenciais a partir do `.env` |

## Estrutura do projeto

```
gerenciador_bd/
├── main.py                  # Menu interativo e funções de leitura segura
├── database/
│   ├── __init__.py
│   ├── conexao.py           # Função que abre a conexão com o banco
│   └── setup.sql            # Criação das tabelas + dados de exemplo
├── operacoes/
│   ├── __init__.py
│   ├── operacoes_funcionarios.py
│   ├── operacoes_projetos.py
│   └── operacoes_tarefas.py
├── .env.example             # Modelo das variáveis de ambiente
├── .gitignore
├── requirements.txt
└── README.md
```

## Modelo de dados

```
funcionarios (1) ──── (N) projetos (1) ──── (N) tarefas
```

| Tabela | Colunas |
|---|---|
| `funcionarios` | `id`, `nome`, `cargo`, `salario`, `departamento`, `email` |
| `projetos` | `id`, `titulo`, `funcionario_id` (referencia `funcionarios`) |
| `tarefas` | `id`, `descricao`, `concluida` (padrão `false`), `projeto_id` (referencia `projetos`) |

As chaves estrangeiras protegem a integridade dos dados: não é possível cadastrar um projeto para um funcionário inexistente, nem deletar um funcionário que ainda tenha projetos (ou um projeto que ainda tenha tarefas). Nesses casos o banco recusa a operação e o programa mostra o erro.

---

## Como rodar

### Pré-requisitos

- [Python 3.12](https://www.python.org/downloads/) instalado
- [PostgreSQL](https://www.postgresql.org/download/) instalado e em execução
- [Git](https://git-scm.com/downloads)
- Um editor de código (VS Code ou PyCharm)

### 1. Clonar o repositório

```bash
git clone https://github.com/Yan-Guilherme29/gerenciador_bd.git
cd gerenciador_bd
```

### 2. Criar e ativar o ambiente virtual

Crie o ambiente (igual em todos os sistemas):

```bash
python -m venv .venv
```

Ative conforme o seu terminal:

| Terminal | Comando |
|---|---|
| PowerShell / CMD (Windows) | `.venv\Scripts\activate` |
| Git Bash (Windows) | `source .venv/Scripts/activate` |
| Linux / macOS | `source .venv/bin/activate` |

Quando estiver ativo, o prompt começa com `(.venv)`.

> **Atenção:** no Git Bash, a barra invertida (`\`) não funciona e o comando falha com `command not found`. Use o `source` com barras normais.

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados

Crie um banco vazio no PostgreSQL, pelo pgAdmin ou pelo terminal:

```sql
CREATE DATABASE estudos_sql;
```

### 5. Criar as tabelas e os dados de exemplo

Com o banco criado, execute o script. Pelo terminal:

```bash
psql -U seu_usuario -d estudos_sql -f database/setup.sql
```

Ou abra o arquivo `database/setup.sql` no pgAdmin, conectado ao banco `estudos_sql`, e execute.

> Rode o script **uma vez**, em um banco novo e vazio. Executá-lo de novo duplica os dados de exemplo.

### 6. Configurar as variáveis de ambiente

Copie o modelo e preencha com os dados do **seu** PostgreSQL:

```bash
cp .env.example .env
```

(No PowerShell: `copy .env.example .env`.)

Conteúdo do `.env`:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=estudos_sql
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

O `.env` não vai para o Git (está no `.gitignore`), então suas credenciais ficam só na sua máquina.

### 7. Executar

Sempre a partir da **pasta raiz** do projeto:

```bash
python main.py
```

---

## Menu

```
1 - Listar funcionários          7 - Atualizar salário
2 - Listar projetos              8 - Atualizar projeto
3 - Listar tarefas               9 - Atualizar descrição da tarefa
4 - Cadastrar funcionário       10 - Atualizar status da tarefa
5 - Cadastrar projeto           11 - Deletar funcionário
6 - Cadastrar tarefa            12 - Deletar projeto
                                13 - Deletar tarefa
0 - Sair
```

Dicas de uso:

- O salário usa **ponto** como separador decimal (ex.: `3500.50`).
- Nas confirmações, digite `1` para Sim e `0` para Não.
- Os dados de exemplo são fictícios: 4 funcionários, 3 projetos e 6 tarefas.

---

## Problemas comuns

**O terminal diz `command not found` ao ativar o venv (Git Bash)**
Use `source .venv/Scripts/activate`, com barras normais.

**O PyCharm avisa "Package requirements ... are not satisfied"**
O interpretador do projeto não é o `.venv`. Vá em *Settings → Project → Python Interpreter* e aponte para `.venv\Scripts\python.exe` da pasta do projeto.

**`Fatal error in launcher: Unable to create process...`**
A pasta do projeto foi movida depois de criar o `.venv`, e o ambiente guarda o caminho antigo. Apague a pasta `.venv` e crie de novo (passo 2). Ela não vai para o Git, então nada se perde.

**`error: Microsoft Visual C++ 14.0 or greater is required` ao instalar o psycopg2**
Sua versão do Python é nova demais para existir um pacote já compilado do `psycopg2` na versão fixada. Use o Python 3.12 (versão testada) ou instale o *Microsoft C++ Build Tools* que a própria mensagem indica.

**`ModuleNotFoundError` ao rodar o programa**
Execute `python main.py` a partir da pasta raiz do projeto, não de dentro de `database/` ou `operacoes/`.

**Erro de conexão ou variáveis vazias**
Confirme que o `.env` existe na raiz, que o PostgreSQL está rodando e que usuário, senha e nome do banco estão corretos.

---

## O que este projeto pratica

- Conexão com PostgreSQL usando `psycopg2`
- Consultas parametrizadas e prevenção de SQL injection
- `try / except / finally` e fechamento correto da conexão
- Chaves estrangeiras e ordem de deleção
- `cursor.rowcount` para detectar operações que não afetaram nenhuma linha
- Validação de entrada do usuário com funções auxiliares reaproveitáveis
- Ambientes virtuais, `requirements.txt` e variáveis de ambiente
- Organização do código em pacotes Python
- Commits semânticos (`feat`, `fix`, `refactor`, `config`)

## Próximos passos

- [ ] Relatórios com `JOIN` entre as tabelas
- [ ] Interface de terminal mais completa com `rich`
- [ ] Testes automatizados com `pytest`
- [ ] Migração para uma API com **FastAPI**
- [ ] Deploy

---

## Autor

**Yan Guilherme**, estudante de Engenharia de Software.

- GitHub: [@Yan-Guilherme29](https://github.com/Yan-Guilherme29)