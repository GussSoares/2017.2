# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Janela_3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import functools

from Interface import janela_4, warning, functions_criterio
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    criterio = None
    atividade = None
    objetivo = None
    """ Configura a interface atual, alguns objetos da interface são 
        configurados dinamicamentes, como a quantidade de linha e colunas da matriz"""
    def setupUi(self, MainWindow, crit, ativ, obj):
        global criterio, atividade, vetor, objetivo
        criterio = crit
        atividade = ativ
        objetivo = obj

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 418)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)

        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 621, 281))
        self.tableWidget.setRowCount(len(criterio))
        self.tableWidget.setColumnCount(len(criterio))

        for i in range(len(criterio)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 330, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 6, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """ Onde as funções são chamadas"""
    def central_funcao(self):
        try:
            valores = functions_criterio.decimal()
            soma = functions_criterio.soma_coluna(valores)
            normal = functions_criterio.normalizar_Matriz(soma, valores)
            eigen = functions_criterio.vetor_eigen(normal)
            lambd = functions_criterio.lambd(eigen, soma)
            ci = functions_criterio.ci(lambd)
            ri = functions_criterio.tabela_valor_ri(len(criterio))
            cr = functions_criterio.cr(ci, ri)


            janela_4.MainWindow = QtWidgets.QMainWindow()
            janela_4.ui = janela_4.Ui_MainWindow()
            janela_4.ui.setupUi(janela_4.MainWindow, criterio, atividade, objetivo, eigen, lambd, ci, cr)
            janela_4.MainWindow.show()

            janela_4.ui.pushButton.clicked.connect(functools.partial(janela_4.ui.preencher_Atividades))
            janela_4.ui.pushButton_2.clicked.connect(functools.partial(janela_4.ui.central_funcao))

        except:
            warning.MainWindow = QtWidgets.QMainWindow()
            warning.ui = warning.Ui_MainWindow()
            warning.ui.setupUi(warning.MainWindow)

            warning.MainWindow.show()
            warning.ui.pushButton.clicked.connect(functools.partial(warning.MainWindow.close))

    """Completa a triangular superior
        Adiciona os valores por coluna"""
    def preencher_Criterio(self):

        try:
            _translate = QtCore.QCoreApplication.translate
            importancia = functions_criterio.capturar_Valor_Matriz()
            x = 0
            for j in range(len(criterio)):
                for i in range(len(criterio)):
                    if i < j:
                        element = QtWidgets.QTableWidgetItem()
                        element.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.tableWidget.setItem(i, j, element)

                        valor = QtWidgets.QTableWidgetItem()
                        valor.setText(_translate("MainWindow", str(importancia[x])))
                        self.tableWidget.setItem(i, j, valor)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastrar Matriz de Critérios"))

        for i in range(len(criterio)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))  # critério 1

            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))

            for j in range(len(criterio)):
                if i <= j:  # Aqui era <=
                    element = QtWidgets.QTableWidgetItem()
                    element.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, j, element)

            """Resolvido o erro da diagonal"""
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow", "1"))
            self.tableWidget.setItem(i, i, item)
            item.setFlags(QtCore.Qt.ItemIsEnabled)

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Cadastrar Matriz"))
        self.label.setText(_translate("MainWindow", "Preencha a triangular inferior da matriz de critérios"))
        self.pushButton_2.setText(_translate("MainWindow", "Avançar"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

