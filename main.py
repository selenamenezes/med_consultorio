import sqlite3
from funcoes import *
import sys

conexao = sqlite3.connect('cadastro_paciente_consultorio.db')
cursor = conexao.cursor()

def main():
    while True:
        print("\n")
        tela()
        op = input('Digite uma opção: ')
        print("\n")

        if op == '1':
            print("=-=- Cadastro de paciente -=-=")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            nasc = input("Data de nascimento (AAAA-MM-DD): ")
            telefone = input("Telefone: ")
            cadastrar_paciente(conexao, nome, cpf, nasc, telefone)

        elif op == '2':
            print("=-=- Pacientes cadastrados -=-=")
            ler_dados(conexao)

        elif op == '3':
            print("=-=- Atualizar paciente -=-=")
            cpf = input('Digite o CPF do paciente: ')
            nome = input("Digite seu nome: ")
            nasc = input("Digite sua data de nascimento (AAAA-MM-DD): ")
            telefone = input("Digite seu telefone: ")
            atualizar_paciente(conexao, nome, cpf, nasc, telefone)

        elif op == '4':
            print("=-=- Remover paciente -=-=")
            cpf = input('Digite o CPF do paciente: ')
            remover_paciente(conexao, cpf)

        elif op == '5':
            print("Saindo...")
            conexao.close() 
            sys.exit()  

        else:
            print("Opção inválida. Digite uma opção válida.")

if __name__ == "__main__":
    main()