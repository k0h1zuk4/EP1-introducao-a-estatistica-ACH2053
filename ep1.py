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
	soma_total = 0

	for number in range(10000):
		questoes_sorteadas = sortear_questoes(questoes, numero)
		
		soma_das_pr_prova = 0

		for questao in questoes_sorteadas:
			soma_das_pr_prova = soma_das_pr_prova + TRI(aluno,questao)

		soma_total = soma_total + (soma_das_pr_prova / 20)	

	resultado = (soma_total / 10000)
	return resultado	

	

def problema2_2():
	return

def problema2_3():
	return


if __name__=='__main__':	
	a = ler_questoes()
	b = sortear_questoes(a, 4)
	print (problema2_1(a, 20, aluno5))