# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
import Rop, time, Direcao, random

smf = Semaphore(4)
rop = Rop.Rop(None)

class Babuino(Thread) :

    def __init__(self, position, time):

        Thread.__init__(self)
        self.position = position                            # posicao inicial do babuino
        self.time = time                                    # tempo
        self.arrived = False


    def atravessar(self):

        smf.acquire()
        if len(rop.rop) is 0:
            time.sleep(1)
            rop.rop.append(self)
            rop.direcao = self.position

        elif rop.direcao == self.position:
            time.sleep(1)
            rop.rop.append(self)



        for i in rop.rop:
            print(i.name)
        smf.release()
        # self.arrived = True

    def run(self):
        # ação executada pela thread

        # print("teste")
        lado = ["East", "West"]
        self.position = random.choice(lado)
        self.time = random.randint(1,8)

        time.sleep(self.time)

        if self.position == "East":
            Direcao.East.append(self)
            print("adicionou" + str(self) + "em East")
        else:
            Direcao.West.append(self)
            print("adicionou" + str(self) + "em West")

        self.atravessar()