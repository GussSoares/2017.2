# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
import Rop, time, Direcao, random

smf = Semaphore(6)

class Babuino(Thread) :

    def __init__(self, position, time):

        Thread.__init__(self)
        self.position = position                            # posicao inicial do babuino
        self.time = time                                    # tempo
        self.arrived = False



    def atravessar(self):

        smf.acquire()
        if len(Rop.rop) == 0:

            Rop.rop.append(Direcao.East[0])
        print("Corda: " + str(Rop.rop))
        smf.release()
        # self.arrived = True

    def run(self):
        # ação executada pela thread

        # print("teste")
        lado = ["East", "West"]
        self.position = random.choice(lado)
        self.time = random.randint(1,8)
        # time.sleep(1)
        while True:
            pass
        # self.atravessar()
        # print("FIM DA THREAD")
    # def create_thread(self):
    #     thread = Thread(target=self.printar)
    #     return thread.start()
