from uteis import apresentarprograma, cores, escolhasenha1, escolhasenha2 , escolhasenha3, choice

def escolhesenha():
    apresentarprograma()
    print("ao programa de Gerar senhas - \033[1;35mPara finalizar o programa digite 'Sair' ou '3' \033[m")
    while True:
        opcao = input("""\033[1;35mMenu de opções:\n[ 1 ] Escolher o que vai ter na senha\n[ 2 ] Gerar senha aleatoria\n[ 3 ] Sair\nSua opção:\033[m """)
        for opcoes in opcao:
            if opcoes in '1':
                cores()
                escolhersenha = input("""\033[1;35mTemos em nosso programa as seguintes opções de senha:\n[ 1 ]Só com letras\n[ 2 ]Com letras e números\n[ 3 ]Com letras,números e caracteres\nSua opção: \033[m""")
                if escolhersenha in '1':
                    escolhasenha1()
                elif escolhersenha in '2':
                    escolhasenha2()
                else:
                    escolhasenha3()
            else:
                if opcoes in '3' or opcoes in 'Sairsair':
                    exit()
                if opcoes > '3':
                    print(f"OPS, não encontramos o número {opcoes} em nossas opções.\nPor favor, repita.")
            if opcoes in '2':
                gerar_senha_aleatoria()
       
        
def gerar_senha_aleatoria():
    try:
        caracter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        tamanho = int(input("Qual é o tamanho da senha? "))
        senha_forte = ''
        for x in range(tamanho):
            senha_forte += choice(caracter)
        salvar = str(input("\033[1;35mDeseja salvar a senha em um arquivo de texto? [S/N]: \033[m"))
        if salvar in 'Nn':
            print("Voce optou por não salvar.")
        else:
            with open('Senhas.txt', 'a', newline='') as arquivo:
                arquivo.write(f" Senha: {senha_forte}")
                print("Salvada com sucesso!")      
                cores()                   
    except (ValueError, TypeError):
        print("Erro de tipo de valor.")
    finally:
        print("Encerrando o programa...")

escolhesenha()