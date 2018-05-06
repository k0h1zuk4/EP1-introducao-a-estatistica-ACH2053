import os
import argparse
import sys
from os import system as system_call 
import random

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
			questao_atual = Questao(a, b)
			questoes.append(questao_atual)
	return questoes

def TRI(aluno, question):
	return

def exponencial(valor):
	return


def problema2_1():
	return

def problema2_2():
	return

def problema2_3():
	return


if __name__=='__main__':	
	a = ler_questoes()
	b = sortear_questoes(a, 2)
