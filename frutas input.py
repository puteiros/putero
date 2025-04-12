frutas = ["banana", "maca", "tomate"]
legumes = ["cenoura", "abobora", "alface"]

alimento = input("digite o nome de um alimento: ")

if alimento in frutas:
    print(f"{alimento} é uma fruta")
elif alimento in legumes:
    print(f"{alimento} é um legume")
else:
    print(f"o item nao esta na lista")
    