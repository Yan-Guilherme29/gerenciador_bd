from conexao import conectar

def listar_tarefas():
    conn = None

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tarefas")
        resultado = cursor.fetchall()
        return resultado

    except Exception as e:
        print("Erro ao listar tarefas!")

    finally:
        if conn:
            conn.close()

def cadastrar_tarefa(descricao, projeto_id):
    conn = None

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tarefas (descricao, projeto_id) VALUES (%s, %s)",
            (descricao, projeto_id)
        )

        conn.commit()
        print("Tarefa cadastrada com sucesso!")

    except Exception as e:
        print("Erro ao cadastrar tarefa!")

    finally:
        if conn:
            conn.close()

def deletar_tarefa(id_tarefa):
    conn = None

    try:
        conn = conectar()
        cursor = conn.cursor()


        cursor.execute(
            "DELETE FROM tarefas WHERE id = %s ",
            (id_tarefa, )
        )

        conn.commit()
        print("Tarefa deletada com sucesso!")

    except Exception as e:
        print("Erro ao deletar tarefa!")

    finally:
        if conn:
            conn.close()