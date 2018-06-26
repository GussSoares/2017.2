#!/usr/bin/python3

# from interface.matriz import Ui_MainWindow
# import numpy as np

from interface.tela1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

criterios = []

# def matriz(qtd_criterios, matriz):
#     for i in range(1, qtd_criterios+1+1):
#         linhas = []
#             linhas.append(criterios[j-1])
#         mat.append(linhas)
#     return mat
#
#
# if __name__ == "__main__":
#     j=0
#         for j in range(1, qtd_criterios+1+1):
#     objective = input("diga seu objetivo: ")
#     qtd_criterios = int(input("Quantos criterios: "))
#
#     mat = np.zeros((qtd_criterios, qtd_criterios))
#     np.fill_diagonal(mat, 1)
#
#     print("Critérios:")
#     for i in range(0, qtd_criterios):
#         j=j+i
#     print("triangular inferior = ", j)
#
#     print(mat)
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #------------------------------------

    #------------------------------------
    MainWindow.show()
    # ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    sys.exit(app.exec_())