

""" Calculadora para operações matemáticas simples """

# Configuracao inicial da calculadora
opcao = 0

# Função para verificar se a string é um número
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

# Interface da calculadora	
while opcao in (0,1,2,3,4,5,6):
	print('\n*********************** Python Calculator ***********************')
	print('\n')
	print('\nSelecione o número da operação desejada:')
	print('\n1 - Soma')
	print('\n2 - Subtração')
	print('\n3 - Multiplicação')
	print('\n4 - Divisão')
	print('\n5 - Potenciação')
	print('\n6 - Radiciação')	
	print('\n99 - Sair')
	print('\n')
	
	opcao = input('\nDigite sua opção (1/2/3/4/5/6/99):  ')
	
	# Sair
	if isfloat(opcao) == True:
		if int(float(opcao)) == 99:
			break	
			
	# Caso o usuário entre com opção inválida, reinicia a interface
	if isfloat(opcao) == False or (isfloat(opcao) == True and int(float(opcao)) not in (1,2,3,4,5,6)):
		opcao = 0
		print('\n\nOpção inválida !!!\n\n')
		input('\nTecle Enter para continuar...\n\n')
		continue
	
	# Recebe números somente em caso de opção válida
	num1 = input('\nDigite o primeiro número:  ')
	num2 = input('\nDigite o segundo número:  ')
	
	# Caso o usuário entre com dados incorretos, reinicia a interface
	if isfloat(num1) == False or isfloat(num2) == False:
		opcao = 0
		print('\n\nNúmeros entrados em formato inválido !!!\n\n')
		input('\nTecle Enter para continuar...\n\n')
		continue
		
	opcao = int(float(opcao))
	num1 = float(num1)
	num2 = float(num2)
	
	# Executa a opção desejada
	if opcao == 1:
		resultado = num1 + num2
		mensagem = 'Resultado de\n\n {} + {} = {}'.format(num1,num2,resultado)
	elif opcao == 2:
		resultado = num1 - num2
		mensagem = 'Resultado de\n\n {} - {} = {}'.format(num1,num2,resultado)
	elif opcao == 3:
		resultado = num1 * num2
		mensagem = 'Resultado de\n\n {} * {} = {}'.format(num1,num2,resultado)
	elif opcao == 4 and num2 == 0:
		mensagem = 'Não é possível dividir por zero'
	elif opcao == 4 and num2 != 0:
		resultado = num1 / num2
		mensagem = 'Resultado de\n\n {} / {} = {}'.format(num1,num2,resultado)
	elif opcao == 5:
		resultado = num1 ** num2
		mensagem = 'Resultado de\n\n {} ^ {} = {}'.format(num1,num2,resultado)
	elif opcao == 6:
		resultado = num1 ** ( 1 / num2 )
		mensagem = 'Resultado de\n\n {} ^ 1/{} = {}'.format(num1,num2,resultado)
	else: 
		mensagem = 'Digitar uma opção válida !!!'
		
	opcao = 0
	print('\n\n',mensagem,'\n\n')
	print('\n')
	input('\nTecle Enter para continuar...\n\n')
	
	
		
	
	
	
	