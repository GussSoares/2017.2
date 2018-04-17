# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
import Rop, time, Direcao, random, sys

smf = Semaphore(value=4)
rop = Rop.Rop(None)

class Babuino(Thread) :

    def __init__(self, position, time):

        Thread.__init__(self)
        self.position = position                            # posicao inicial do babuino
        self.time = time                                    # tempo
        self.arrived = False


    def atravessar(self):

        if len(rop.rop) is 0:
            smf.acquire()
            time.sleep(1)
            rop.rop.append(self)
            rop.direcao = self.position
            for i in rop.rop:
                sys.stdout.write(str(i.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
                sys.stdout.flush()
            time.sleep(4)
            rop.rop.popleft()

            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()

            # print(str(self.name) + " saiu da corda")
            smf.release()

        elif rop.direcao == self.position:
            smf.acquire()
            time.sleep(1)
            rop.rop.append(self)
            for i in rop.rop:
                sys.stdout.write(str(i.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
                # print(str(i.name) + " entrou na corda pela " + str(rop.direcao))
                sys.stdout.flush()
            time.sleep(4)
            rop.rop.popleft()
            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()
            # print(str(self.name) + " saiu da corda")
            smf.release()

        else:
            pass


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