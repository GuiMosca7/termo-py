import random

# Lista de palavras
palavras = ["chaves", "tabelas", "cedula", "delete", "script"]

# Escolhe uma palavra aleatória no início
adivinhar = random.choice(palavras)

def menu():
    while True:
        print("\n========== MENU DE ENIGMAS ==========")
        print("1. Começar o Jogo")
        print("2. Ver Instruções")
        print("3. Desistir (caso não consiga adivinhar a palavra)")
        print("=====================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            jogar_enigma()
        elif escolha == '2':
            instrucoes()
        elif escolha == '3':
            print(f"\nVocê desistiu. A palavra era: {adivinhar}")
            break
        else:
            print("Opção inválida! Tente novamente.")

def instrucoes():
    print("\n========== INSTRUÇÕES ==========")
    print("1. Você deve tentar adivinhar a palavra secreta.")
    print("2. A cada tentativa, digite a palavra inteira.")
    print("3. O número de tentativas é ilimitado (ou até você desistir).")
    print("4. Não vale procurar as respostas na internet!")
    print("================================")

def jogar_enigma():
    tentativa = ""
    tentativas = 0

    print("\nDica: a palavra tem", len(adivinhar), "letras.")

    while tentativa != adivinhar:
        tentativa = input("Digite sua tentativa: ").lower()
        tentativas += 1

        if tentativa == adivinhar:
            print(f"\nParabéns! Você acertou a palavra '{adivinhar}' em {tentativas} tentativa(s)!")
            break
        else:
            print("Errado! Tente novamente.")

# Inicia o menu
menu()
