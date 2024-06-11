#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
print('Digite algo:')
algo = input()
print('O tipo primitivo é:', type(algo))
print('É alfanumérico?', algo.isalnum())
print('É alfabético?', algo.isalpha())
print('É um número?', algo.isnumeric())  #essa função só funciona com strings que contenham apenas números
print('É um decimal?', algo.replace('.', '', 1).isdigit()) #substitui o ponto por nada e verifica se é um número
print('É maiúscula?', algo.isupper())  #verifica se a string está toda em maiúscula
print('É minúscula?', algo.islower())  #verifica se a string está toda em minúscula
print('É um título?', algo.istitle())  #verifica se a string está formatada como um título (primeira letra de cada palavra em maiúscula)
print('É um espaço?', algo.isspace())  #verifica se a string é composta apenas por espaços
print('É capitalizada?', algo.capitalize() == algo)  #verifica se a string está capitalizada (primeira letra em maiúscula e o resto em minúscula)
#obs: o método capitalize() retorna uma string com a primeira letra em maiúscula e 
#o resto em minúscula, então se a string original for igual ao resultado do capitalize
#significa que a string já estava capitalizada
print('Pode ser impresso?', algo.isprintable())  #verifica se a string pode ser impressa (não contém caracteres de controle)
#obs: caracteres de controle são caracteres que não são visíveis, como o caractere de tab 
#ou o caractere de quebra de linha, por exemplo.
#essa função pode ser útil para verificar se uma string pode ser impressa em uma tela ou
#em um arquivo, por exemplo.
#obs2: essa função pode ser útil para verificar se uma string pode ser impressa em




