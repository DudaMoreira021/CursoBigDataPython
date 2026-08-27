# 26/08

# Palavra chave = reutilizar

# list / set / tuple / dict 

#V.ENV

def calculadora_v1(num1,num2,operador="3"): #aqui criamos uma função, tipo print, algo que comanda a operação
    # num1=float(input("Digite seu primeiro número:"))
    # num2=float(input("Digite seu segundo número:"))

    # operador=input("Informe a operação desejada entre: 1. adição; 2.subtração; 3. multiplicação; 4.divisão.")

    match operador:
        case "1":
            print(f"Resultado{num1+num2}.")
        case "2":
                print(f"Resultado{num1-num2}.") 
        case "3":
                print(f"Resultado{num1*num2}.")
        case "4":
            if num2!=0:                             #if = se / else= será 
                print(f"Resultado{num1/num2}.")                  
            else:
                print(f"errou rude demaisssss!") 
        case _:
                print("Informe um número de operador válido.")

# calculadora_v1 (200,500,"1") #fazemos isso para chamar a função, como fazemos com print.


calculinho = calculadora_v1(200,500)

calculinho




