# -*- coding: utf-8 -*-

from threading import Thread, BoundedSemaphore, Semaphore, Condition
import Rop, time, Direcao, random, sys

smf = BoundedSemaphore(value=4)
rop = Rop.Rop(None)


class Babuino(Thread) :

    def __init__(self, position, time):

        Thread.__init__(self)
        self.position = position                            # posicao inicial do babuino
        self.time = time                                    # tempo

    def atravessar(self):

        if rop.direcao is None:

            smf.acquire()
            rop.direcao = self.position
            rop.rop.append(self)

            if self.position == "East":
                Direcao.East.popleft()
            else:
                Direcao.West.popleft()

            rop.maximo += 1

            sys.stdout.write(str(self.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
            sys.stdout.flush()

            time.sleep(5)
            rop.rop.popleft()

            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()

            smf.release()


        # if len(rop.rop) is 0:
        #
        #     smf.acquire()
        #     time.sleep(1)
        #     rop.rop.append(self)
        #     rop.direcao = self.position
        #     for i in rop.rop:
        #         sys.stdout.write(str(i.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
        #         sys.stdout.flush()
        #     time.sleep(4)
        #     rop.rop.popleft()
        #
        #     sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
        #     sys.stdout.flush()
        #
        #     # print(str(self.name) + " saiu da corda")
        #     smf.release()

        elif rop.direcao is self.position:

            smf.acquire()
            time.sleep(1)
            rop.rop.append(self)

            if self.position == "East":
                Direcao.East.popleft()
            else:
                Direcao.West.popleft()

            rop.maximo += 1

            sys.stdout.write(str(self.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
            sys.stdout.flush()

            time.sleep(4)
            rop.rop.popleft()

            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()

            smf.release()

            if rop.maximo == 4 or (rop.maximo > 0 and (len(Direcao.East)==0 or len(Direcao.West)==0)):
                print("Entrou no if")
                smf.acquire()
                rop.maximo = 0
                while len(rop.rop) != 0:
                    pass
                if rop.direcao == "East":
                    rop.direcao = "West"
                else:
                    rop.direcao = "East"
                smf.release()
                self.atravessar()
            # sys.stdout.write(rop.direcao)
            # sys.stdout.flush()



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