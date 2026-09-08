from conexao import conectar



def listar_funcionarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    resultado = cursor.fetchall()
    return resultado
