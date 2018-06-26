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
        MainWindow.resize(629, 381)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 611, 301))
        self.tableWidget.setMinimumSize(QtCore.QSize(610, 300))
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
        self.tableWidget.setItem(i, i, item)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 629, 21))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        for i in range(len(criterio)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i])) #critério 1

            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))



            for j in range(len(criterio)):
                if i<=j:
                    element = QtWidgets.QTableWidgetItem()
                    element.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, j, element)

            """Resolvido o erro da diagonal"""
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow","1"))
            self.tableWidget.setItem(i,i,item)
            item.setFlags(QtCore.Qt.ItemIsEnabled)

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        """O Problema está neste for, o codigo só coloca 1 na posição (0, 0)
        mesmo se n usar o for"""
        # for k in range(len(criterio)):
            # print(i)
            # item = self.tableWidget.item(k, k)
            # item.setText(_translate("MainWindow", "1"))
            # self.tableWidget.setItem(k, k, item)

        self.tableWidget.setSortingEnabled(__sortingEnabled)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

