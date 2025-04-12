itens = []

while True:
    print("\n==== MENU ====")
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - carrinho")
    print("4 - sair")

    opcao = input("digite uma opcao")
    if opcao == "1":
        item = input("digite o item: ")
        itens.append(item)
        print(f"item '{item}' adicionado a lista")
    elif opcao == "2":
        if itens:
            print("\nLista de items")
            for i, item in enumerate(itens):
                print(f"{i+1}. {item}")
            else:
                print("a lista esta vazia")

    elif opcao == "3":
        if itens:
            item = input("digite o item que deseja remover")
            if item in itens:
                itens.remove(item)
                print(f"o {item} foi removido")
            else:
                print("item nao encontrado")
        else:
            print("a lista esta vazia")
            
    elif opcao == "0":
        print("saindo...")
        break 

    else:
        print("oocao invalida")        