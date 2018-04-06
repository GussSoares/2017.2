from Babuino import Babuino
from threading import Thread
East = []
West = []
field = []
count = 1

# babuino = Babuino(None, None)
#
# babuino.lucky_side()
# babuino.lucky_time()
# babuino.create_thread()

# print(babuino.initial_pos)
# print(babuino.time)
# a.join()

while count <=50:
    # name = "babuino"+str(count)
    babuino = Babuino(None, None)
    babuino.lucky_side()
    babuino.lucky_time()
    field.append(babuino)
    count +=1

print("Campo inicial: " + str(len(field)))

# for i in range(len(field)):
#     if field[i].position == "East":
#         East.append(field[i])
#     else:
#         West.append(field[i])

# for i in range(len(field)):
#     field.pop()

# print("POSICIONAMENTO")
# print("Campo inicial: " + str(len(field)))
# print("Leste: " + str(len(East)))

# for i in East:
#     print(str(i.position) + " " + str(i.time))
#
# print("Oeste: " + str(len(West)))
#
# for i in West:
#     print(str(i.position) + " " + str(i.time))
for i in range(len(field)):
    field[i].start()


# print(East[0].position)
