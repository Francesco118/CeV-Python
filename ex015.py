#Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.k
#Calcule o preço a pagar sabendo que o carro custa R$60/dia e R$0,15/km
dias = int(input("Quantos dias você alugou o carro? "))
km = float(input("Quantos km você rodou? "))
custo_dias = dias * 60
custo_km = km * 0.15
total = custo_dias + custo_km
print(f"O total a pagar é de R${total:.2f}")
