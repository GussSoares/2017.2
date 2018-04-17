from collections import deque

class Rop:

    def __init__(self, direcao):
        self.direcao = direcao
        self.rop = deque(maxlen=4)