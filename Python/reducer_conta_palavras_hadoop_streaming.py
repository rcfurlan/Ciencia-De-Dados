
#!/usr/bin/env python

import sys

palavra_anterior = ''
contador = 0

if __name__ == '__main__':

   # Regra de reducao e agregacao
   for linha in sys.stdin:
      if linha.split('\t')[0] == palavra_anterior or contador == 0:
         contador += int(linha.split('\t')[1])
      else:
         sys.stdout.write('{}\t{}\n'.format(palavra_anterior,contador))
         contador = 1

      palavra_anterior = linha.split('\t')[0]

   sys.stdout.write('{}\t{}\n'.format(palavra_anterior,contador))