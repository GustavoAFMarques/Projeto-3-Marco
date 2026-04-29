# Desafio 2 - Editor de Texto com Opção de Desfazer (Pilha)

texto = []

while True:
    print()
    print("EDITOR DE TEXTO")
    print("[1] - Digitar palavra")
    print("[2] - Desfazer última palavra")
    print("[3] - Mostrar texto")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        palavra = input("Digite uma palavra: ").strip()
        if palavra != "":
            texto.append(palavra)
            print(f"Palavra adicionada: {palavra}")
        else:
            print("Nenhuma palavra digitada.")

    elif opcao == "2":
        if len(texto) == 0:
            print("Não há palavras para desfazer.")
        else:
            palavra_removida = texto.pop()
            print(f"Palavra removida: {palavra_removida}")

    elif opcao == "3":
        if len(texto) == 0:
            print("O texto está vazio.")
        else:
            print("Texto atual:", " ".join(texto))

    elif opcao == "4":
        print("Encerrando o editor.")
        break

    else:
        print("Opção inválida. Escolha entre 1 e 4.")
