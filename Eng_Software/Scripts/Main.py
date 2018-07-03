from Interface.Janela_1 import *
from Interface import Janela_3, janela_4
from Interface import warning
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import functools
# Imports da Main
#------------------------------------------------------------
"""Captura o objetivo que o usuário digitou e
    armazena em uma lista"""
def cadastrar_Objetivo():
    objetivo = ui.writeObjetivo.text()
    print(objetivo)
    return objetivo

"""Captura os critérios que o usuário digitou 
    e armazena em uma lista"""
def cadastrar_Criterio():
    aux = ui.writeCriterio.text()
    criterios = aux.split("-")
    print(criterios)
    return criterios

"""Captura as atividades que o usuário digitou
    e armazena em uma lista"""
def cadastrar_Atividade():
    aux = ui.writeAtividades.text()
    atividades = aux.split("-")
    print(atividades)
    return atividades

"""Chama as funções de cadastro e inicia a janela de aviso
    ou a próxima janela"""
def cadastrar():
    cadastrar_Objetivo()
    crit = cadastrar_Criterio()
    objetivo = cadastrar_Objetivo()
    ativ = cadastrar_Atividade()

    if (len(crit) <= 2 or len(crit) > 15) or (len(ativ) <= 2 or len(ativ) > 15):
        warning.MainWindow = QtWidgets.QMainWindow()
        warning.ui = warning.Ui_MainWindow()
        warning.ui.setupUi(warning.MainWindow)

        warning.MainWindow.show()
        warning.ui.pushButton.clicked.connect(functools.partial(warning.MainWindow.close))

    else:
        Janela_3.MainWindow = QtWidgets.QMainWindow()
        Janela_3.ui = Janela_3.Ui_MainWindow()
        Janela_3.ui.setupUi(Janela_3.MainWindow, crit, ativ, objetivo)

        Janela_3.MainWindow.show()

        Janela_3.ui.pushButton.clicked.connect(functools.partial(Janela_3.ui.preencher_Criterio))
        Janela_3.ui.pushButton_2.clicked.connect(functools.partial(Janela_3.ui.central_funcao))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(functools.partial(cadastrar))
    sys.exit(app.exec_())

#-------------------------------------------------------------------------------------------------------------------