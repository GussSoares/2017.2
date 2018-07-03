import os
path = os.path.abspath('resultado.txt')

with open(path,"r+") as file:
    file.write("Resultado")
# print(path)
# os.path.realpath(file.name)