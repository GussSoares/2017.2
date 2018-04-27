# -*- coding: utf-8 -*-

from Babuino import Babuino
import time, random, Vetores


count_east = 0
count_west = 0

def create_babuino():
    field = []
    direcao = ["East", "West"]
    while not len(field) == 50:                                 # cria 50 babuinos

        babuino = Babuino(None, None)
        field.append(babuino)
        babuino.time = random.randint(1, 8)
        babuino.position = random.choice(direcao)
        # if field.count(babuino.position):
        #     babuino.position = "East"
        # else:
        #     babuino.position = "West"
    return field                                                        # retorna um vetor de babuinos

# def chegada_ao_canyon(list):
#
#     for i in list:
#         if str(i.position) == "East":
#
#             pre_east.append(i)
#         else:
#             pre_west.append(i)

# def go_east(list):                                                      # manda os babuinos para o Leste
#     Direcao.lock = True
#     for i in list:
#         if (len(Direcao.East) == 0) and (i.position == "East"):         # se é o primeiro babuino, so adiciona
#             print("adicionou" + str(i) + "em East")
#             Direcao.East.append(i)
#
#         elif len(Direcao.East) == 5:                                    # se encher, espera ate surgir vaga
#             while len(Direcao.East) == 5:
#                 print("entrou while East")
#                 # time.sleep(1)
#                 pass
#         else:
#             if str(i.position) == "East":                               # adiciona ao Leste junto com o tempo
#                 time.sleep(i.time)
#                 print("adicionou"+str(i)+"em East")
#                 Direcao.East.append(i)
#     Direcao.lock = False
#
# def go_west(list):                                                      # manda os babuinos para o Oeste
#     Direcao.lock = True
#     for i in list:
#         if (len(Direcao.West) == 0) and (i.position == "West"):         # se é o primeiro babuino, so adiciona
#             print("adicionou" + str(i) + "em West")
#             Direcao.West.append(i)
#
#         elif len(Direcao.West) == 5:                                    # se encher, espera até surgir vaga
#             while len(Direcao.West) == 5:
#                 print("entrou while West")
#                 time.sleep(1)
#                 pass
#         else:
#             if str(i.position) == "West":                               # adiciona ao Oeste junto com o tempo
#                 time.sleep(i.time)
#                 print("adicionou"+str(i)+"em West")
#                 Direcao.West.append(i)
#     Direcao.lock = False
#

def main():
    global count_west, count_east
    campo = create_babuino()                                            # cria 50 babuinos
    # print("Campo inicial: " + str(len(field)))

    # for i in range(len(field)):
    #     if field[i].position == "East":
    #         East.append(field[i])
    #     else:
    #         West.append(field[i])

    # for i in range(len(field)):
    #     field.pop()

    # print("POSICIONAMENTO")
    # print("Campo inicial: " + str(len(field)))
    # print("Leste: " + str(len(East)))

    # for i in East:
    #     print(str(i.position) + " " + str(i.time))
    #
    # print("Oeste: " + str(len(West)))
    #
    # for i in West:
    #     print(str(i.position) + " " + str(i.time))
    for i in campo:                                                     # inicializa os babuinos
        i.start()
        print(str(i.name) + " " + str(i.position) + " " + str(i.time))

    for i in campo:
        i.join()
        if i.position == "East":
            count_east += 1
        else:
            count_west += 1

    # for i in campo:
    #     i.join()

    # for i in campo:                                                     # contar quantos babuinos existe em cada lado
    #     if i.position == "East":
    #         count_east += 1
    #     else:
    #         count_west += 1
    # tEast = Thread(target=go_east, args=(campo,))
    # tWest = Thread(target=go_west, args=(campo,))
    #
    # tEast.start()
    # tWest.start()
    # tEast.join()
    # tWest.join()

if __name__ == '__main__':

    tempo = 0
    tempo_corda = 0
    inicio = time.time()
    main()
    fim = time.time()

    for i in Vetores.crossing_time:
        print("Tempo individual de travessia: " + str(i))
        tempo += i

    for i in Vetores.rop_time:
        tempo_corda += i
        print(i)

    # relatorio()
    print("\n\n*****************************")
    print("Relatório")
    print("Quantidade de Babuinos")
    print("Leste: " + str(count_east))
    print("Oeste: " + str(count_west))
    print("Tempo de execução: "+ str(fim-inicio) + " segundos")
    print("Tempo da corda: " + str(tempo_corda) + " segundos")

    # tempo = soma dos tempos que cada babuino passa na corda
    print("Tempo médio de travessia: " + str(tempo/50) + " segundos")
    aproveitamento = tempo_corda/(fim-inicio)
    print("Taxa de aproveitamento da corda: " + str(aproveitamento) + " ou " + str(aproveitamento*100) + "%")
    #tempo de uso da corda / tempo de execucao