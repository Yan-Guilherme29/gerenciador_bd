CREATE TABLE IF NOT EXISTS funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cargo VARCHAR(50),
    salario NUMERIC(10,2),
    departamento VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS projetos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    funcionario_id INT REFERENCES funcionarios(id)
);

CREATE TABLE IF NOT EXISTS tarefas (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    concluida BOOLEAN NOT NULL DEFAULT false,
    projeto_id INT REFERENCES projetos(id)
);

INSERT INTO funcionarios (nome, cargo, salario, departamento, email)
VALUES
    ('Yan', 'Gerente', 4000, 'TI', 'yan@empresa.com'),
    ('Diego', 'Gerente', 5000, 'Vendas', 'diego@empresa.com'),
    ('Lucas', 'Analista', 3000, 'TI', 'lucas@empresa.com'),
    ('Aline', 'Assistente', 2000, 'TI', 'aline@empresa.com');

INSERT INTO projetos (titulo, funcionario_id)
VALUES
    ('Dashboard Financeiro', 1),
    ('Sistema de vendas online', 2),
    ('API de pagamentos', 1);

-- concluida não é informada: o DEFAULT false entra sozinho
INSERT INTO tarefas (descricao, projeto_id)
VALUES
    ('Modelar o banco de dados', 1),
    ('Criar os gráficos de receita', 1),
    ('Montar o catálogo de produtos', 2),
    ('Criar o endpoint de pagamento', 3);

-- aqui concluida é informada como true
INSERT INTO tarefas (descricao, projeto_id, concluida)
VALUES
    ('Levantar requisitos do dashboard', 1, true),
    ('Definir o layout da loja', 2, true);