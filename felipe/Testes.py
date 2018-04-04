import random

# sentido_da_movimentacao = None
# tempo_chegada_canyon = None
#
#
# #def sorteio_sentido(self):
# direcoes = ['Leste', 'Oeste']
# sentido_da_movimentacao = random.choice(direcoes)  # Escolhe uma elemento de direcoes
#
#
# #def sorteio_tempo_chegada(self):
# #tempos = [1, 2, 3, 4, 5, 6, 7, 8]
# tempo_chegada_canyon = random.randint(1, 8)


sentido_da_movimentacao   # Leste ou Oeste
tempo_chegada_canyon      # Entre 1 e 8 segundos

def sorteio_sentido():
    direcoes = ['Leste', 'Oeste']
    sentido_da_movimentacao = random.choice(direcoes)

def sorteio_tempo_chegada():
    tempo_chegada_canyon = random.randint(1, 8)    # Escolhe um numero de 1 a 8

print(sentido_da_movimentacao)
print(tempo_chegada_canyon)