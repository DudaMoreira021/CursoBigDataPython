# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.



combustivel = 6.15

inicio = float(input("Odômetro no início do dia:"))
final = float(input("Odômetro no final do dia:"))
litros = float(input("Litros de combustível gastos:"))
recebido = float(input("Valor recebido dos passageiros:"))     

km = final - inicio
consumo = km / litros
gasto_combustivel = litros * combustivel
lucro = recebido - gasto_combustivel

print("Consumo médio:", consumo, "km/L")
print("Lucro líquido: R$", lucro)