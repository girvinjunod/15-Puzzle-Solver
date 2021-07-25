from PyQt5 import QtCore, QtGui, QtWidgets,QtTest
from PyQt5.QtWidgets import QMessageBox
from solver import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 492)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.solvebutton = QtWidgets.QPushButton(self.centralwidget)
        self.solvebutton.setGeometry(QtCore.QRect(50, 150, 191, 41))
        self.solvebutton.setObjectName("solvebutton")

        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setGeometry(QtCore.QRect(50, 240, 191, 41))
        self.resetbutton.setObjectName("resetbutton")

        self.solvebutton.clicked.connect(self.solveClicked)
        self.resetbutton.clicked.connect(self.resetClicked)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(370, 110, 242, 242))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 3, item)

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(60)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 370, 571, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlaceholderText("Langkah")
        self.plainTextEdit.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "15 Puzzle Solver"))
        self.solvebutton.setText(_translate("MainWindow", "Solve"))
        self.resetbutton.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "15 Puzzle Solver"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "15"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def getValue(self):
        temp = []
        for i in range(4):
            for j in range(4):
                temp.append(self.tableWidget.item(i,j).text())
        return temp

    def changeValue(self, p):
        #p = [1,2,3,4,...]
        count = 0
        for i in range(4):
            for j in range(4):
                if p[count] == 16:
                    self.tableWidget.item(i,j).setText("")
                else:
                    self.tableWidget.item(i,j).setText(str(p[count]))
                count+=1
        
    def validateValue(self, p):
        #val = ["1","2",...]
        val = p[:]
        if len(val) != 16:
            return False, []
        try:
            for i in range(len(val)):
                if val[i] == "" or val[i]==" ":
                    val[i] = 16
                val[i] = int(val[i])
        except:
            return False, []
        temp = []
        for i in range(len(val)):
            if val[i] in temp or val[i] < 1 or val[i] > 16 :
                return False, []
            temp.append(val[i])
        return True, val

    def solveClicked(self):
        print("clicked")
        val = self.getValue()
        check = self.validateValue(val)
        if check[0] == False:
            self.popupError()
        else:
            p = check[1]
            if kurang(p) == False:
                self.popupUnsolvable()
            else:
                res, found = astar(p)
                path = res[2]
                langkah = res[4]
                self.outLangkah(langkah)
                for i in range(len(path)):
                    self.changeValue(path[i])
                    QtTest.QTest.qWait(1000)
                print(path)
                print(langkah)

    def outLangkah(self,l):
        teks = "Langkah: "
        for i in range(len(l)):
            if i != len(l)-1:
                teks += l[i] + ", "
            else:
                teks += l[i]
        self.plainTextEdit.setPlainText(teks)


    def resetClicked(self):
        print("clicked")
        p = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",""]
        self.changeValue(p)

    def popupUnsolvable(self):
        msg = QMessageBox(MainWindow)
        msg.setWindowTitle("Notice        ")
        msg.setText("Puzzle Unsolvable!!         ")
        msg.setIcon(QMessageBox.Information)
        x= msg.exec_()

        
    def popupError(self):
        msg = QMessageBox(MainWindow)
        msg.setWindowTitle("Notice        ")
        msg.setText("Input Error!!         ")
        msg.setIcon(QMessageBox.Warning)
        x= msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
