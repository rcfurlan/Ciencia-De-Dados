 

""" Jogo de Advinhação """

import random

# Numero que deve ser advinhado
correto = random.randrange(1,100)

# Numero de tentativas
tentativa = 1

# Função para verificar se a string é um número
def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

# Controle de acerto da resposta	
acertou = False

print('\n*******************************')
print('*     Jogo da Adivinhação     *')
print('*******************************')
print('\n')

# Interface da calculadora	
while not acertou:
	
	chute = input('\nDigite seu chute de 1 a 100:  ')
	
	# Caso o usuário entre com chute em formato incorreto, reinicia a interface
	if isInt(chute) == False:
		print('\n\nOpção inválida. O chute deve ser um número inteiro !!!\n\n')
		input('\nTecle Enter para continuar...\n\n')
		continue
	
	# Caso o usuário entre com chute fora do intervalo do jogo
	if int(chute) not in list(range(1,101)):
		print('\n\nOpção inválida. Ô Burrice ... mentecapito ... é entre 1 e 100 !!!\n\n')
		input('\nTecle Enter para continuar...\n\n')
		continue
	
	# Caso o usuário entre com chute em formato correto, converte para int	
	chute = int(chute)

	# Descobre se o chute esta correto ou nao
	acertou = correto == chute
	maior = chute > correto
	menor = chute < correto
	
	# Executa a opção desejada
	if acertou and tentativa == 1:
		mensagem = 'Maluco cagado da porra, acertou de prima !!!!!!'
	elif acertou and tentativa > 1:
		mensagem = 'Ahhhh MULEKE ... resposta correta depois de {} tentativas !!!!!!'.format(tentativa)
	elif maior:
		mensagem = 'Errouuuuuuuuu ... chutou alto. Tenta de novo.'
	else: 
		mensagem = 'Errouuuuuuuuu ... chutou baixo. Tenta de novo.'
		
	tentativa += 1
		
	print('\n\n',mensagem,'\n\n')
	print('\n')

	
input('\nTecle Enter para sair...\n\n')
	
	
		
	
	
	
	