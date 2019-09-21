

""" Programa para calcular as ra?zes de uma Equa??o de 2? Grau """

import math
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

# Cria a caixa de dialogo para receber os valores
root = tk.Tk()
root.withdraw()

a = float(simpledialog.askstring(title="Entrada de Coeficientes da Eq.",prompt="Entre com o valor de A:"))
b = float(simpledialog.askstring(title="Entrada de Coeficientes da Eq.",prompt="Entre com o valor de B:"))
c = float(simpledialog.askstring(title="Entrada de Coeficientes da Eq.",prompt="Entre com o valor de C:"))

# Calculo do Delta
delta = b ** b - ( 4 * a * c )

# Calcula as raizes a partir do resultado do delta
if delta > 0:
    x1 = (( -1 * b ) - math.sqrt(delta)) / ( 2 * a )
    x2 = (( -1 * b ) + math.sqrt(delta)) / ( 2 * a )
    resultado = 'A equacao possui duas raizes reais distintas e iguais a \n  x1 = {:.2f} \n    e \n  x2 = {:.2f}'.format(x1,x2)
elif delta == 0:
    x = ( -1 * b ) / ( 2 * a )
    resultado = 'A equacao possui duas raizes reais e iguais a x1 = x2 = {:.2f}'.format(x)
else:
    resultado = "A equacao nao possui raizes reais !!!"

# Exibe um MessageBox com o resultado obtido
messagebox.showinfo('Resultado', resultado)
	
	