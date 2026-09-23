preco = float(input("Qual o preço do produto? "))
quantidade = int(input("Em qual quantidade? "))
valor_total = preco*quantidade
print(f"Para {quantidade} de produtos com preço R${preco:.2f}, o valor total será de R${valor_total:.2f}")