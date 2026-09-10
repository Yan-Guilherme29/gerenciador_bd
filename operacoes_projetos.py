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
