#Um professor quer sortear um dos 4 alunos para pagar o quadro faça um programa que o ajude, lendo o nome deles, e escrevendo o nome do escolhido.
import random
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
sorteado = random.random(a,b,c,d)
print(f'O escolhido é: {sorteado}')