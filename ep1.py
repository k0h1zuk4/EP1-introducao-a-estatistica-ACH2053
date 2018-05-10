import os
import argparse
import sys
from os import system as system_call 
import random
import math

aluno1 = -1.0
aluno2 = -0.5
aluno3 = 0.0
aluno4 = 0.5
aluno5 = 1.0

dir_path = os.path.dirname(os.path.realpath(__file__))


class Questao():
	a = 0.0
	b = 0.0
	
	def __init__(self, a ,b):
		self.a = a
		self.b = b


def sortear_questoes(questoes, numero):
	questoes_sorteadas = random.sample(questoes, numero)
	return questoes_sorteadas


def ler_questoes():	
	questoes = []
	with open(dir_path + '/dados/questoes' + ".txt", 'r') as f:
		data = f.readlines()
		for registro in data:
			a, b = registro.split(' ')
			a = float(a)
			b = float(b)
			questao_atual = Questao(a, b)
			questoes.append(questao_atual)
	return questoes


def TRI(aluno, questao):
	valor = math.exp(questao.a*(aluno - questao.b))
	pr = valor / (1 + valor)
	return pr


def problema2_1(questoes, numero, aluno):
	total_aluno = 0

	for number in range(100000):
		questoes_sorteadas = sortear_questoes(questoes, numero)
		
		nota = 0
		nota5 = 0

		for questao in questoes_sorteadas:
			acertou = random.uniform(0.0, 1.0)
			acertou5 = random.uniform(0.0, 1.0)

			if (TRI(aluno,questao)) > acertou:
				nota = nota + 1
			if (TRI(aluno5, questao)) > acertou5:
				nota5 = nota5 + 1	
		
		if nota > nota5:
			total_aluno = total_aluno + 1
	
	resultado = (100000 - total_aluno) / 100000

	return resultado	

	

def problema2_2():
	return

def problema2_3():
	return


if __name__=='__main__':	
	a = ler_questoes()
	b = sortear_questoes(a, 4)
	print (problema2_1(a, 20, aluno3))