# 5. Média do Aluno com Optativa:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0

# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
# resultado final.


nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
optativa = float(input("Digite a nota da optativa:"))

if optativa != -1:
    if nota1 < nota2:
        nota1 = optativa
    else:
        nota2 = optativa

media = (nota1 + nota2) / 2

if media >= 6.0:
    print("Aprovado")
elif media < 3.0:
    print("Reprovado")
else:
    print("Recuperação")