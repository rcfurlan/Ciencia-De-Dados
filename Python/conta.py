
import datetime

class Conta:
	"""
	Banco SeuDinheiro
	2019
	
	Objeto : Conta corrente do banco
	"""
	
	_totalDeContas = 0
	
	def __init__(self, numero, cliente, saldo, limite = 1000.00):
		self._numero = numero
		self._titular = cliente
		self._saldo = saldo
		self._limite = limite
		self._historico = Historico()
		Conta._totalDeContas += 1
	
	@staticmethod
	def totalDeContas():
		return Conta._totalDeContas
	
	@property
	def numero(self):
		return self._numero
	
	@property
	def limite(self):
		return self._limite
	
	@limite.setter
	def limite(self, limite):
		if limite <= 0:
			print('Nao podemos ter limite menor ou igual a zero')
		else:
			self._limite = limite
		
	def deposita(self, valor):
		self._saldo += valor
		self._historico.transacoes.append('Deposito no valor de : {}'.format(valor))
		
	def saca(self, valor):
		if self._saldo < valor:
			return False
		else:
			self._saldo -= valor
			self._historico.transacoes.append('Saque no valor de : {}'.format(valor))
			return True
			
	def recebeTransferenciaDe(self, conta, valor):
		self._saldo += valor
		self._historico.transacoes.append('Transferencia recebida da conta {1} para conta {0} no valor de : {2}'.format(self._numero, conta.numero, valor))
			
			
	def transferePara(self, conta, valor):
		if self._saldo < valor:
			return False
		else:
			self._saldo -= valor
			conta.recebeTransferenciaDe(self, valor)
			self._historico.transacoes.append('Transferencia realizada da conta {0} para conta {1} no valor de : {2}'.format(self._numero, conta.numero, valor))
			return True
	
	def extrato(self):
		self._historico.transacoes.append('Extrato em {} - Saldo de {}'.format(datetime.datetime.today(), self._saldo))
		print('\n\n Conta    : {} \n Abertura : {} \n Titular  : {} \n Saldo    : {}'.format(self._numero, self._historico.dataAbetura, self._titular.nome + ' ' + self._titular.sobrenome, self._saldo))
		
	def saldoAtual(self):
		self._historico.transacoes.append('Saldo {} em {} '.format(self._saldo, datetime.datetime.today()))
		print('Saldo atual : {}'.format(self.saldo))
		
	def imprimeHistoricoTransacoes(self):
		self._historico.imprime()
	

	
class Historico:
	"""
	Banco Seu Dinheiro
	2019
	
	Objeto : Historico de Transacoes da conta
	"""
	
	def __init__(self):
		self._dataAbetura = datetime.datetime.today()
		self._transacoes = []
		
	@property
	def dataAbetura(self):
		return self._dataAbetura
		
	@property
	def transacoes(self):
		return self._transacoes
		
	@transacoes.setter
	def transacoes(self, transacoes):
		self._transacoes = transacoes
		
	def imprime(self):
		print('\n\n Data de abertura : {}'.format(self._dataAbetura))
		print(' Transacoes :')
		for i,t in enumerate(self._transacoes):
			print(' {} - {}'.format(i + 1,t))
			

			
class Cliente:
	"""
	Banco SeuDinheiro
	2019
	
	Objeto : Cliente do banco
	"""
	
	def __init__(self, nome, sobrenome, cpf):
		self._nome = nome
		self._sobrenome = sobrenome
		self._cpf = cpf
	
	"""
	Cria uma seguranca para a classe trabalhar somente com esses atributos
	Mas a principal funcionalidade do slots é dar ganho em uso de memoria
	"""
	__slots__ = ['_nome','_sobrenome','_cpf']	
		
	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self, nome):
		self._nome = nome
		
	@property
	def sobrenome(self):
		return self._sobrenome
		
	@sobrenome.setter
	def sobrenome(self, sobrenome):
		self._sobrenome = sobrenome
	
	@property
	def cpf(self):
		return self._cpf
		
	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf
		
		
		
	
	
		
	