criterios = []
mat = []

def matriz(qtd_criterios, matriz):
    for i in range(1, qtd_criterios+1):
        linhas = []
        for j in range(1, qtd_criterios+1):
            linhas.append(criterios[j-1])
        mat.append(linhas)
    return mat

if __name__ == "__main__":

    objective = input("diga seu objetivo: ")
    qtd_criterios = input("Quantos criterios: ")

    for i in range(int(qtd_criterios)):
        criterios.append(input())

    print(matriz(int(qtd_criterios), mat))
