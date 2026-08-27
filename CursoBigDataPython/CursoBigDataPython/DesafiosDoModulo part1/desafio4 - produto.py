# 4. Código de Origem do Produto:
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região
# de sua procedência, conforme a tabela abaixo:
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser
# encarado como “Importado


#for i in range(3):





try:
        codigo = int(input("Qual código?:"))

        match codigo:

                case 1:
                    print("O número 1 corresponde a região Sul.")
                case 2:
                    print("O número 2 corresponde a região Norte.")
                case 3:
                    print("O número 3 corresponde a região Leste.")
                case 4:
                    print("O número 4 corresponde a região Oeste.")
                case 5:
                    print("O número 5 corresponde a região Nordeste.")
                case 6:
                    print("O número 6 corresponde a região Nordeste.")
                case 7:
                    print("O número 7 corresponde a região Sudeste.")
                case 8:
                    print("O número 8 corresponde a região Sudeste.")    
                case 9:
                        print("O número 9 corresponde a região Sudeste.")
                case 10:
                        print("O número 10 corresponde a região Centro-oeste.") 
                case 11:
                        print("O número 11 corresponde a região Noroeste.")

                case _:
                    print(f"Número {codigo} inválido. Digite entre 1 e 11.")


except ValueError:
    print("Entrada inválida, número importado. Por favor digite o código novamente.")

     
