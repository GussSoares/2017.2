from Interface import Janela_1, Janela_3, janela_4, finish
from PyQt5 import QtCore, QtGui, QtWidgets

def tabela_valor_ri(num_criterios):
    vetor_ri = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
    return vetor_ri[num_criterios - 1]

"""Essa função o usuário não sabe que existe
    Ler a matriz completa e retorna um vetor com os elementos  da matriz 
    na forma de decimal"""
def decimal():
    valores = []
    for t in range(len(Janela_3.criterio)):
        print("MATRIZ do ", t)
        matriz = janela_4.ui.tabWidget.findChild(QtCore.QObject, "tableWidget_" + str(t))
        for i in range(len(Janela_3.atividade)):
            for j in range(len(Janela_3.atividade)):
                valores.append(matriz.item(i, j).text())

    for i in range(len(valores)):
        if "/" in valores[i]:
            valores[i] = float(valores[i].split("/")[1])
        else:
            valores[i] = float( 1 /int(valores[i]))

    print("valores decimais: ", valores)
    return valores

"""Soma os elementos de cada coluna de todas as matrizes de atividade"""
def soma_coluna(val):
    vetor = val
    soma = []
    aux = 0
    for t in range(len(Janela_3.criterio)):
        print("MATRIZ do ", t)
        for i in range(len(Janela_3.atividade)):
            s = 0
            for j in range(len(Janela_3.atividade)):
                s += vetor[aux]
                aux += 1
            soma.append(s)
    print("soma colunas: ", soma)
    return soma


def normalizar_Matriz(soma, val):
    vetor = val
    normal = []
    div = 0
    print("MATRIZ normalizada ")
    for i in range(len(soma)):
        for j in range(len(Janela_3.atividade)):
            normal.append(vetor[div] / soma[i])
            div += 1

    print("matriz normal: ", normal)
    return normal

def vetor_eigen(normal):
    matriz = normal
    eigen = []
    aux2 = 0
    for t in range(len(Janela_3.criterio)):
        print("MATRIZ do ", t)
        for i in range(len(Janela_3.atividade)):
            s = 0
            aux = 0
            for j in range(len(Janela_3.atividade)):
                s += matriz[i + aux + aux2]
                aux += len(Janela_3.atividade)
            eigen.append(s / len(Janela_3.atividade))
        aux2 += len(Janela_3.atividade ) *len(Janela_3.atividade)
    print("vetor de eigen: ", eigen)
    return eigen


def lambd(eigen, soma):
    soma_coluna = soma
    vet_eigen = eigen
    vetor_result = []
    aux = 0
    for t in range(len(Janela_3.criterio)):
        print("MATRIZ do ", t)
        lambda_v = 0
        for i in range(len(Janela_3.atividade)):
            lambda_v += soma_coluna[ i +aux ] *vet_eigen[ i +aux]
        vetor_result.append(lambda_v)
        aux += len(Janela_3.atividade)
    print("lambda: ", vetor_result)
    return vetor_result

def ci(lambd):
    lambd_v = lambd
    vetor_result = []
    for t in range(len(Janela_3.criterio)):
        print("MATRIZ do ", t)
        ci = (lambd_v[t] - len(Janela_3.atividade)) / (len(Janela_3.atividade) -1)
        vetor_result.append(ci)
    print("ci: ", vetor_result)
    return vetor_result

def cr(ci, ri):
    vetor_ci = ci
    valor_ri = ri
    vetor_result = []
    for t in range(len(Janela_3.criterio)):
        print("MATRIZ do " ,t)
        cr = vetor_ci[t ] /valor_ri
        vetor_result.append(cr)
    print("cr: ", vetor_result)
    return vetor_result

"""Ordem de captura dos valores: pega os valores da linha que satisfaz a condição.
        Padroniza os valores e adiciona em um vetor para completar a matriz"""
def capturar_Valor_Matriz():
    valores = []
    for t in range(len(Janela_3.criterio)):
        print("MATRIZ do ", t)
        matriz = janela_4.ui.tabWidget.findChild(QtCore.QObject, "tableWidget_" + str(t))
        for i in range(len(Janela_3.atividade)):
            for j in range(len(Janela_3.atividade)):
                if i > j:
                    valores.append(matriz.item(i, j).text())

    for i in range(len(valores)):
        if "/" in valores[i]:
            valores[i] = valores[i].split("/")[1]
        elif "1" in valores[i]:
            valores[i] = valores[i]
        else:
            valores[i] = "1/" + valores[i]

    return valores