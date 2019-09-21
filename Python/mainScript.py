

"""

A variável name
No Python, arquivos .py são chamados de módulos. Cada módulo pode ser executado diretamente, como um programa em si, ou importado por outro módulo.

Precisamos, de alguma maneira, identificar essa diferença. Para isso, temos uma variável nativa que pode nos auxiliar nisso - a __name__, 
que nos indica o nome do contexto em que o módulo está rodando.

Resumindo, a variável __name__ representa o nome do módulo. Entretanto, quando o módulo é executado por si só como um programa, __name__ é definido para ’__main__’, 
diferente de quando o módulo é importado, no qual o valor fica de fato igual ao nome do módulo.

"""

# Obs.: poderia ter sido criado um arquivo impressora.py e substituir a definicao de classe aqui por "import impressora"
class Impressora():

	def imprime(self):
		print('A instancia da classe impressora')

# Metodo com o corpo principal do programa
def main():
	impressora = Impressora()
	impressora.imprime()
	
# Execucao do corpo principal do programa caso esse modulo seja executado com "python mainScript.py"
if __name__ == '__main__':
	main()
	


