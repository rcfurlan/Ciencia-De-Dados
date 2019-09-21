
"""
Comando no Windows para testar:
> echo foo ach ach foo foo beux ach beux foo | python mapper_conta_palavras.py | python reducer_conta_palavras.py
""" 

import sys

lista = []

# Regra de mapeamento e transformação
for linha in sys.stdin:
   for palavra in linha.split():
       lista.append('{} 1'.format(palavra))
	   
lista_ordenada = sorted(lista)

for chave_valor in lista_ordenada:
    print(chave_valor)
