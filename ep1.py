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

	
#pego o mesmo conjutnto de n questoes e vejo qual dos dois alunos vai melhor 100 vezes.
#o conjunto de provas onde o aluno5 for melhor entre 100 vezes é a escolhida.
def problema2_2(questoes, numero, aluno):

	melhor_conjunto_total = 0.0
	melhores_questoes = None

	for number in range(100000):
		questoes_sorteadas = sortear_questoes(questoes, numero)
		
		total_aluno5 = 0.0

		for number in range(100):
			nota = 0
			nota5 = 0
			
			for questao in questoes_sorteadas:
				acertou = random.uniform(0.0, 1.0)
				acertou5 = random.uniform(0.0, 1.0)

				if (TRI(aluno,questao)) > acertou:
					nota = nota + 1
				if (TRI(aluno5, questao)) > acertou5:
					nota5 = nota5 + 1	
		
			if nota5 > nota:
				total_aluno5 = total_aluno5 + 1
	
		if total_aluno5 > melhor_conjunto_total:
			melhor_conjunto_total = total_aluno5 
			melhores_questoes = questoes_sorteadas
			#print (total_aluno5)

	return (melhores_questoes)	


def melhores_questoes_pr(melhores_questoes):
	linha = ''
	for questao in melhores_questoes:
		string_pr = str(TRI(aluno5, questao))
		linha = linha + ' ' + string_pr

	print (linha)

def aux_2_2(questoes, numero):
	
	alunos = [aluno1, aluno2, aluno3, aluno4]
	resp_string = ''
	
	for aluno in alunos:
		
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

		resultado = str(resultado)

		resp_string = resp_string + ' ' + resultado
	
	return resp_string

def problema2_3():
	return


if __name__=='__main__':	
	a = ler_questoes()
	
	print ('10 questoes')
	pr_10 = problema2_2(a, 10, aluno4)
	melhores_questoes_pr(pr_10)
	print(aux_2_2(pr_10, 10))
	print ('-----------------------------')
	
	print ('20 questoes')
	pr_20 = problema2_2(a, 20, aluno4)
	melhores_questoes_pr(pr_20)
	print (aux_2_2(pr_20, 20))
	print ('-----------------------------')
	
	print ('50 questoes')
	pr_50 = problema2_2(a, 50, aluno4)
	print (aux_2_2(pr_50, 50))
	melhores_questoes_pr(pr_50)


	# print ('100 aluno1')
	# print (problema2_1(a, 100, aluno1))
	# print ('-------------')
	# print ('100 aluno2')
	# print (problema2_1(a, 100, aluno2))
	# print ('-------------')
	# print ('100 aluno3')
	# print (problema2_1(a, 100, aluno3))
	# print ('-------------')
	# print ('100 aluno4')
	# print (problema2_1(a, 100, aluno4))
	# print ('-------------')

