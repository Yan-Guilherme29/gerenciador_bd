from operacoes import listar_funcionarios

for funcionario in listar_funcionarios():

    print(f"\n ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]} | Salário: {funcionario[3]} | Departamento: {funcionario[4]} | Email: {funcionario[5]}  ")
