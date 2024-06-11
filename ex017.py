#Faça um programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
cateto_o = float(input("Digite o valor do cateto o posto: "))
cateto_a = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto_a, cateto_o)
print(f"O valor da hipotenusa é: {hipotenusa:.2f}")
