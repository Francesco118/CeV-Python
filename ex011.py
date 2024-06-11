#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade digita necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input("Largura da parede em metros: "))
altura = float(input("Altura da parede em metros: "))
area = largura * altura
litros = area / 2
print(f"A área da parede é de {area:.2f}m² e você precisará de {litros:.2f} litros de tinta para pintá-la.")
#O :.2f é para formatar a saída para ter apenas 2 casas decimais
#O f antes da string é para formatar a string com as variáveis
#O {} é para indicar onde as variáveis devem ser substituídas na string