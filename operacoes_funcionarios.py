from conexao import conectar


def listar_funcionarios():
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM funcionarios ORDER BY id")
        resultado = cursor.fetchall()
        return resultado

    except Exception as e:
        print("\nErro ao listar funcionários!")

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
        print("\nFuncionário cadastrado com sucesso!")

    except Exception as e:
        print("\nErro ao cadastrar funcionário!")

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
        print("\nSalário alterado com sucesso!")

    except Exception as e:
        print("\nErro ao atualizar salário!")

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
        print("\nFuncionário deletado com sucesso!")


    except Exception as e:
        print("\nErro ao deletar funcionário!")

    finally:
        if conn:
            conn.close()