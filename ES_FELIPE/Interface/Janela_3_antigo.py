# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Janela_3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    criterio = None
    def setupUi(self, MainWindow, crit):
        global criterio
        criterio = crit

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 418)
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
        self.pushButton.setGeometry(QtCore.QRect(250, 330, 121, 31))
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

    """Ordem de captura dos valores: pega os valores da linha que 
        satisfaz a condição"""
    def capturar_Valor_Matriz(self):
        valores = []
        for i in range(len(criterio)):
            for j in range(len(criterio)):
                if i > j:
                    valores.append(self.tableWidget.item(i, j).text())
        for i in range(len(valores)):
            if "/" in valores[i]:
                valores[i] = valores[i].split("/")[1]
            else:
                valores[i] = "1/" + valores[i]

        print(valores)
        return valores

    def calcular_decimal(self):
        valores = []
        for i in range(len(criterio)):
            for j in range(len(criterio)):
                if i > j:
                    valores.append(float(self.tableWidget.item(i, j).text()))
        for i in range(len(valores)):
            if "/" in valores[i]:
                valores[i] = float(valores[i].split("/")[1])
            else:
                valores[i] = float(1 / int(valores[i]))

        print(valores)
        return valores

    """Adiciona os valores por coluna"""
    def preencher_Criterio(self):
        _translate = QtCore.QCoreApplication.translate
        importancia = self.capturar_Valor_Matriz()
        x = 0
        for j in range(len(criterio)):
            for i in range(len(criterio)):
                if i < j:
                    element = QtWidgets.QTableWidgetItem()
                    element.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, j, element)

                    valor = QtWidgets.QTableWidgetItem()
                    valor.setText(_translate("MainWindow", str(importancia[x])))
                    print(importancia[x])
                    self.tableWidget.setItem(i, j, valor)
                    x += 1


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        for i in range(len(criterio)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))  # critério 1

            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))

            for j in range(len(criterio)):
                if i == j:  #Aqui era <=
                    element = QtWidgets.QTableWidgetItem()
                    element.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, j, element)

            """Resolvido o erro da diagonal"""
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow", "1"))
            self.tableWidget.setItem(i, i, item)
            item.setFlags(QtCore.Qt.ItemIsEnabled)

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)# Aqui é False

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Cadastrar Matriz"))
        self.label.setText(_translate("MainWindow", "Preencha a triangular inferior da matriz de critérios"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

