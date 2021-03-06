#python3
import os
import argparse
import sys
from os import system as system_call 
import random
import math
import numpy as np
import scipy as sp
import scipy.stats

aluno1 = -1.0
aluno2 = -0.5
aluno3 = 0.0
aluno4 = 0.5
aluno5 = 1.0

# PARTE II
# para cada quetão vou rodar a distribuição de probabilidades, considerando erro ou acerto.
# Fazer o prodtória das probabilidades de todas as perguntas para cada Teta.
# Ver qual teta gerou a maior probebilidade de ter gerado aquele conjunto de questões

dir_path = os.path.dirname(os.path.realpath(__file__))

class Questao():
    a = 0.0
    b = 0.0
    index = 0
    diff = None

    def __init__(self, a ,b, index):
        self.a = a
        self.b = b
        self.index = index

    def add_diff(self, diff):
        self.diff = diff

def sortear_questoes(questoes, numero):
    questoes_sorteadas = random.sample(questoes, numero)
    return questoes_sorteadas


def ler_questoes():	
    questoes = []
    with open(dir_path + '/dados/questoes' + ".txt", 'r') as f:
        index = 0
        data = f.readlines()
        for registro in data:
            a, b = registro.split(' ')
            a = float(a)
            b = float(b)
            questao_atual = Questao(a, b, index)
            questoes.append(questao_atual)
            index = index + 1
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

            if (TRI(aluno,questao)) >= acertou:
                nota = nota + 1
            if (TRI(aluno5, questao)) >= acertou5:
                nota5 = nota5 + 1

        if nota > nota5:
            total_aluno = total_aluno + 1

    print(total_aluno)
    return (float(100000 - total_aluno) / 100000)


#pego o mesmo conjutnto de n questoes e vejo qual dos dois alunos vai melhor 100 vezes.
#o conjunto de provas onde o aluno5 for melhor entre 1000 vezes e a escolhida.
def problema2_2(questoes, numero, aluno):

    melhor_conjunto_total = 0.0
    melhores_questoes = None
    melhores_questoes_index = []

    for number in range(100000):
        questoes_sorteadas = sortear_questoes(questoes, numero)

        total_aluno5 = 0.0

        for number in range(1):
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
        #string_pr = str(TRI(aluno5, questao))
        linha = linha + ' ' + str(questao.index)

    print (linha)

def aux_2_2(questoes):

    alunos = [aluno1, aluno2, aluno3, aluno4]
    resp_string = ''

    for aluno in alunos:

        total_aluno = 0

        for number in range(100000):

            nota = 0
            nota5 = 0

            for questao in questoes:
                acertou = random.uniform(0.0, 1.0)
                acertou5 = random.uniform(0.0, 1.0)

                if (TRI(aluno, questao)) >= acertou:
                    nota = nota + 1
                if (TRI(aluno5, questao)) >= acertou5:
                    nota5 = nota5 + 1

            if nota > nota5:
                total_aluno = total_aluno + 1

        pr = (float(100000 - total_aluno)/100000)

        resp_string = resp_string + ' ' + str(pr)


    print(resp_string)
    return

def intervalo_confianca(data, confidence=0.90):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m-h, m+h

def calculando_melhores_questoes(questoes, quantas):

    for questao in questoes:
        TRI_4 = TRI(aluno4, questao)
        TRI_5 = TRI(aluno5, questao)

        diff = TRI_5 - TRI_4

        questao.add_diff(diff)

    questoes.sort(key=lambda x: x.diff, reverse = True)

    top_questoes = []
    count = 0
    for questao in questoes:
        if count < quantas:
            top_questoes.append(questao)
            count = count + 1
        else:
            break

    return top_questoes


def print_top_questoes(top_questoes):
        indexes = ''
        for questao in top_questoes:
            indexes = indexes + ' ' + str(questao.index)

        print(indexes)

