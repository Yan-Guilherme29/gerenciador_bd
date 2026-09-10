from operacoes_funcionarios import *
from operacoes_projetos import *

print("=-" * 50)
print("Tabela funcionarios: ")

for funcionario in listar_funcionarios():

    print(f"\n ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]} | Salário: {funcionario[3]} | Departamento: {funcionario[4]} | Email: {funcionario[5]}  ")

print("=-"*50)
print("Tabela projetos: ")

for projeto in listar_projetos():

    print(f"\n ID: {projeto[0]} | Título: {projeto[1]} | Funcionário ID: {projeto[2]} ")

print("=-"*50)
