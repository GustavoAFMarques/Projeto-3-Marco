# Desafio 1 - Sistema de Votação de Representantes de Classe

candidatos_validos = ["ana", "bruno", "carlos"]
votos = []

print("Candidatos:")
print("1. Ana")
print("2. Bruno")
print("3. Carlos")
print()

while True:
    entrada = input("Digite o nome do candidato (fim para encerrar): ").strip().lower()

    if entrada == "fim":
        break
    elif entrada in candidatos_validos:
        votos.append(entrada)
        print(f"Voto registrado para {entrada.capitalize()}.")
    else:
        print("Voto inválido. Tente novamente.")

    print()

# Contagem de votos
votos_ana    = votos.count("ana")
votos_bruno  = votos.count("bruno")
votos_carlos = votos.count("carlos")

print()
print("Resultado da votação:")
print(f"Ana: {votos_ana} votos")
print(f"Bruno: {votos_bruno} votos")
print(f"Carlos: {votos_carlos} votos")

maior = max(votos_ana, votos_bruno, votos_carlos)

vencedores = []
if votos_ana == maior:
    vencedores.append("Ana")
if votos_bruno == maior:
    vencedores.append("Bruno")
if votos_carlos == maior:
    vencedores.append("Carlos")

if len(vencedores) == 1:
    print(f"O vencedor é: {vencedores[0]}")
else:
    print("Houve um empate entre os candidatos.")
