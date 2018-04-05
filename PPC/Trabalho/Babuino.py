import random
from threading import Thread

class Babuino:

    def __init__(self, position, time):
        self.position = position                          # posicao inicial do babuino
        self.time = time                          # tempo

    def lucky_side(self):                                       # sorteia laoo que o babuino tem q ir
        lado = ["East", "West"]
        self.position = random.choice(lado)

    def lucky_time(self):                                       # sorteia o tempo q o babuino leva pra chegar no canyon
        self.time = random.randint(1,8)

    def printar(self):
        print("teste")

    # def create_thread(self):
    #     thread = Thread(target=self.printar)
    #     return thread.start()