def problema2_3(questoes):
    alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

    index10 = [92, 74, 78, 80, 32, 65, 86, 81, 34, 66]
    index20 = [82, 19, 53, 11, 51, 37, 66, 27, 87, 71, 9, 85, 28, 95, 39, 92, 90, 1, 3, 70]
    index50 = [84, 43, 60, 51, 77, 23, 93, 80, 36, 22, 71, 59, 1, 34, 16, 2, 17, 87, 66, 29, 0, 72, 68, 54, 90, 56, 76, 35, 97, 10, 40, 26, 44, 75, 83, 86, 53, 94, 37, 92, 30, 27, 7, 61, 73, 98, 63, 4, 42, 15]

    questoes10 = []
    questoes20 = []
    questoes50 = []

    for questao in questoes:
        for crr_index in index10:
            if questao.index == crr_index:
                questoes10.append(questao)
        for crr_index in index20:
            if questao.index == crr_index:
                questoes20.append(questao)
        for crr_index in index50:
            if questao.index == crr_index:
                questoes50.append(questao)

    for aluno in alunos:
        print(aluno, '-------------------')
        nota_10 = []
        nota_20 = []
        nota_50 = []
        nota_100 = []

        for number in range(10000):
            nota10 = 0
            nota20 = 0
            nota50 = 0
            nota100 = 0

            for questao in questoes10:
                acertou = random.uniform(0.0, 1.0)

                if (TRI(aluno, questao)) > acertou:
                    nota10 = nota10 + 1

            nota_10.append(nota10)

            for questao in questoes20:
                acertou = random.uniform(0.0, 1.0)

                if (TRI(aluno, questao)) > acertou:
                    nota20 = nota20 + 1

            nota_20.append(nota20)

            for questao in questoes50:
                acertou = random.uniform(0.0, 1.0)

                if (TRI(aluno, questao)) > acertou:
                    nota50 = nota50 + 1

            nota_50.append(nota50)

            for questao in questoes:
                acertou = random.uniform(0.0, 1.0)

                if (TRI(aluno, questao)) > acertou:
                    nota100 = nota100 + 1

            nota_100.append(nota100)

        print(intervalo_confianca(nota_10))
        print(intervalo_confianca(nota_20))
        print(intervalo_confianca(nota_50))
        print(intervalo_confianca(nota_100))

# PARTE II
# para cada quetão vou rodar a distribuição de probabilidades, considerando erro ou acerto.
# Fazer o prodtória das probabilidades de todas as perguntas para cada Teta.
# Ver qual teta gerou a maior probebilidade de ter gerado aquele conjunto de questões

class Aluno():
    respostas = None
    index = None

    def __init__(self, respostas, index):
        self.respostas = respostas
        self.index = index

def ler_respostas():	
    alunos = []
    with open(dir_path + '/dados/respostas' + ".txt", 'r') as f:
        index = 0
        lines = f.readlines()
        
        for i in range(2000):
            result = []
            for line in lines:
                line.rstrip("\n\r")
                value = int(line.split(' ')[i])
                result.append(value)
            aluno = Aluno(result, i)
            alunos.append(aluno)
    
    return alunos

min = -20
max = 20

tetas = [round(x*0.1, 2) for x in range(10*min, 10*max+1)]

class TetaRespostas():
    valor_do_teta = None
    probabilidade = None

    def __init__(self, valor_do_teta, probabilidade):
        self.valor_do_teta = valor_do_teta
        self.probabilidade = probabilidade

def para_cada_aluno_gerar_lista_de_prob(questoes, aluno):
    tetas_e_probabilidades = []

    for teta in tetas :
        probs = []
        for questao in questoes:
            
            if aluno.respostas[questao.index] == 0:
                prob_for_question = 1 - TRI(teta, questao)
            else:
                prob_for_question = TRI(teta, questao)
            
            probs.append(prob_for_question)
        prob = 1
        for x in probs:
            prob = prob * x

        tetas_e_probabilidades.append(TetaRespostas(teta, prob))

    tetas_e_probabilidades.sort(key=lambda x: x.probabilidade, reverse = True)

    count = 0
    for teta_e_probabilidade in tetas_e_probabilidades:
        if count < 1:
            print(teta_e_probabilidade.valor_do_teta)
            count = count + 1
        else:
            break

