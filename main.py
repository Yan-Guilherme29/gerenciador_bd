from operacoes_funcionarios import *
from operacoes_projetos import *
from operacoes_tarefas import *

while True:

    print("=-" * 15)
    print("\nGerenciador de Banco de dados\n")
    print("=-" * 15)
    print("1 - Listar funcionários ")
    print("2 - Listar projetos")
    print("3 - Listar tarefas")
    print("=-" * 15)
    print("4 - Cadastrar funcionário")
    print("5 - Cadastrar projeto")
    print("6 - Cadastrar tarefa")
    print("=-" * 15)
    print("7 - Atualizar funcionário")
    print("8 - Atualizar projeto")
    print("9 - Atualizar descrição da tarefa")
    print("10 - Atualizar status da tarefa")
    print("=-" * 15)
    print("11 - Deletar funcionário ")
    print("12 - Deletar projeto")
    print("13 - Deletar tarefa")
    print("=-" * 15)
    print("0 - Sair")
    print("=-" * 15)


    escolha = int(input("\nDigite sua escolha: "))

    match escolha:

        case 0:
            print("\nSistema finalizado! Até a próxima!")
            break

        case 1:
            for funcionario in listar_funcionarios():
                print("=-" *15 )
                print("\n Tabela de Funcionários: \n")
                print(
                    f"\n ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]} | Salário: {funcionario[3]} | Departamento: {funcionario[4]} | Email: {funcionario[5]}"
                )

        case 2:
            for projeto in listar_projetos():
                print("\n Tabela de Projetos: \n")
                print(
                    f"\n ID: {projeto[0]} | Título: {projeto[1]} | Funcionário ID: {projeto[2]} "
                )

        case 3:
            for tarefa in listar_tarefas():
                print("\n Tabela de Tarefas: \n")
                print(
                    f"\n ID: {tarefa[0]} | Descrição: {tarefa[1]} | Concluída: {tarefa[2]} | Projeto ID: {tarefa[3]}  "
                )

        case 4:

            print("\n Cadastrar Funcionário: \n")

            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            departamento = input("Departamento: ")
            email = input("Email: ")

            cadastrar_funcionario(nome, cargo, salario, departamento, email)

        case 5:

            print("\n Cadastrar Projeto: \n")

            titulo = input("Título: ")
            funcionario_id = int(input("Id Funcionário: "))

            cadastrar_projetos(titulo, funcionario_id)

        case 6:

            print("\n Cadastrar Tarefa: \n")

            descricao = input("Descrição: ")
            projeto_id = int(input("Id projeto: "))

            cadastrar_tarefa(descricao, projeto_id)
