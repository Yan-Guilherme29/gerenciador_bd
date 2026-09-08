from conexao import conectar



def listar_funcionarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    resultado = cursor.fetchall()
    return resultado

def cadastrar_funcionario(nome, cargo, salario, departamento, email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO funcionarios (nome , cargo, salario, departamento, email) VALUES (%s, %s, %s, %s, %s)",
        (nome, cargo, salario, departamento, email)
    )

    conn.commit()
    print("Dado inserido com sucesso!")