# 2_2
# para cada prova de tamanho N previamente selecionadas: 
# simular a execução da prova novamente
# nota utilizando TRI -> Para aquele conjunto de respostas/perguntas/theta temos uma probabilidade, verificar qual tem a maior?
#
#
#

def nota_utilizando_TRI(questoes, respostas, teta):
    tetas_e_probabilidades = []

    probs = []
    count = 0
    for questao in questoes:
        if respostas[count] == 0:
            prob_for_question = 1 - TRI(teta, questao)
        else:
            prob_for_question = TRI(teta, questao)

        probs.append(prob_for_question)

        count += 1
    prob = 1
    for x in probs:
        prob = prob * x

    return prob

def parte2_2(questoes):

    alunos = [aluno1, aluno2, aluno3, aluno4]
    resp_string = ''
    notas_alunos = []
    count_aluno = 0
    for aluno in alunos:

        total_aluno = 0
        notas_aluno = []
        notas_aluno5 = []

        for number in range(100000):

            nota = 0
            nota5 = 0
            
            respostas = []
            respostas5 = []

            for questao in questoes:
                acertou = random.uniform(0.0, 1.0)
                acertou5 = random.uniform(0.0, 1.0)
                
                if (TRI(aluno, questao)) >= acertou:
                    respostas.append(1)
                if (TRI(aluno, questao)) < acertou:
                    respostas.append(0)
                if (TRI(aluno5, questao)) >= acertou5:
                    respostas5.append(1)
                if (TRI(aluno5, questao)) < acertou5:
                    respostas5.append(0)
            
            nota = nota_utilizando_TRI(questoes, respostas, aluno) 
            nota5 = nota_utilizando_TRI(questoes, respostas5, aluno5)
            
            if nota > nota5:
                total_aluno = total_aluno + 1
            
            notas_aluno.append(nota)
            if count_aluno == 3:
                notas_aluno5.append(nota5)
        
        notas_alunos.append(notas_aluno)

        if count_aluno == 3:
            notas_alunos.append(notas_aluno5)

        pr = (float(100000 - total_aluno)/100000)

        resp_string = resp_string + ' ' + str(pr)

        count_aluno += 1

    print(resp_string)
    return notas_alunos

def notas_alunos_acertos(questoes):

    alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
    resp_string = ''
    notas_alunos = []

    for aluno in alunos:

        total_aluno = 0
        notas_aluno = []

        for number in range(100000):

            nota = 0

            for questao in questoes:
                acertou = random.uniform(0.0, 1.0)

                if (TRI(aluno, questao)) >= acertou:
                    nota = nota + 1
            
            notas_aluno.append(nota)
    
        notas_alunos.append(notas_aluno)

    return notas_alunos

def intervalo_confianca_normal(data, confidence=0.90):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    print (m-h, m+h)
    return m-h, m+h

def run_interval_for_questions(notas_alunos):
    response = ''
    print(len(notas_alunos))
    for notas_aluno in notas_alunos:
        print(len(notas_aluno))
        i, f = intervalo_confianca_normal(notas_aluno)
        reponse = response + ' ' + str(i) + ' ' + str(f)

    print (response)

