from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(380, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 240, 30))
        font = QtGui.QFont("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        # Поле ввода 1
        self.lineEdit_1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(260, 10, 113, 30))
        self.lineEdit_1.setObjectName("lineEdit_1")

        # Поле ввода 2
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 40, 113, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Поле ввода 3
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 70, 113, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")

        # Поле ввода 4
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 100, 113, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")

        # Поле ввода 5
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 130, 113, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")

        # Поле ввода 6
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 160, 113, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")

        # Поле ввода 7
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(260, 190, 113, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")

        # Поле ввода 8
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(260, 220, 113, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")

        # Строка вывода
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 280, 360, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.textBrowser.setObjectName("textBrowser")

        # Кнопка
        self.btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(130, 440, 120, 32))
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn.setObjectName("btn")

        # Логика
        def btn_click():
            # Переменные
            self.a1 = self.lineEdit_1.text()  # ;(* D NOMINAL M6, M8, M10...)     [30]
            self.a2 = self.lineEdit_2.text()  # ;(* THREAD PITCH [F])             [2]
            self.a3 = self.lineEdit_3.text()  # ;(* THREAD DEEP axis Z [mm])      [-30]

            self.a4 = self.lineEdit_4.text()  # ;(* SPINDLE SPEED)                [300]
            self.a5 = self.lineEdit_5.text()  # ;(* Q MIN CUT  [micron])          [50]
            self.a6 = self.lineEdit_6.text()  # ;(* Q MAX CUT [micron])           [100]
            self.a7 = self.lineEdit_7.text()  # ;(* R PRIPUSK [mm])               [0.4]
            self.a8 = self.lineEdit_8.text()  # ;(* R KONUS [mm])                 [0]
            # ;(* = "0", > "-", < "+")

            # Математика
            self.a9 = int(self.a1) + int(5)  # ;(RETRACT axis X)
            self.a10 = float(self.a2) * int(2)  # ;(RETRACT axis Z)
            self.a11 = float(self.a2) * int(542)  # ;(HEIGHT THREAD PROFILE [micron])
            self.a12 = int(self.a1) - float(self.a11) / int(1000) * int(2)  # ;(D DEEP axis X [mm])

            #  Результат в консоль
            # print('S' + str(self.a4))
            # print('(CYCLE REZBA)')
            # print('G00 X' + str(self.a9), 'Z' + str(self.a10), ';(RETRACT)')
            # print('G76 P021060 Q' + str(self.a5), 'R' + str(self.a7))
            # print('G76 X' + str(self.a12), 'Z' + str(self.a3), 'R' + str(self.a8), 'P' + str(self.a11), 'Q' + str(self.a6), 'F' + str(self.a2))

            # Результат
            info_str = (f'{str('S') + str(self.a4)} {str('M03')} \n'
                        f'{str('(CYCLE REZBA)')} \n'
                        f'{str('G00 X') + str(self.a9)} {str('Z') + str(self.a10)} {str(';(RETRACT)')} \n'
                        f'{str('G76 P021060 Q') + str(self.a5)} {str('R') + str(self.a7)} \n'
                        f'{str('G76 X') + str(self.a12)} {str('Z') + str(self.a3)} '
                        f'{str('R') + str(self.a8)} {str('P') + str(self.a11)} '
                        f'{str('Q') + str(self.a6)} {str('F') + str(self.a2)}')

            # Окно с ошибкой
            # messagebox.showerror(title='Ошибка', message='Расчёты не верны')

            self.textBrowser.setText(info_str)

        self.btn.clicked.connect(btn_click)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчет резьбы"))

        self.label_1.setText(_translate("MainWindow", "Наминальный диамерт: M"))
        self.label_2.setText(_translate("MainWindow", "Шаг резьбы: F"))
        self.label_3.setText(_translate("MainWindow", "Длина резьбы: L=mm"))
        self.label_4.setText(_translate("MainWindow", "Скорость шпинделя: S"))
        self.label_5.setText(_translate("MainWindow", "Минимальный съём: Q1=µm"))
        self.label_6.setText(_translate("MainWindow", "Максимальный съём: Q2=µm"))
        self.label_7.setText(_translate("MainWindow", "Припуск: R1=mm"))
        self.label_8.setText(_translate("MainWindow", "Конус: R2=mm"))

        self.lineEdit_1.setText(_translate("MainWindow", "30"))
        self.lineEdit_2.setText(_translate("MainWindow", "2"))
        self.lineEdit_3.setText(_translate("MainWindow", "-30"))
        self.lineEdit_4.setText(_translate("MainWindow", "300"))
        self.lineEdit_5.setText(_translate("MainWindow", "50"))
        self.lineEdit_6.setText(_translate("MainWindow", "100"))
        self.lineEdit_7.setText(_translate("MainWindow", "0.4"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))

        self.btn.setText(_translate("MainWindow", "Расчитать"))

        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
