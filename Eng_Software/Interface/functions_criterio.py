from Interface import Janela_1, Janela_3, janela_4, finish


def tabela_valor_ri(num_criterios):
    vetor_ri = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
    return vetor_ri[num_criterios - 1]

"""Essa função o usuário não sabe que existe
    Ler a matriz completa e retorna um vetor com os elementos  da matriz 
    na forma de decimal"""
def decimal():
    valores = []
    for i in range(len(Janela_3.criterio)):
        for j in range(len(Janela_3.criterio)):
            valores.append(Janela_3.ui.tableWidget.item(i, j).text())

    for i in range(len(valores)):
        if "/" in valores[i]:
            valores[i] = float(valores[i].split("/")[1])
        else:
            valores[i] = float(1 / int(valores[i]))

    print("valores decimais: ", valores)
    return valores


def soma_coluna(val):
    vetor = val
    soma = []
    aux = 0
    for i in range(len(Janela_3.criterio)):
        s = 0
        for j in range(len(Janela_3.criterio)):
            s += vetor[aux]
            aux += 1
        soma.append(s)
    print("soma colunas: ", soma)
    return soma


def normalizar_Matriz(soma, val):
    vetor = val
    div = 0
    normal = []
    for i in range(len(soma)):
        for j in range(len(Janela_3.criterio)):
            normal.append(vetor[div] / soma[i])
            div += 1

    print("matriz normal: ", normal)
    return normal


def vetor_eigen(normal):
    matriz = normal
    eigen = []
    for i in range(len(Janela_3.criterio)):
        s = 0
        aux = 0
        for j in range(len(Janela_3.criterio)):
            s += matriz[i + aux]
            aux += len(Janela_3.criterio)
        eigen.append(s / len(Janela_3.criterio))
    print("vetor de eigen: ", eigen)
    return eigen


def lambd(eigen, soma):
    lambda_v = 0
    soma_coluna = soma
    vet_eigen = eigen
    for i in range(len(Janela_3.criterio)):
        lambda_v += soma_coluna[i] * vet_eigen[i]
    print("lambda: ", lambda_v)
    return lambda_v


def ci(lambd):
    lambd_v = lambd
    ci = (lambd_v - len(Janela_3.criterio)) / (len(Janela_3.criterio) - 1)
    print("ci: ", ci)
    return ci


def cr(ci, ri):
    cr = ci / ri
    print("cr: ", cr)
    return cr

def close_multi_windows():
    janela_4.MainWindow.close()
    Janela_3.MainWindow.close()
    finish.MainWindow.close()

"""Ordem de captura dos valores: pega os valores da linha que satisfaz a condição
        Padroniza os valores e add em um vetor para completar a matriz"""
def capturar_Valor_Matriz():
    valores = []
    for i in range(len(Janela_3.criterio)):
        for j in range(len(Janela_3.criterio)):
            if i > j:
                valores.append(Janela_3.ui.tableWidget.item(i, j).text())

    for i in range(len(valores)):
        if "/" in valores[i]:
            valores[i] = valores[i].split("/")[1]
        elif "1" in valores[i]:
            valores[i] = valores[i]
        else:
            valores[i] = "1/" + valores[i]

    print("valores:", valores)
    return valores