if __name__=='__main__':	
    a = ler_questoes()
    
    # #PARTE2_1
    # alunos = ler_respostas()
    # for aluno in alunos:
    #     para_cada_aluno_gerar_lista_de_prob(a, aluno)

    #PARTE2_2
    # top_questoes_10 = calculando_melhores_questoes(a, 10)
    # notas_alunos_TRI_10 = parte2_2(top_questoes_10)
    # notas_alunos_normal_10 = notas_alunos_acertos(top_questoes_10)
    # run_interval_for_questions(notas_alunos_TRI_10)
    # run_interval_for_questions(notas_alunos_normal_10)
    
    
    # top_questoes_20 = calculando_melhores_questoes(a, 20)
    # notas_alunos_TRI_20 = parte2_2(top_questoes_20)
    # notas_alunos_normal_20 = notas_alunos_acertos(top_questoes_20)
    # run_interval_for_questions(notas_alunos_TRI_20)
    # run_interval_for_questions(notas_alunos_normal_20)
    
    
    # top_questoes_50 = calculando_melhores_questoes(a, 50)
    # notas_alunos_TRI_50 = parte2_2(top_questoes_50)
    # notas_alunos_normal_50 = notas_alunos_acertos(top_questoes_50)
    # run_interval_for_questions(notas_alunos_TRI_50)
    # run_interval_for_questions(notas_alunos_normal_50)


    notas_alunos_TRI_100 = parte2_2(a)
    notas_alunos_normal_100 = notas_alunos_acertos(a)
    run_interval_for_questions(notas_alunos_TRI_100)
    run_interval_for_questions(notas_alunos_normal_100)


    #PARTE2_3




    #2_3
    #problema2_3(a)

    # top_questoes_10 = calculando_melhores_questoes(a, 10)
    # print_top_questoes(top_questoes_10)
    # aux_2_2(top_questoes_10)
    #
    #
    # top_questoes_20 = calculando_melhores_questoes(a, 20)
    # print_top_questoes(top_questoes_20)
    # aux_2_2(top_questoes_20)
    #
    #
    # top_questoes_50 = calculando_melhores_questoes(a, 50)
    # print_top_questoes(top_questoes_50)
    # aux_2_2(top_questoes_50)

    # #2_2
    # print ('10 questoes')
    # pr_10 = problema2_2(a, 10, aluno4)
    # melhores_questoes_pr(pr_10)
    # print(aux_2_2(pr_10))
    # print ('-----------------------------')

    # print ('20 questoes')
    # pr_20 = problema2_2(a, 20, aluno4)
    # melhores_questoes_pr(pr_20)
    # print (aux_2_2(pr_20))
    # print ('-----------------------------')

    # print ('50 questoes')
    # pr_50 = problema2_2(a, 50, aluno4)
    # print (aux_2_2(pr_50))
    # melhores_questoes_pr(pr_50)

    #2_1
    # print ('10 aluno1')
    # print (problema2_1(a, 10, aluno1))
    # print ('-------------')
    # print ('10 aluno2')
    # print (problema2_1(a, 10, aluno2))
    # print ('-------------')
    # print ('10 aluno3')
    # print (problema2_1(a, 10, aluno3))
    # print ('-------------')
    # print ('10 aluno4')
    # print (problema2_1(a, 10, aluno4))
    # print ('-------------')

    # print ('20 aluno1')
    # print (problema2_1(a, 20, aluno1))
    # print ('-------------')
    # print ('20 aluno2')
    # print (problema2_1(a, 20, aluno2))
    # print ('-------------')
    # print ('20 aluno3')
    # print (problema2_1(a, 20, aluno3))
    # print ('-------------')
    # print ('20 aluno4')
    # print (problema2_1(a, 20, aluno4))
    # print ('-------------')

    # print ('50 aluno1')
    # print (problema2_1(a, 50, aluno1))
    # print ('-------------')
    # print ('50 aluno2')
    # print (problema2_1(a, 50, aluno2))
    # print ('-------------')
    # print ('50 aluno3')
    # print (problema2_1(a, 50, aluno3))
    # print ('-------------')
    # print ('50 aluno4')
    # print (problema2_1(a, 50, aluno4))
    # print ('-------------')


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
