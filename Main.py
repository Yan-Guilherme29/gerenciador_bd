from operacoes import *

# cadastrar_funcionario("Sarah", "Designer", 5000, "TI", "sarah@gmail.com")

# atualizar_salario(1, 12000)

# deletar_funcionario(7)


for funcionario in listar_funcionarios():

    print(f"\n ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]} | Salário: {funcionario[3]} | Departamento: {funcionario[4]} | Email: {funcionario[5]}  ")

