#identificar variáveis e constantes
#constante sempre em letra maiúscula


POTENCIA = float (input("Digite a potência da lampada(3w):"))
largura = float(input("digite a largura do comomodo(5m)"))
comprimento = float(input("digite o comprimento do comodo(5m)"))
area = largura * comprimento
potencia_necessaria = area * 3

lampadas = potencia_necessaria / POTENCIA

if lampadas % 1 != 0:
    lampadas = int(lampadas) + 1
else=
    lampadas = int(lampadas)


