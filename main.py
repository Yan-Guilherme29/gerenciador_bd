from operacoes_funcionarios import *
from operacoes_projetos import *
from operacoes_tarefas import *

while True:

    print("\n   Gerenciador de Banco de dados   ")
    print("=-" * 18)
    print("1 - Listar funcionários ")
    print("2 - Listar projetos")
    print("3 - Listar tarefas")
    print("=-" * 18)
    print("4 - Cadastrar funcionário")
    print("5 - Cadastrar projeto")
    print("6 - Cadastrar tarefa")
    print("=-" * 18)
    print("7 - Atualizar salário")
    print("8 - Atualizar projeto")
    print("9 - Atualizar descrição da tarefa")
    print("10 - Atualizar status da tarefa")
    print("=-" * 18)
    print("11 - Deletar funcionário ")
    print("12 - Deletar projeto")
    print("13 - Deletar tarefa")
    print("=-" * 18)
    print("0 - Sair")
    print("=-" * 18)


    escolha = int(input("\nDigite sua escolha: "))

    match escolha:

        case 0:
            print("\nSistema finalizado! Até a próxima!")
            break

        case 1:
            print("\n Tabela de Funcionários:")
            print("=-" * 50)

            for funcionario in listar_funcionarios():
                print(
                    f"ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]} | Salário: {funcionario[3]} | Departamento: {funcionario[4]} | Email: {funcionario[5]}"
                )
            print("=-" * 50)

        case 2:
            print("\n Tabela de Projetos:")
            print("=-" * 50)

            for projeto in listar_projetos():
                print(
                    f"ID: {projeto[0]} | Título: {projeto[1]} | Funcionário ID: {projeto[2]} "
                )
            print("=-" * 50)

        case 3:
            print("\n Tabela de Tarefas:")
            print("=-" * 55)

            for tarefa in listar_tarefas():
                print(
                    f"ID: {tarefa[0]} | Descrição: {tarefa[1]} | Concluída: {tarefa[2]} | Projeto ID: {tarefa[3]}  "
                )
            print("=-" * 55)

        case 4:

            print("\n Cadastrar Funcionário:")
            print("=-" * 50)

            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            departamento = input("Departamento: ")
            email = input("Email: ")

            cadastrar_funcionario(nome, cargo, salario, departamento, email)
            print("=-" * 50)

        case 5:

            print("\n Cadastrar Projeto:")
            print("=-" * 50)

            titulo = input("Título: ")
            funcionario_id = int(input("Id do Funcionário: "))

            cadastrar_projetos(titulo, funcionario_id)
            print("=-" * 50)

        case 6:

            print("\n Cadastrar Tarefa:")
            print("=-" * 50)

            descricao = input("Descrição: ")
            projeto_id = int(input("Id do projeto: "))

            cadastrar_tarefa(descricao, projeto_id)
            print("=-" * 50)

        case 7:

            print("\n Atualizar Salário:")
            print("=-" * 50)

            id_funcionario = int(input("Id do funcionário: "))
            novo_salario = float(input("Novo salário: "))

            atualizar_salario(id_funcionario, novo_salario)
            print("=-" * 50)

        case 8:

            print("\n Atualizar Projeto:")
            print("=-" * 50)

            id_projeto = int(input("Id do projeto: "))
            novo_titulo = input("Novo título: ")

            atualizar_projeto(id_projeto, novo_titulo)
            print("=-" * 50)

        case 9:

            print("\n Atualizar descrição da tarefa:")
            print("=-" * 50)

            id_tarefa = int(input("Id da tarefa: "))
            nova_descricao = input("Nova descrição: ")


            atualizar_descricao_tarefa(id_tarefa, nova_descricao)
            print("=-" * 50)

        case 10:
            print("\n Atualizar status da tarefa:")
            print("=-" * 50)

            id_tarefa = int(input("Id da tarefa: "))
            opcao = int(input("Concluída? (Sim = 1 | Não = 0): "))

            if opcao in (0, 1):
                concluida = opcao == 1

                atualizar_status_tarefa(id_tarefa, concluida)

            else:
                print("Digite apenas 1 para Sim ou 0 para Não!")

            print("=-" * 50)

        case 11:

            print("\n Deletar funcionário:")
            print("=-" * 50)

            id_funcionario = int(input("Id do funcionário: "))

            opcao = int(input("Tem certeza que deseja deletar esse funcionário? (Sim = 1 | Não = 0): "))

            if opcao == 1:
                deletar_funcionario(id_funcionario)

            elif opcao == 0:
                print("\n Exclusão cancelada!")

            else:
                print("\n Digite apenas 1 para Sim ou 0 para Não!")

            print("=-" * 50)

        case 12:

            print("\n Deletar projeto:")
            print("=-" * 50)

            id_projeto = int(input("Id do projeto: "))

            opcao = int(input("Tem certeza que deseja deletar esse projeto? (Sim = 1 | Não = 0): "))

            if opcao == 1:
                deletar_projeto(id_projeto)

            elif opcao == 0:
                print("\n Exclusão cancelada!")

            else:
                print("\n Digite apenas 1 para Sim ou 0 para Não!")

            print("=-" * 50)

        case 13:

            print("\n Deletar tarefa:")
            print("=-" * 50)

            id_tarefa = int(input("Id da tarefa: "))

            opcao = int(input("Tem certeza que deseja deletar essa tarefa? (Sim = 1 | Não = 0): "))

            if opcao == 1:
                deletar_tarefa(id_tarefa)

            elif opcao == 0:
                print("\n Exclusão cancelada!")

            else:
                print("\n Digite apenas 1 para Sim ou 0 para Não!")

            print("=-" * 50)