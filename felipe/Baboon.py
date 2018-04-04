import random

class Babuino():
    def __init__(self, movimento, tempo):
        self.sentido_da_movimentacao = movimento  # Leste ou Oeste
        self.tempo_chegada_canyon = tempo     # Entre 1 e 8 segundos
       # print("Construtor")

    def sorteio_sentido(self):
        direcoes = ['Leste', 'Oeste']
        self.sentido_da_movimentacao = random.choice(direcoes) # Escolhe uma elemento de direcoes

    def sorteio_tempo_chegada(self):
        self.tempo_chegada_canyon = random.randint(1, 8)    # Escolhe um numero de 1 a 8

    # def imprime(self):
    #     print('sentirdo: %s' %(self.sentido_da_movimentacao))

# teste = Babuino()
# teste.sorteio_sentido()
# teste.imprime()