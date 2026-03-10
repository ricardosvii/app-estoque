estoque = {}

def cadastrar_produto():
    print("\n=== Cadastro de Produto ===")

    sku = input("SKU do produto: ")
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    localizacao = input("Localização no estoque: ")

    estoque[sku] = {
        "nome": nome,
        "quantidade": quantidade,
        "localizacao": localizacao
    }

    print("Produto cadastrado com sucesso!")


def ver_estoque():
    print("\n=== Estoque Atual ===")

    if not estoque:
        print("Estoque vazio.")
        return

    for sku, dados in estoque.items():
        print(f"""
SKU: {sku}
Produto: {dados['nome']}
Quantidade: {dados['quantidade']}
Localização: {dados['localizacao']}
""")


def buscar_produto():
    sku = input("Digite o SKU do produto: ")

    if sku in estoque:
        produto = estoque[sku]

        print(f"""
Produto encontrado:
Nome: {produto['nome']}
Quantidade: {produto['quantidade']}
Localização: {produto['localizacao']}
""")
    else:
        print("Produto não encontrado.")


def atualizar_quantidade():
    sku = input("SKU do produto: ")

    if sku in estoque:
        nova = int(input("Nova quantidade: "))
        estoque[sku]["quantidade"] = nova
        print("Quantidade atualizada!")
    else:
        print("Produto não encontrado.")


def alerta_estoque_baixo():

    print("\n=== ALERTA DE ESTOQUE BAIXO ===")

    for sku, dados in estoque.items():

        if dados["quantidade"] <= 5:

            print(f"""
Produto: {dados['nome']}
Quantidade: {dados['quantidade']}
""")


while True:

    print("""
======== STOCK VISION ========

1 - Cadastrar produto
2 - Ver estoque
3 - Buscar produto
4 - Atualizar quantidade
5 - Alertas estoque baixo
6 - Sair

==============================
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        ver_estoque()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        atualizar_quantidade()

    elif opcao == "5":
        alerta_estoque_baixo()

    elif opcao == "6":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida")
