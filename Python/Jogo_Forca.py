

""" Jogo da Forca """

from random import choice

# Controle de acerto da resposta	
acertou = False
enforcou = False
numero_erros = 0
numero_acertos = 0


# Escolher uma palavra aleatoriamente
arquivo = open('Jogo_Forca_Palavras.txt','r')
arquivo_linhas = arquivo.read().split('\n')

arquivo_palavras = []
for linhas in arquivo_linhas:
	palavras = linhas.split(' ')
	for palavra in palavras:
		arquivo_palavras.append(palavra)


# Palavra para adivinhar
palavra = choice(arquivo_palavras).upper()
palavra_oculta = ''
lista_palavra = []

for caracter in palavra:
	lista_caracter = [caracter,'F']
	lista_palavra.append(lista_caracter)

	
# Exibe para o jogador quantos caracteres tem a palavra
for posicao in palavra:
	palavra_oculta += '___ ' 
	

# Funcao para verificar se é uma letra	
def isStr(value):
  try:
    int(value)
    return False
  except ValueError:
    return True
	
	
# Funcao para verifica se o palpite esta certo
def verificaPalpite(palpite):
	
	palpite_certo = False
	
	for lista_caracter in lista_palavra:
		if lista_caracter[0] == palpite:
			lista_caracter[1] = 'V'
			palpite_certo = True
			
	return palpite_certo
	


print('\n\n*******************************')
print('*         Jogo da Forca       *')
print('*******************************')
print('\n\n\n\nTente adivinhar essa palavra: {}'.format(palavra_oculta))


# Interface do jogo	
while not acertou and not enforcou:

	palpite = input('\n\n\n\nDigite uma letra:  ').upper()
	
	
	# Caso o usuário digite um numero como palpite, reinicia a interface
	if isStr(palpite) == False:
		print('\n\nOpção inválida. O palpite deve ser uma letra !!!\n\n')
		input('\nTecle Enter para continuar...\n\n')
		continue
	
	
	# Caso o usuário digite mais de uma letra
	if len(palpite) > 1:
		print('\n\nOpção inválida. Burro do caralho .. É só uma letra !!!\n\n')
		input('\nTecle Enter para continuar...\n\n')
		continue		
		
	
	# Verfica se o palpite da esta correto
	if verificaPalpite(palpite):
		for lista_caracter in lista_palavra:
			if lista_caracter[0] == palpite:
				numero_acertos += 1
	else:
		numero_erros += 1
		
		
	# Atualiza o status do jogo
	acertou = numero_acertos == len(palavra)
	enforcou = numero_erros == 6
	
	
	# Exibe os palpites certos
	palavra_oculta = ''
	for lista_caracter in lista_palavra:			
			if lista_caracter[1] == 'V':
				palavra_oculta += ' {}  '.format(lista_caracter[0])
			else:
				palavra_oculta += '___ '
				
	
	# Exibe os acertos
	print('\n\n\n\n {}'.format(palavra_oculta))
	
	
	# Exibe a forca
	print('\n\n _____')
	print(' |    |')
	print(' |    O' if numero_erros >= 1 else ' |')
	if numero_erros == 2:
		print(' |   /')
	elif numero_erros == 3:
		print(' |   / \\')
	elif numero_erros >= 4:
		print(' |   /|\\')
	else:
		print(' |')
	if numero_erros == 5:
		print(' |   /')
	elif numero_erros >= 6:
		print(' |   / \\')
	else:
		print(' |')
	print(' |')
	print(' ======================')
	
	
if acertou:
	print('\n\nAhhhhhhh MULEKE ... descobriu a parada hein !!!!')
	print('\n\n──────▄▀▀═════════════▀▀▄         ')
	print('───────█═══════════════════█      ')
	print('──────█═════════════════════█     ')
	print('─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█    ')
	print('────█═══█████████═█████████═══█   ')
	print('────█══██▀────▀█████▀────▀██══█   ')
	print('───██████──█▀█──███──█▀█──██████  ')
	print('───██████──▀▀▀──███──▀▀▀──██████  ')
	print('────█══▀█▄────▄██─██▄────▄█▀══█   ')
	print('────█════▀█████▀───▀█████▀════█   ')
	print('────█═════════════════════════█   ')
	print('────█═════════════════════════█   ')
	print('────█═══════█▀█▀█▀█▀█▀█═══════█   ')
	print('────█═══════▀▄───────▄▀═══════█   ')
	print('───▐▓▓▌═══════▀▄█▄█▄▀═══════▐▓▓▌  ')
	print('───▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌  ')
	print('───█══▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌══█  ')
	print('──█══▌═▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌═▐══█ ')
	print('──█══█═▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌═█══█ ')
	print('──█══█═▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌═█══█ ')
	print('──█══█═▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌═█══█ ')
	print('──█══█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█══█ ')
	print('─▄█══█▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█══█▄')
	print('─█████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─█████')
	print('─██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─████  ')
	print('──▀█▀█──▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌───█▀█▀ ')
	print('─────────▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌         ')
	print('──────────▐▓▓▓▓▌──▐▓▓▓▓▌          ')
else:
	print('\n\n\n    Dançou nenem. Fica pra próxima !!! ')
	print('\n\n\n    Só pra voce saber, a palavra era : {}'.format(palavra))
	print('\n\n__________###_________')
	print('_________#___#________')
	print('_________#___#________')
	print('_________#===#________')
	print('_________#___#________')
	print('_________#___#________')
	print('_________#___#________')
	print('_________#___#________')
	print('_________#___#________')
	print('_________#___#________')
	print('_________#___#________')
	print('______####___####_____')
	print('_____#___#___#___####_')
	print('_____#___#___#___#___#')
	print('###__#___#___#___#___#')
	print('#__#_#___#___#___#___#')
	print('#___##___#___#___#___#')
	print('_#___#___#___#___#___#')
	print('__#__________________#')
	print('___#________________#_')
	print('____#______________#__')
	

input('\n\n\n\nTecle Enter para sair...\n\n')	




