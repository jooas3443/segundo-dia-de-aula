materiais = {
    "mouse": 10,
    "teclado": 6,
    "cabo": 20
}

nome = input("Qual material deseja retirar? ").strip().lower()

try:
    quantidade = int(input("Quantas unidades? "))

    if nome not in materiais:
        print("Material não encontrado!")

    elif quantidade <= 0:
        print("A quantidade deve ser maior que zero!")

    elif quantidade > materiais[nome]:
        print("Estoque insuficiente!")
        print("Quantidade disponível:", materiais[nome])

    else:
        materiais[nome] -= quantidade
        print("Retirada realizada com sucesso!")

    print("\n--- ESTOQUE ATUALIZADO ---")
    for material, qtd in materiais.items():
        print(f"{material.capitalize()}: {qtd} unidades")

except ValueError:
    print("Digite uma quantidade numérica válida!")