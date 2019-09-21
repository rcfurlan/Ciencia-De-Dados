 
import sys

palavra_anterior = ''
contador = 0
resultado = {}

for linha in sys.stdin:
    if linha.split()[0] == palavra_anterior:	    
	    contador += int(linha.split()[1])	
    else:
        contador = 1

    palavra_anterior = linha.split()[0]
    resultado[linha.split()[0]] = contador
	
for chave in resultado:
    print('{} {}'.format(chave,resultado[chave]))