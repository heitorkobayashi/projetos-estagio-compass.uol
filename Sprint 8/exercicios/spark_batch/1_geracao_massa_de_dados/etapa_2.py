animais = [
    "Jaguar", "Cachorro", "Tigre", "Coala", "Elefante",
    "Urso", "Panda", "Macaco", "Crocodilo", "Tubarao",
    "Girafa", "Zebra", "Rinoceronte", "Peixe", "Raposa",
    "Sapo", "Coelho", "Cavalo", "Gorila", "Avestruz"
]

animais.sort()

for animal in animais:
    print(animal)


with open("lista_animais.csv", "w") as arquivo:
    for animal in animais:
        arquivo.write(animal + "\n")


print("\nArquivo salvo em: 'lista_animais.csv'.")
