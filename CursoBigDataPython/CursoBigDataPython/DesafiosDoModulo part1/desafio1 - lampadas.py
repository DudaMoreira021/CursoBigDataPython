#identificar variáveis e constantes
#constante sempre em letra maiúscula


potencia = float(input("Qual a potência da lâmpada? "))

largura = float(input("Qual a largura do cômodo? "))

comprimento = float(input("Qual o comprimento do cômodo? "))

area = largura * comprimento

potencia = area * 3

lampadas = potencia / potencia

bocais = area / 3

print("Área do cômodo:", area, "m²")
print("Potência necessária:", potencia, "watts")
print("Quantidade de lâmpadas:", lampadas)
print("Quantidade de bocais:", bocais)

