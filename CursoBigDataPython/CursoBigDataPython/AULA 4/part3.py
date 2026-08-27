#identação! espaço correto entre os comandos e textos

#visão match case
mes = int(input("informe o mês de seu nascimento"))
match mes:
     case 1: 
        signo="aquario"
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


# | Situação                                           | Use                    |
# | -------------------------------------------------- | ---------------------- |
# | Preciso verificar uma **condição**                 | `if` / `elif` / `else` |
# | Tenho vários **valores específicos** para comparar | `match` / `case`       |
# | Quero saber se algo é maior, menor, igual etc.     | `if` / `elif`          |
# | Quero saber se o código é 1, 2, 3, 4...            | `match` / `case`       |
# | "Se nada disso acontecer..."                       | `else` ou `case _`     |


# Por exemplo, menu com 1, 2, 3, 4 combina muito naturalmente com match.

# Já uma média >= 6, < 3 etc. combina muito mais naturalmente com if/elif/else.