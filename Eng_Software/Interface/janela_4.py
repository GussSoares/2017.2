# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela_4.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import functools, os

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Interface import finish, Janela_3, functions_criterio, warning, functions_atividade


class Ui_MainWindow(object):
    criterio = None
    atividade = None
    objetivo = None
    """ Configura a interface atual, alguns objetos da interface são 
        configurados dinamicamentes, como a quantidade de linha e colunas da matriz"""
    def setupUi(self, MainWindow, crit, ativ, obj, _eigen, _lambd, _ci, _cr):
        global criterio, atividade, vetor, _objetivo_, _eigen_, _lambd_, _ci_, _cr_
        criterio = crit
        atividade = ativ
        _objetivo_ = obj
        _eigen_ = _eigen
        _lambd_ = _lambd
        _ci_ = _ci
        _cr_ = _cr
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 568)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 510, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 510, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Texto = QtWidgets.QLabel(self.centralwidget)
        self.Texto.setGeometry(QtCore.QRect(10, 20, 781, 18))

        """ Tive que colocar o translate aqui pois se não, só conseguia
        modificar os indices da última matriz de atividade. Pois
        apenas salvava o nome da última table Widget"""
        _translate = QtCore.QCoreApplication.translate

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        for i in range(len(criterio)):
            self.tab = QtWidgets.QWidget()
            self.tabWidget.addTab(self.tab, criterio[i])
            self.tab.setObjectName("tab " + str(i))

            self.tableWidget = QtWidgets.QTableWidget(self.tab)
            self.tabWidget.setGeometry(QtCore.QRect(4, 60, 791, 441))
            self.tabWidget.setObjectName("tabWidget")
            self.tableWidget.setColumnCount(len(atividade))
            self.tableWidget.setRowCount(len(atividade))

            self.tableWidget.setGeometry(QtCore.QRect(2, 1, 782, 412))
            self.tableWidget.setObjectName("tableWidget_" + str(i))

            for x in range(len(atividade)):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(x, item)

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(x, item)

                item = self.tableWidget.verticalHeaderItem(x)
                item.setText(_translate("MainWindow", atividade[x]))

                item = self.tableWidget.horizontalHeaderItem(x)
                item.setText(_translate("MainWindow", atividade[x]))

                for j in range(len(atividade)):
                    if x <= j:  # Aqui era <=
                        element = QtWidgets.QTableWidgetItem()
                        element.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.tableWidget.setItem(x, j, element)

                item = QtWidgets.QTableWidgetItem()
                item.setText(_translate("MainWindow", "1"))
                self.tableWidget.setItem(x, x, item)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)


        font = QtGui.QFont()
        font.setPointSize(13)
        self.Texto.setFont(font)
        self.Texto.setObjectName("Texto")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """ Onde as funções são chamadas e no final do processo 
        é criado um txt contendo o resultado do cálculo"""
    def central_funcao(self):
        try:
            valores = functions_atividade.decimal()
            soma = functions_atividade.soma_coluna(valores)
            normal = functions_atividade.normalizar_Matriz(soma, valores)
            eigen =functions_atividade.vetor_eigen(normal)
            lambd = functions_atividade.lambd(eigen, soma)
            ci = functions_atividade.ci(lambd)
            ri = functions_atividade.tabela_valor_ri(len(criterio))
            cr = functions_atividade.cr(ci, ri)


            print("criando arquivo")
            aux=0
            path = os.path.abspath('resultado.txt')
            with open(path, 'w') as file:

                file.write("Objetivo: "+str(_objetivo_))

                file.write("\n\n")

                file.write("Vetor de Eigen da Matriz de Critérios: "+str(_eigen_))

                file.write("\n\n")

                file.write("Auto Valor máximo da Matriz de Critérios: "+str(_lambd_))

                file.write("\n\n")

                file.write("CI da Matriz de Critérios: "+str(_ci_))

                file.write("\n\n")

                file.write("CR da Matriz de Critérios: "+str(_cr_))

                file.write("\n\n")

                for i in range(len(criterio)):
                    file.write("Vetor de Eigen da Matriz de atividade em relação ao critério "+str(criterio[i])+": ")
                    file.write("[")
                    for j in range(len(criterio)):
                        file.write(str(eigen[j+aux])+", ")
                    file.write("]\n")
                    aux+=len(atividade)

                file.write("\n\n")

                for i in range(len(criterio)):
                    file.write("Auto valor máximo da Matriz de atividades em relação ao critério "+str(criterio[i])+": ")
                    file.write(str(lambd[i])+"\n")

                file.write("\n\n")

                for i in range(len(criterio)):
                    file.write("CI da Matriz de atividades em relação ao critério "+str(criterio[i])+": ")
                    file.write(str(ci[i])+"\n")

                file.write("\n\n")

                for i in range(len(criterio)):
                    file.write("CR da Matriz de atividades em relação ao critério "+str(criterio[i])+": ")
                    file.write(str(cr[i])+"\n")

            finish.MainWindow = QtWidgets.QMainWindow()
            finish.ui = finish.Ui_MainWindow()
            finish.ui.setupUi(finish.MainWindow)
            finish.MainWindow.show()

            finish.ui.pushButton_2.clicked.connect(functools.partial(sys.exit))
            finish.ui.pushButton.clicked.connect(functools.partial(functions_criterio.close_multi_windows))
        except:
            warning.MainWindow = QtWidgets.QMainWindow()
            warning.ui = warning.Ui_MainWindow()
            warning.ui.setupUi(warning.MainWindow)

            warning.MainWindow.show()
            warning.ui.pushButton.clicked.connect(functools.partial(warning.MainWindow.close))

    """Completa a triangular superior
         Adiciona os valores por coluna"""
    def preencher_Atividades(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            importancia = functions_atividade.capturar_Valor_Matriz()
            x = 0
            for t in range(len(criterio)):
                matriz = self.tabWidget.findChild(QtCore.QObject, "tableWidget_" + str(t))
                for j in range(len(atividade)):
                    for i in range(len(atividade)):
                        if i < j:
                            element = QtWidgets.QTableWidgetItem()
                            element.setFlags(QtCore.Qt.ItemIsEnabled)
                            matriz.setItem(i, j, element)

                            valor = QtWidgets.QTableWidgetItem()
                            valor.setText(_translate("MainWindow", str(importancia[x])))
                            matriz.setItem(i, j, valor)
                            x += 1
        except:
            warning.MainWindow = QtWidgets.QMainWindow()
            warning.ui = warning.Ui_MainWindow()
            warning.ui.setupUi(warning.MainWindow)

            warning.MainWindow.show()
            warning.ui.pushButton.clicked.connect(functools.partial(warning.MainWindow.close))

    """ Renomeia itens na interface"""
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matriz de Atividades/Critérios"))

        self.pushButton.setText(_translate("MainWindow", "Cadastrar"))
        self.pushButton_2.setText(_translate("MainWindow", "Calcular"))
        self.Texto.setText(_translate("MainWindow", "Preencha a triangular inferior das matrizes em relação "
                                                    "a cada critério"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

