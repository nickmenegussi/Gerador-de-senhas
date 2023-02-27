from pyfiglet  import Figlet as fg
from termcolor import colored
from random import choice
from time import sleep

def apresentarprograma():
    f = fg(font="standard")
    print(colored(f.renderText(" Bem vindo"), 'blue'))
    

def cores():
    print(colored("-"*55, 'green'))

def escolhasenha1():
    try:
        caracter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tamanhosenha = int(input("Quantos caracteres quer que sua senha tenha? "))
        senha_forte = ''
        for x in range(tamanhosenha):
            senha_forte += choice(caracter)
        salvar = str(input("\033[1;35mDeseja salvar a senha em um arquivo de texto? [S/N]: \033[m"))
        if salvar in 'Nn':
            print("Voce optou por não salvar.")
        else:
            with open('senhas.txt', 'a', newline='') as arquivo:
                arquivo.write(f" Senha: {senha_forte}")
                print("Salvada com sucesso!")      
                cores()  
    except (ValueError, TypeError):
        print("Erro de tipo de valor.")
    finally:
        print("Encerrando o programa...")
        sleep(1)
        print("=== VOLTE SEMPRE!! ===")

def escolhasenha2():
    try:
        caracter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567891011121314151617181920212223242578798081828384858687888990919293949596979899100"
        tamanhosenha = int(input("Quantos caracteres quer que sua senha tenha?"))
        senha_forte = ''
        for n in range(tamanhosenha):
            senha_forte += choice(caracter)
        salvar = str(input("\033[1;35mDeseja salvar a senha em um arquivo de texto? [S/N]: \033[m"))
        if salvar in 'Nn':
            print("Voce optou por não salvar.")
        else:
            with open("Senhas.txt", 'a', newline='') as arquivo:
                arquivo.write(f" Senha: {senha_forte}")
                print("Arquivo salvado com sucesso!!")
                cores()
    except (ValueError, TypeError):
        print("Erro de tipo de valor.")
    finally:
        print("Encerrando o programa...")
        sleep(1)
        print("=== VOLTE SEMPRE!! ===")
def escolhasenha3():
    try:
        caracter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789101112131415161718192021222324258687888990919293949596979899100!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        tamanhosenha = int(input("Quantos caracteres quer que sua senha tenha?"))
        senha_forte = ''
        for n in range(tamanhosenha):
            senha_forte += choice(caracter)
        salvar = str(input("\033[1;35mDeseja salvar a senha em um arquivo de texto? [S/N]: \033[m"))
        if salvar in 'Nn':
            print("Voce optou por não salvar.")
        else:
            with open("Senhas.txt", 'a', newline='') as arquivo:
                arquivo.write(f" Senha: {senha_forte}")
                print("Arquivo salvado com sucesso!!")
                cores()
    except (ValueError, TypeError):
        print("Erro de tipo de valor.")
    finally:
        print("Encerrando o programa...")
        sleep(1)
        print("=== VOLTE SEMPRE!! ===")