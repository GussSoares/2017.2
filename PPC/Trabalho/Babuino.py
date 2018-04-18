# -*- coding: utf-8 -*-

from threading import Thread, BoundedSemaphore, Semaphore, Condition
import Rop, time, Direcao, random, sys

smf = Semaphore(value=4)
smf_fluxo = Semaphore(value=4)
smf_teste = Semaphore(value=1)

smf_east = Semaphore()
smf_west = Semaphore()
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

            # if self.position == "East":
            #     Direcao.East.popleft()
            # else:
            #     Direcao.West.popleft()

            rop.maximo += 1
            sys.stdout.write("count = " + str(rop.maximo) + "\n")
            sys.stdout.flush()

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

            # if self.position == "East":
            #     Direcao.East.popleft()
            # else:
            #     Direcao.West.popleft()

            rop.maximo += 1
            sys.stdout.write("count = " + str(rop.maximo) + "\n")
            sys.stdout.flush()

            sys.stdout.write(str(self.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
            sys.stdout.flush()

            time.sleep(4)
            rop.rop.popleft()

            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()

            smf.release()

            if (rop.maximo == 4) or (rop.maximo > 0 and (len(Direcao.East)==0 or len(Direcao.West)==0)):
                smf_fluxo.acquire()
                sys.stdout.write("Entrou no if" + "\n")
                sys.stdout.flush()
                # print("Entrou no if")
                rop.maximo = 0
                # while len(rop.rop) != 0:
                #     pass
                if rop.direcao == "East":
                    rop.direcao = "West"
                    sys.stdout.write("DIRECAO DA CORDA ALTERADA PARA: " + rop.direcao + "\n")
                    sys.stdout.flush()

                else:
                    rop.direcao = "East"
                    sys.stdout.write("DIRECAO DA CORDA ALTERADA PARA: " + rop.direcao + "\n")
                    sys.stdout.flush()

                smf_fluxo.release()
                self.atravessar()
            # sys.stdout.write(rop.direcao)
            # sys.stdout.flush()



        # self.arrived = True

    def run(self):
        # ação executada pela thread

        # print("teste")
        lado = ["East", "West"]
        # self.position = random.choice(lado)
        self.time = random.randint(1,8)

        # smf_teste.acquire()

        if self.position == "East":
            smf_east.acquire()
        else:
            smf_west.acquire()

        time.sleep(self.time)

        if self.position == "East":
            Direcao.East.append(self)
            sys.stdout.write("adicionou" + str(self) + "em East" + "\n")
            sys.stdout.flush()
            # print("adicionou" + str(self) + "em East")
        else:
            Direcao.West.append(self)
            sys.stdout.write("adicionou" + str(self) + "em West" + "\n")
            sys.stdout.flush()
            # print("adicionou" + str(self) + "em West")
        # smf_teste.release()

        if self.position == "East":
            smf_east.release()
        else:
            smf_west.release()
        self.atravessar()