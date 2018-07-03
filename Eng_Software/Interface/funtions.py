def decimal(self):
    valores = []
    for i in range(len(criterio)):
        for j in range(len(criterio)):
            valores.append(self.tableWidget.item(i, j).text())

    for i in range(len(valores)):
        if "/" in valores[i]:
            valores[i] = float(valores[i].split("/")[1])
        else:
            valores[i] = float(1 / int(valores[i]))

    print("valores decimais: ", valores)
    return valores


def soma_coluna(self, val):
    vetor = val
    soma = []
    aux = 0
    for i in range(len(criterio)):
        s = 0
        for j in range(len(criterio)):
            s += vetor[aux]
            aux += 1
        soma.append(s)
    print("soma colunas: ", soma)
    return soma


def normalizar_Matriz(self, soma, val):
    vetor = val
    div = 0
    normal = []
    for i in range(len(soma)):
        for j in range(len(criterio)):
            normal.append(vetor[div] / soma[i])
            div += 1

    print("matriz normal: ", normal)
    return normal


def vetor_eigen(self, normal):
    matriz = normal
    eigen = []
    for i in range(len(criterio)):
        s = 0
        aux = 0
        for j in range(len(criterio)):
            s += matriz[i + aux]
            aux += len(criterio)
        eigen.append(s / len(criterio))
    print("vetor de eigen: ", eigen)
    return eigen


def lambd(self, eigen, soma):
    lambda_v = 0
    soma_coluna = soma
    vet_eigen = eigen
    for i in range(len(criterio)):
        lambda_v += soma_coluna[i] * vet_eigen[i]
    print("lambda: ", lambda_v)
    return lambda_v


def ci(self, lambd):
    lambd_v = lambd
    ci = (lambd_v - len(criterio)) / (len(criterio) - 1)
    print("ci: ", ci)
    return ci


def cr(self, ci, ri):
    cr = ci / ri
    print("cr: ", cr)
    return cr