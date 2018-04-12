# -*- coding: utf-8 -*-

from Babuino import Babuino
from threading import Thread
from collections import deque
import time

East = deque(maxlen=5)
West = deque(maxlen=5)
Rop = deque(maxlen=4)
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
    while not len(field) == 50:
        # name = "babuino"+str(count)
        babuino = Babuino(None, None)
        field.append(babuino)
        # continue

    return field

# def chegada_ao_canyon(list):
#
#     for i in list:
#         if str(i.position) == "East":
#
#             pre_east.append(i)
#         else:
#             pre_west.append(i)

def go_east(list):
    # time.sleep(1)                               # para deixar o proximo thread ser executado
    for i in list:
        if (len(East) == 0) and (i.position == "East"):
            print("adicionou" + str(i) + "em East")
            East.append(i)

        elif len(East) == 5:
            while len(East) == 5:
                print("entrou while East")
                time.sleep(1)
                pass
        else:
            if str(i.position) == "East":
                time.sleep(i.time)
                print("adicionou"+str(i)+"em East")
                East.append(i)

def go_west(list):
    for i in list:
        if (len(West) == 0) and (i.position == "West"):
            print("adicionou" + str(i) + "em West")
            West.append(i)

        elif len(West) == 5:
            while len(West) == 5:
                print("entrou while West")
                time.sleep(1)
                pass
        else:
            if str(i.position) == "West":
                time.sleep(i.time)
                print("adicionou"+str(i)+"em West")
                West.append(i)

def main():

    campo = create_babuino()
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
    for i in campo:
        i.start()
        print(i)

    tEast = Thread(target=go_east, args=(campo,))
    tWest = Thread(target=go_west, args=(campo,))

    tEast.start()
    tWest.start()
    # tEast.join()
    # tWest.join()

# print(East[0].position)
if __name__ == '__main__':

    main()