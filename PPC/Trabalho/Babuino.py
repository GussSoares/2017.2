# -*- coding: utf-8 -*-

import random
from threading import Thread
import Rop
# import Main

class Babuino(Thread):

    def __init__(self, position, time):

        Thread.__init__(self)
        self.position = position                            # posicao inicial do babuino
        self.time = time                                    # tempo
        self.arrived = False

    def atravessar(self):

        if len(Rop.rop) == 0:
            pass
        # self.arrived = True

    def run(self):
        # ação executada pela thread

        # print("teste")
        lado = ["East", "West"]
        self.position = random.choice(lado)
        self.time = random.randint(1,8)
        while self.arrived is False:
            pass
        self.atravessar()
    # def create_thread(self):
    #     thread = Thread(target=self.printar)
    #     return thread.start()