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

def atualizar_salario(id_funcionario, novo_salario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE funcionarios SET salario = %s WHERE id = %s",
        (novo_salario, id_funcionario)

    )

    conn.commit()
    print("\nSalário alterado com sucesso!")

def deletar_funcionario(id_funcionario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM funcionarios WHERE id = %s ",
        (id_funcionario,)

    )

    conn.commit()
    print("\nFuncionário deletado com sucesso!")