# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matriz.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    criterio = None
    def setupUi(self, MainWindow, tam, crit):
        global criterio
        criterio = crit
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 306)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 491, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(tam) #Era 2
        self.tableWidget.setRowCount(tam)

        for i in range(len(criterio)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)

        # for i in range(tam):
        #     item = QtWidgets.QTableWidgetItem()
        #     self.tableWidget.setHorizontalHeaderItem(i, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(1, 1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        for i in range(len(criterio)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))#critério 1

            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))

        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "critério 2"))
        #
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "critério"))
        #
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "critério 2"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        # for i in range(len(criterio)):
        #     print(i)
            # item = self.tableWidget.item(i, i)
            # item.setText(_translate("MainWindow", "1"))

        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))

        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "1"))

        # item = self.tableWidget.item(2, 2)
        # item.setText(_translate("MainWindow", "1"))

        # item = self.tableWidget.item(3, 3)
        # item.setText(_translate("MainWindow", "1"))

        self.tableWidget.setSortingEnabled(__sortingEnabled)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

