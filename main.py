from operacoes.operacoes_funcionarios import *
from operacoes.operacoes_projetos import *
from operacoes.operacoes_tarefas import *


def ler_numero(mensagem, tipo):
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            if tipo == int:
                print("\nValor incorreto! Digite apenas números inteiros!")
            elif tipo == float:
                print("\nValor incorreto! Digite um número, usando ponto nos decimais (ex: 3500.50)!")


def ler_confirmacao(mensagem):
    while True:
        opcao = ler_numero(mensagem, int)

        if opcao in (0, 1):
            return opcao

        print("\nDigite apenas 1 para Sim ou 0 para Não!")


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

    escolha = ler_numero('\nDigite sua escolha: ', int)

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
            salario = ler_numero("Salário: ", float)
            departamento = input("Departamento: ")
            email = input("Email: ")

            cadastrar_funcionario(nome, cargo, salario, departamento, email)
            print("=-" * 50)

        case 5:

            print("\n Cadastrar Projeto:")
            print("=-" * 50)

            titulo = input("Título: ")
            funcionario_id = ler_numero('\nId do funcionário: ', int)

            cadastrar_projetos(titulo, funcionario_id)
            print("=-" * 50)

        case 6:

            print("\n Cadastrar Tarefa:")
            print("=-" * 50)

            descricao = input("Descrição: ")
            projeto_id = ler_numero("Id do projeto: ", int)

            cadastrar_tarefa(descricao, projeto_id)
            print("=-" * 50)

        case 7:

            print("\n Atualizar Salário:")
            print("=-" * 50)

            id_funcionario = ler_numero("Id do funcionário: ", int)
            novo_salario = ler_numero("Novo salário: ", float)

            atualizar_salario(id_funcionario, novo_salario)
            print("=-" * 50)

        case 8:

            print("\n Atualizar Projeto:")
            print("=-" * 50)

            id_projeto = ler_numero("Id do projeto: ", int)
            novo_titulo = input("Novo título: ")

            atualizar_projeto(id_projeto, novo_titulo)
            print("=-" * 50)

        case 9:

            print("\n Atualizar descrição da tarefa:")
            print("=-" * 50)

            id_tarefa = ler_numero("Id da tarefa: ", int)
            nova_descricao = input("Nova descrição: ")

            atualizar_descricao_tarefa(id_tarefa, nova_descricao)
            print("=-" * 50)

        case 10:
            print("\n Atualizar status da tarefa:")
            print("=-" * 50)

            id_tarefa = ler_numero("Id da tarefa: ", int)
            opcao = ler_confirmacao("Concluída? (Sim = 1 | Não = 0): ")

            concluida = opcao == 1

            atualizar_status_tarefa(id_tarefa, concluida)

            print("=-" * 50)

        case 11:

            print("\n Deletar funcionário:")
            print("=-" * 50)

            id_funcionario = ler_numero("Id do funcionário: ", int)

            opcao = ler_confirmacao("Tem certeza que deseja deletar esse funcionário? (Sim = 1 | Não = 0): ")

            if opcao == 1:
                deletar_funcionario(id_funcionario)

            else:
                print("\n Exclusão cancelada!")

            print("=-" * 50)

        case 12:

            print("\n Deletar projeto:")
            print("=-" * 50)

            id_projeto = ler_numero("Id do projeto: ", int)

            opcao = ler_confirmacao("Tem certeza que deseja deletar esse projeto? (Sim = 1 | Não = 0): ")

            if opcao == 1:
                deletar_projeto(id_projeto)

            else:
                print("\n Exclusão cancelada!")

            print("=-" * 50)

        case 13:

            print("\n Deletar tarefa:")
            print("=-" * 50)

            id_tarefa = ler_numero("Id da tarefa: ", int)

            opcao = ler_confirmacao("Tem certeza que deseja deletar essa tarefa? (Sim = 1 | Não = 0): ")

            if opcao == 1:
                deletar_tarefa(id_tarefa)

            else:
                print("\n Exclusão cancelada!")

            print("=-" * 50)

        case _:
            print("\nOpção inválida! Tente um número de 0 até 13 !\n")
