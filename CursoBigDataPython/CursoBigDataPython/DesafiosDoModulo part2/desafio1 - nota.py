# 1. Cálculo de Média Escolar para Vários Alunos
# Use o laço for para repetir a lógica de cálculo de média e status
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.

for i in range(10):

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print("Média:", media)

    if media >= 6:
        print("Aprovado")
    elif media < 3:
        print("Reprovado")
    else:
        print("Recuperação")