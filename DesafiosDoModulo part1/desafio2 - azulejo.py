#2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²

comprimento = float(input("Qual comprimento do cômodo?"))
largura = float(input("Qual largura do cômodo?"))
altura = float(input("Qual altura do cômodo?"))

Área = comprimento * largura 
caixa = 1,5
azulejo = Área * caixa

print ("Você precisa de:", azulejo, "caixas de azulejos. Volte sempre!")

