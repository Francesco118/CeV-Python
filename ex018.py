#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosneme tangente desse ângulo.
import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f'O ângulo de {ang} graus tem:\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')