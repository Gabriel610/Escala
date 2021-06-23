#Programa criado em 26 de maio de 2021 as 00:25 por Gabriel dos Santos de Luna Silva
from random import choice
import os.path


class Escala(object):
	
	def __init__(self: object) -> None:
		self.__caixas: list = []
		self.__operadores: list = []
		self.__dia: dict = {}
		self.__semana: list = []
		

	@property
	def dia(self: object) -> list:
		return self.__dia

	@property
	def operadores(self: object) -> list:
		return self.__operadores

	@property
	def caixas(self: object) -> int:
		return self.__caixas
	
	@property
	def semana(self: object) -> list:
		return self.__semana

	@property
	def em_pe(self: object) -> list:
		return self.__em_pe
	
	
	
	def add_operadores(self: object) -> None:
		
		with open('operadores.txt','w') as arquivo:
			numero = 0
			while True:
				numero += 1
				nome: str = input(f'Digite o nome do funcionario {numero}:')
				
				if nome == 'sair':
					break
				else:
					arquivo.write(nome+'\n')
			arquivo.close()


	def folgas(self: object) -> None:

		if os.path.isfile('operadores.txt'):
			dia_semana = ('segunda','terça','quarta','quinta','sexta','sabado')
			add_dia_semana = input("qual é o dia da semana? ")
			if add_dia_semana in dia_semana:
				with open(add_dia_semana+'.txt','w') as arq:
					numero = 0
					while True:
						
						numero += 1
						nome: str = input(f'Digite o nome do funcionario {numero} de folga na  {add_dia_semana}:')
						
						if nome == 'sair':
							break
						elif nome+'\n' in open('operadores.txt','r'):
							arq.write(nome+'\n')
						else:
							print('nome invalido')
							
				arq.close()
				
		else:
			print("adicione operadores")


	def selecionar(self: object) -> None:
		
		dias_semana = ('segunda','terça','quarta','quinta','sexta','sabado')
		validador: bool = True
		verificador = 0
		verificardor2 = 0
		lista = []
		while True:
			
			with open('operadores.txt','r') as arquivo:
				for linha in arquivo:
					self.__operadores.append(linha[:-1:])
				arquivo.close()
			
			if os.path.isfile(dias_semana[len(self.__semana)]+'.txt'):
				with open(dias_semana[len(self.__semana)]+'.txt','r') as arqui:
					for linha in arqui:
						self.__operadores.remove(linha[:-1:])
				arqui.close()
			
			if len(self.__operadores) > 13:
				while True:
					em_pe = choice(self.__operadores)
					self.__operadores.remove(em_pe)
					if len(self.__operadores) == 13:
						break
			
			self.__dia = {caixa+1:" " for caixa in range(13)}

			self.__caixas = [caixa+1 for caixa in range(13)]

			while True:
				
				nome: str = choice(self.__operadores)
				caixa: int = choice(self.__caixas)
			
				if len(self.__semana) > 0:
					
					for dia in range(len(self.__semana)):
						if self.__semana[dia][caixa] == nome:	
							validador = False
							break
						if caixa == 11:
							if self.__semana[dia][11] == nome:	
								validador = False
								break
							elif self.__semana[dia][12] == nome:	
								validador = False
								break
							elif self.__semana[dia][13] == nome:	
								validador = False
								break
						elif caixa == 12:
							if self.__semana[dia][11] == nome:	
								validador = False
								break
							elif self.__semana[dia][12] == nome:	
								validador = False
								break
							elif self.__semana[dia][13] == nome:	
								validador = False
								break
						elif caixa == 13:
							if self.__semana[dia][11] == nome:	
								validador = False
								break
							elif self.__semana[dia][12] == nome:	
								validador = False
								break
							elif self.__semana[dia][13] == nome:	
								validador = False
								break
						else:
							validador = True

				if validador == True:
					self.__dia[caixa] = nome
					self.__operadores.remove(nome)
					self.__caixas.remove(caixa)
					verificador = 0
				else:
					verificador += 1

				if verificador > 10:
					self.__operadores.clear()
					verificador2 += 1
					break

				if len(self.__operadores) == 0:
					self.__semana.append(self.__dia)
					break
				
			if verificador == 10:
				self.__semana.clear()

			if len(self.__semana) == 6:
				break


	def imprimir(self: object) -> list:
		return self.__semana

	