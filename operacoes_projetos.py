from conexao import conectar

def listar_projetos():
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM projetos")
        resultado = cursor.fetchall()
        return resultado

    except Exception as e:
        print("Erro ao listar projetos")

    finally:
        if conn:
            conn.close()


def cadastrar_projetos(titulo, funcionario_id):
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute (
            "INSERT INTO projetos (titulo, funcionario_id) VALUES (%s, %s)",
            (titulo, funcionario_id)
        )

        conn.commit()
        print("Projeto cadastrado com sucesso!")

    except Exception as e:
        print("Erro ao cadastrar projeto!")

    finally:
        if conn:
            conn.close()

def atualizar_projeto(id_projeto, novo_titulo):
    conn = None

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE projetos SET titulo = %s WHERE id = %s",
            (novo_titulo, id_projeto)
        )

        conn.commit()
        print("Projeto alterado com sucesso!")

    except Exception as e:
        print("Erro ao atualizar projeto!")

    finally:
        if conn:
            conn.close()

def deletar_projeto(id_projeto):
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM projetos WHERE id = %s ",
            (id_projeto,)

        )

        conn.commit()
        print("Projeto deletado com sucesso!")


    except Exception as e:
        print("Erro ao deletar projeto!")

    finally:
        if conn:
            conn.close()