import random

print("""VAMOS JOGAR Jokenpô?""")

qntd_vitorias_computador = 0
qntd_vitorias_usuario = 0
opcao_jogar = 'S'
while(opcao_jogar.upper() == 'S'):
    opcao_usuario = input("PEDRA, PAPEL ou TESOURA?")
    opcao_computador = ['PEDRA','PAPEL','TESOURA']

    jogada_usuario = opcao_usuario.upper()
    jogada_computador = random.choice(opcao_computador)
    if opcao_jogar.upper() == 'S':
        if jogada_usuario == jogada_computador:
            print(f"A SUA OPÇÃO FOI {jogada_usuario} X OPÇÃO DO COMPUTADOR foi {jogada_computador}")
            print("\033[34mEMPATE\033[0m")
        elif jogada_computador == "TESOURA" and jogada_usuario == "PAPEL":
            print(f"A SUA OPÇÃO FOI {jogada_usuario} X OPÇÃO DO COMPUTADOR foi {jogada_computador}")
            print("\033[31mO Computador venceu!\033[0m")
            qntd_vitorias_computador += 1
        elif jogada_computador == "PAPEL" and jogada_usuario == "PEDRA":
            print(f"A SUA OPÇÃO FOI{jogada_usuario} X OPÇÃO DO COMPUTADOR foi {jogada_computador}")
            print("\033[31mO Computador venceu!\033[0m")
            qntd_vitorias_computador += 1
        elif jogada_computador == "PEDRA" and jogada_usuario == "TESOURA":
            print(f"A SUA OPÇÃO FOI {jogada_usuario} X OPÇÃO DO COMPUTADOR foi {jogada_computador}")
            print("\033[31mO Computador venceu!\033[0m")
            qntd_vitorias_computador += 1
            
        elif jogada_usuario == "TESOURA" and jogada_computador == "PAPEL":
            print(f"A SUA OPÇÃO FOI {jogada_usuario} X OPÇÃO DO COMPUTADOR foi {jogada_computador}")
            print("\033[32mVocê venceu!\033[0m")
            qntd_vitorias_usuario += 1
        elif  jogada_usuario == "PAPEL" and jogada_computador == "PEDRA":
            print(f"A SUA OPÇÃO FOI {jogada_usuario} X OPÇÃO DO COMPUTADOR foi {jogada_computador}")
            print("\033[32mVocê venceu!\033[0m")
            qntd_vitorias_usuario += 1
        elif jogada_usuario == "PEDRA" and jogada_computador == "TESOURA":
            print(f"A SUA OPÇÃO FOI {jogada_usuario} X OPÇÃO DO COMPUTADOR foi {jogada_computador}")
            print("\033[32mVocê venceu!\033[0m")
            qntd_vitorias_usuario += 1
        
        opcao_jogar = input("Deseja continuar o jogo? S/N")

def pontuacao():
    if qntd_vitorias_usuario > qntd_vitorias_computador:
        print("\033[32mPARABÉNS VOCÊ GANHOU!!!\033[0m")
        print(f"A quantidade de vitórias do Usuário foram {qntd_vitorias_usuario}")
        print(f"A quantidade de vitórias do Computador foram {qntd_vitorias_computador}")
    elif qntd_vitorias_computador > qntd_vitorias_usuario:
        print("\033[31mVOCÊ PERDEU :(\033[0m")
        print(f"A quantidade de vitórias do Computador foram {qntd_vitorias_computador}")
        print(f"A quantidade de vitórias do Usuário foram {qntd_vitorias_usuario}")
    elif qntd_vitorias_usuario == qntd_vitorias_computador:
        print("\033[34mEMPATOU!\033[0m")
        print(f"A quantidade de vitórias do Computador foram {qntd_vitorias_computador}")
        print(f"A quantidade de vitórias do Usuário foram {qntd_vitorias_usuario}")

pontuacao()
print("FIM")

    

    