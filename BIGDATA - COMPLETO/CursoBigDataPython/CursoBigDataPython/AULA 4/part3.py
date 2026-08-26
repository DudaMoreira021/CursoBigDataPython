#visão match case
mes = int(input("informe o mês de seu nascimento"))
match mes:
     case 1: 
        signo:"aquario"
     case 2: 
        signo="peixes"
     case 3: 
        signo="áries"
     case 4: 
        signo="touro"
     case 5: 
        signo="gemeos"
     case _:
        signo= "número de mês inválido"

print(f"{signo}.")