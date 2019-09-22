
"""
Entrada : A A A D E C C B E E E E E E E E C A B B B D B C A E D

Comando Hadoop-Streaming
$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar 
 -file /home/maria_dev/hadoop_streaming/mapper_hs.py    (envia o arquivo a cada nó do cluster antes do processamento, caso contrario é assumido que já estão lá)
 -file /home/maria_dev/hadoop_streaming/reducer_hs.py   (envia o arquivo a cada nó do cluster antes do processamento, caso contrario é assumido que já estão lá)
 -mapper "python mapper_hs.py" 
 -reducer "python reducer_hs.py" 
 -input entrada_ContaPalavras.txt                       (fazer o upload do arquivo para o HDFS antes)
 -output ContaPalavras                                  (gera saida no HDFS)
 
[maria_dev@sandbox-hdp ~]$ hdfs dfs -cat /user/maria_dev/ContaPalavras/part*    (visualizar o resultado)
A       5
B       5
C       4
D       3
E       10
"""


#!/usr/bin/env python

import sys

if __name__ == '__main__':

   # Regra de mapeamento e transformacao
   for linha in sys.stdin:
      for palavra in linha.split():
         sys.stdout.write('{}\t1\n'.format(palavra))
