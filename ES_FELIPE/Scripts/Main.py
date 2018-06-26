from Interface.Janela_1 import * #Ui_MainWindow
from Interface import Janela_2
from Interface import Janela_3
from Interface import matriz
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import functools

def cadastrar_Objetivo():
    objetivo = ui.writeObjetivo.text()
    print(objetivo)
    return objetivo
def cadastrar_Criterio():
    aux = ui.writeCriterio.text()
    criterios = aux.split("-")
    print(criterios)
    return criterios

def cadastrar_Atividade():
    aux = ui.writeAtividades.text()
    atividades = aux.split("-")
    print(atividades)
    return atividades


def cadastrar():
    cadastrar_Objetivo()
    crit = cadastrar_Criterio()
    len_crit = len(crit)

    ativ = cadastrar_Atividade()
    len_ativ = len(ativ)

    # #app = QtWidgets.QApplication(sys.argv)

    # Janela_2.MainWindow = QtWidgets.QMainWindow()
    # Janela_2.ui = Janela_2.Ui_MainWindow()
    # Janela_2.ui.setupUi(Janela_2.MainWindow, crit)
    # Janela_2.MainWindow.show()

    #sys.exit(app.exec_())

    # matriz.MainWindow = QtWidgets.QMainWindow()
    # matriz.ui = matriz.Ui_MainWindow()
    # matriz.ui.setupUi(matriz.MainWindow, len_crit, crit)
    # # matriz.ui.retranslateUi(matriz.MainWindow, crit)
    # matriz.MainWindow.show()

    Janela_3.MainWindow = QtWidgets.QMainWindow()
    Janela_3.ui = Janela_3.Ui_MainWindow()
    Janela_3.ui.setupUi(Janela_3.MainWindow, crit)
    Janela_3.MainWindow.show()

if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(functools.partial(cadastrar))
    sys.exit(app.exec_())