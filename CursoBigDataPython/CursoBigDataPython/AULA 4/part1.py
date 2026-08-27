#comando de input retorna com texto
#if  / elif / else



nome = input ("Informe seu nome:") #Peça um número ou texto ao usuário e 
#guarde esse número dentro da variável numero.
if nome=="Pyetro":
    resposta="Pyetro presente!"
elif nome== "Phellipe":
    resposta="Phellipe presente!"

#     #    número
#             ↓
#        é >= 0 ?
#         ↙       ↘
#       SIM       NÃO
#        ↓          ↓
#    Positivo    Negativo

#if significa "se".
#else significa "senão".

#tipo, se(if) for verdadeiro, faça isso. Senão (else), faça aquilo.

#if → primeira possibilidade
# elif → outras possibilidades que ainda têm uma condição
# else → o que sobra quando nenhuma condição foi atendida.

#if e elif dependem de uma condição ser verdadeira.
# else acontece quando nenhuma das condições anteriores foi verdadeira.

# IF/ELIF = "se isso acontecer..."
# ELSE = "se nada disso acontecer..."

# E tem uma consequência importante: else não pode existir sozinho.
# Ele precisa estar ligado a um if (e pode vir depois de vários elif).