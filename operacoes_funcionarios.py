from conexao import conectar


def listar_funcionarios():
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM funcionarios")
        resultado = cursor.fetchall()
        return resultado

    except Exception as e:
        print("Erro ao listar funcionários!")

    finally:
        if conn:
            conn.close()


def cadastrar_funcionario(nome, cargo, salario, departamento, email):
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO funcionarios (nome , cargo, salario, departamento, email) VALUES (%s, %s, %s, %s, %s)",
            (nome, cargo, salario, departamento, email)
        )

        conn.commit()
        print("Funcionário cadastrado com sucesso!")

    except Exception as e:
        print("Erro ao cadastrar funcionário!")

    finally:
        if conn:
            conn.close()


def atualizar_salario(id_funcionario, novo_salario):
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE funcionarios SET salario = %s WHERE id = %s",
            (novo_salario, id_funcionario)

        )

        conn.commit()
        print("Salário alterado com sucesso!")

    except Exception as e:
        print("Erro ao atualizar salário!")

    finally:
        if conn:
            conn.close()


def deletar_funcionario(id_funcionario):
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM funcionarios WHERE id = %s ",
            (id_funcionario,)

        )

        conn.commit()
        print("Funcionário deletado com sucesso!")


    except Exception as e:
        print("Erro ao deletar funcionário!")

    finally:
        if conn:
            conn.close()