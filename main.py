 

from pacotes.objeto import Escala
import os.path
import os

def main() -> None:

	while True:
		comandos: dict = {1:adicionar,2:executar,3:folgas,4:imprimir_folgas}
		print('===========================================\n\t\tEscala\n===========================================\n1 - Adicionar funcionarios\n2 - Iniciar escala\n3 - Adicionar folgas\n4 - Consultar folgas\n5 - Sair')
		try:
			numero: int = int(input('Adicionar opção de comando: '))
		except ValueError:
			print('Comando invalido')
		
		try:
			if numero < 1 or numero > 5:
				print('===========================================')
				print('Numero invalido')
				print('===========================================')
			elif numero == 5:
				dia_semana: tuple = ('segunda','terça','quarta','quinta','sexta','sabado')
				opcao = int(input('deseja salvar alterações: 1 - sim 2 - não'))
				if opcao == 2:
					os.remove('operadores.txt')
					for dia in range(6):
						if os.path.isfile(dia_semana[dia]+'.txt'):
							os.remove(dia_semana[dia]+'.txt')
				break
			else:
				comandos[numero]()
		except UnboundLocalError:
			pass
		
def adicionar():
	
	dia_semana = ('segunda','terça','quarta','quinta','sexta','sabado')
	for semana_dia in range(6):
		if os.path.isfile(dia_semana[semana_dia]+'.txt'):
			os.remove(dia_semana[semana_dia]+'.txt')

	escala: Escala = Escala()
	escala.add_operadores()
	
	
def folgas():
	escala: Escala = Escala()
	escala.folgas()

def executar() -> None:
	
	validador = True
	dia_semana: tuple = ('segunda','terça','quarta','quinta','sexta','sabado')
	
	for validade in range(5):
		if os.path.isfile(dia_semana[validade]+'.txt'):
			validador = True
		else:
			validador = False
			break

	
	if os.path.isfile('operadores.txt'):
		if validador == True:
			while True:
				escala: Escala = Escala()

				try:
					escala.selecionar()
				except:
					pass

				if len(escala.imprimir()) == 6:
						
					for dia in range(6):
						print('===========================================')
						print(dia_semana[dia])
						print('===========================================')
						for caixa in range(13):
							print(f'{caixa+1} - {escala.imprimir()[dia][caixa+1]}')	
						
					break
		else:
			print('Complete a folga da semana')	
	else:
		print('Adicione funcionarios')

		

def imprimir_folgas() -> None:
	dia_semana: tuple = ('segunda','terça','quarta','quinta','sexta','sabado')
	data = input("Digite o dia da semana: ")
	if data in dia_semana:
		if os.path.isfile(data+'.txt'):
			with open(data+'.txt','r') as arquivo:
				print('===========================================')
				for linha in arquivo:
					print(linha[:-1:])
				print('===========================================')
			arquivo.close()
		else:
			print("Antes de consultar adcione a folga")
	else:
		print("Dia da semana invalido")

if __name__ == '__main__':
	main()
