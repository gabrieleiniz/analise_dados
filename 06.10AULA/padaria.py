# SISTEMA DE PADARIA

print("=================================")
print("       PADARIA BOM SABOR")
print("=================================")

print("\nCARDÁPIO:")
print("1 - Pão francês      R$ 0,75")
print("2 - Pão de queijo    R$ 2,50")
print("3 - Coxinha          R$ 6,00")
print("4 - Café             R$ 3,00")
print("5 - Bolo             R$ 8,00")
print("6 - Suco             R$ 5,00")
print("0 - Finalizar pedido")

total = 0

while True:
    opcao = int(input("\nDigite o número do produto: "))

    if opcao == 0:
        break

    if opcao == 1:
        produto = "Pão francês"
        preco = 0.75
    elif opcao == 2:
        produto = "Pão de queijo"
        preco = 2.50
    elif opcao == 3:
        produto = "Coxinha"
        preco = 6.00
    elif opcao == 4:
        produto = "Café"
        preco = 3.00
    elif opcao == 5:
        produto = "Bolo"
        preco = 8.00
    elif opcao == 6:
        produto = "Suco"
        preco = 5.00
    else:
        print("Opção inválida!")
        continue

    quantidade = int(input("Digite a quantidade: "))

    subtotal = preco * quantidade
    total = total + subtotal

    print(quantidade, "x", produto)
    print("Subtotal: R$", subtotal)

print("\n=================================")
print("       RESUMO DA COMPRA")
print("=================================")
print("Valor total: R$", total)
print("Obrigado pela preferência!")