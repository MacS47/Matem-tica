# -----------------------------------------------------------
# Essa função tem como objetivo encontrar os valores para os 
# catetos e a hipotenusa de um triângulo retângulo 
# utilizando o Teorema de Pitágoras h²= a² + b²
# -----------------------------------------------------------

import math
import os


# Essa função tem como objetivo limpar o Console de execução.
# Funciona tanto em sistemas operacionais Linux quanto em Windows

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# A função pitagoras receberá três parâmetros:
# * h - hipotenusa
# * a - 1º cateto
# * b - 2º Cateto

def pitagoras(h = 0, a = 0, b = 0):
    
    # Essa primeira verificação verifica se existem valores, negativos ou positivos para
    # ao menos duas variáveis

    if (h != 0 and a != 0 ) or (h != 0 and b != 0) or (a != 0 and b != 0):

        # Após receber os valores, será verificado qual deles está ausente e calculado seuu valor

        if h == 0 and a != 0 and b != 0:    # Verificando e calculando h
            h = math.sqrt((a**2)+(b**2))
            result = h
        elif a == 0 and h != 0 and b != 0:  # Verificando e calculando a
            a = math.sqrt((h**2)-(b**2))
            result = a
        elif b == 0 and a != 0 and h!= 0:   # Verificando e calculando b
            b = math.sqrt((h**2)-(a**2))
            result = b
        modelo= (f"\n\t|\ \n\t| \ \n {a:.2f}\t|  \ \n\t|   \ {h:.2f} \n\t|    \ \n\t|_____\ \n	  {b:.2f}")
        return result, modelo
    else:
        # Caso não sejam informados, ao menos dois valores inteiros diferentes de 0
        # a função retornará um aviso
        aviso = f"\n\nVocê deve informar ao menos dois valores inteiros!\n"
        modelo= (f"\n\t|\ \n\t| \ \n {a:.2f}\t|  \ \n\t|   \ {h:.2f} \n\t|    \ \n\t|_____\ \n	  {b:.2f}")
        return 0, aviso + modelo

  
# clear() para limpar o console em seguida pitagoras(a = 4, h = 9) que irá determinar o valor de b

clear()  
variable = pitagoras(a = 4, h = 9)
print(f"O valor desconhecido no seu triângulo retângulo é {variable[0]:.2f} \n{variable[1]}")

variable = pitagoras(a = 4, b = 4)
print(f"O valor desconhecido no seu triângulo retângulo é {variable[0]:.2f} \n{variable[1]}")
