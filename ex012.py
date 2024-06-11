#Faça um algo útil que leia o preço de um produto e mostra esse novo preço, com 5 % de desconto
produto = float(input("Digite o preço do produto: R$ "))
desconto = produto * 0.05
novo_preco = produto - desconto
print(f"O preço do produto com 5% de desconto é R$ {novo_preco:.2f}")