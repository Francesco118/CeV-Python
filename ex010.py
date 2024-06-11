#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar considere 1 USD igual a 3.27 BRL
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = dinheiro / 5.27
print(f'Com R${dinheiro:.2f} você pode comprar US${dolar:.2f}')