#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela ou sua porção inteira
import math
num = float(input('Digite um número real: '))
print('A porção inteira do número é: ', math.trunc(num))
#ou
print('A porção inteira do número é: ', int(num))
#ou
print(num//1)