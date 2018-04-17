# -*- coding: utf-8 -*-

from Babuino import Babuino
from threading import Thread
from collections import deque
import time
import Direcao

# babuino = Babuino(None, None)
#
# babuino.lucky_side()
# babuino.lucky_time()
# babuino.create_thread()

# print(babuino.initial_pos)
# print(babuino.time)
# a.join()

def create_babuino():
    field = []
    while not len(field) == 10:                                 # cria 50 babuinos
        # name = "babuino"+str(count)
        # time.sleep(1)
        babuino = Babuino(None, None)
        field.append(babuino)
        # continue

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
        i.join()
        print(str(i.name)+ " " + str(i.position) + " " + str(i.time))
    # tEast = Thread(target=go_east, args=(campo,))
    # tWest = Thread(target=go_west, args=(campo,))
    #
    # tEast.start()
    # tWest.start()
    # tEast.join()
    # tWest.join()

if __name__ == '__main__':

    main()