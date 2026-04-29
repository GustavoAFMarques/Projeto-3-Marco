# Desafio 3 - Fila de Atendimento da Secretaria

fila = []
numero_senha = 100

while True:
    print()
    print("SECRETARIA ACADÊMICA")
    print("[1] - Retirar senha")
    print("[2] - Chamar próximo aluno")
    print("[3] - Mostrar fila")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome do aluno: ").strip()
        if nome != "":
            fila.append((numero_senha, nome))
            print(f"{nome} entrou na fila de atendimento.")
            numero_senha += 1
        else:
            print("Nome inválido.")

    elif opcao == "2":
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            senha, nome = fila.pop(0)
            print(f"Chamando aluno: {nome} (Senha {senha})")

    elif opcao == "3":
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            print("Fila atual:")
            for posicao, (senha, nome) in enumerate(fila, start=1):
                print(f"{posicao}º - {nome} (Senha {senha})")

    elif opcao == "4":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida. Escolha entre 1 e 4.")
