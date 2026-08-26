# #RECAPTULANDO CONTEÚDO

# semana 1 = receita (txt/doc) OK
#            calculadora - a entregar 
#            ativ aula 2 - a entregar 

# semana 2 = versionar no github  OK
#            ativ aula 4 OK 
#            ativ aula 5  OK

#________________________________________________________________
#para paralizar o terminal(quebrar código) - SELECIONAR O TERMINAL E APERTAR CRTL + C = EM EMERGÊNCIAS! 

#no python o sistema conta do 0
#python descarta o ultimo numero

#RANGE = (__,__,__) = início  / final / gap = respectivamente 
#gap = repetição
#SHIFT + TAB = altera a linha do comando voltando
#TAB = altera a linha do comando para frente

#____________________________ÁREA DE TESTES_________________________________



# meunome = "Duda"

# for i in (meunome[2]):
#     print(i)


# for i in range(10):
#     print(i)


# for i in range(1,10,2):
#     print(i)


#WHILE:

# somador = int(input("Registro:"))
# controle = 0 

# while controle <= 30:
#     controle=controle+somador
#     somador = int(input("Registro:"))

# print("Oficina lotada!!!")


# acertou = 0

# while acertou < 5: #ao usar o =, tomar cuidado onde o looping irá quebrar, 
#     print(f"Número {acertou + 1} de 5:")
#     num = float(input("Digite um número: "))
 
#     dobro = num * 2
#     triplo = num * 3
#     quádruplo = num * 4
    
#     print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")

#     acertou+=1 # Incremento


    # except ValueError:
    # print("Entrada inválida. Tente novamente.")
    

#DO WHILE

contador = 0
limite = 5

while True: 
    if contador >= limite:
        break #PONTO DE DECISÃO: Se o limite for atingido, usamos BREAK(BREAK - PAUSE- CONTINUE)

    try:
        print(f"número {contador + 1} de {limite}:")
        num = float(input("Digite um número"))

    dobro = num * 2
    triplo = num * 3
    quádruplo = num * 4
    
    print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")

    acertou+=1 # Incremento
