
import math

class Calcula:
	"""
	Banco SeuDinheiro
	2019
	
	Objeto : Conta corrente do banco
	"""
	
	def __init__(self):
		pass
	
		
	@classmethod
	def soma(cls,*args):
	
		resultado = 0
		
		for n in args:
			resultado += n
			
		return resultado
		
		
	@classmethod
	def subtracao(cls,a,b):
		
		return a - b
		
	
	@classmethod
	def multiplicacao(cls,*args):
	
		resultado = 1
		
		for n in args:
			resultado *= n
			
		return resultado
		
	
	@classmethod
	def divisao(cls,a,b):
		
		return a / b
		
	@classmethod
	def raizQuadrada(cls,n):
	
		return n ** (1/2)
		
	@classmethod
	def raizEnezima(cls,n,k):
	
		return n ** (1/k)		
		
	
	@classmethod
	def eq2Grau(cls,a,b,c):
	
		resultado = ''
		
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
		
		print(resultado)
		
	@classmethod
	def determinante2X2(cls,matriz):
		diagonal_principal = 1
		diagonal_secundaria = 1
		
		for i, n in enumerate(matriz):
			for j, m in enumerate(n):
				if i == j:
					diagonal_principal *= m
				if i != j:
					diagonal_secundaria *= m
					
		resultado = diagonal_principal - diagonal_secundaria
		
		print('O determinante é : {}'.format(resultado))
		
	
	@classmethod
	def determinante3X3(cls,matriz):
		
		# Desenvolvido pela regra de Sarrus
		# Para teste: [[2,5,6],[1,6,7],[-1,2,3]] --> 13 - 7 = 6
		
		matriz_l = matriz
	
		for i, m in enumerate(matriz):
			matriz_l[i].extend(matriz_l[i][:2])
			
		diagonal_principal_1, diagonal_principal_2, diagonal_principal_3  = 1, 1, 1
		diagonal_secundaria_1, diagonal_secundaria_2, diagonal_secundaria_3 = 1, 1, 1
		
		for i, n in enumerate(matriz_l):
			for j, m in enumerate(n):
				if j - i == 0:
					diagonal_principal_1 *= m
				if j - i == 1:
					diagonal_principal_2 *= m
				if j - i == 2:
					diagonal_principal_3 *= m
				if i + j == 2:
					diagonal_secundaria_1 *= m
				if i + j == 3:
					diagonal_secundaria_2 *= m
				if i + j == 4:
					diagonal_secundaria_3 *= m
					
		diagonal_principal = diagonal_principal_1 + diagonal_principal_2 + diagonal_principal_3
		diagonal_secundaria = diagonal_secundaria_1 + diagonal_secundaria_2 + diagonal_secundaria_3
		resultado = diagonal_principal - diagonal_secundaria
		
		print('Diagonal principal ({}) + ({}) + ({}) = {}'.format(diagonal_principal_1,diagonal_principal_2,diagonal_principal_3,diagonal_principal))
		print('Diagonal secundaria ({}) + ({}) + ({}) = {}'.format(diagonal_secundaria_1,diagonal_secundaria_2,diagonal_secundaria_3,diagonal_secundaria))
		print('O determinante é : {}'.format(resultado))
		
		
		
		

		
	
		