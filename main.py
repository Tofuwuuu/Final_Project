# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './interfaces/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initialWindow(object):
    def setupUi(self, initialWindow):
        initialWindow.setObjectName("initialWindow")
        initialWindow.resize(626, 504)
        initialWindow.setMaximumSize(QtCore.QSize(626, 504))
        initialWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(initialWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 340, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 340, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 400, 371, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(110, 40, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.Title.setTextFormat(QtCore.Qt.RichText)
        self.Title.setScaledContents(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        initialWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(initialWindow)
        self.statusbar.setObjectName("statusbar")
        initialWindow.setStatusBar(self.statusbar)

        self.retranslateUi(initialWindow)
        QtCore.QMetaObject.connectSlotsByName(initialWindow)

    def retranslateUi(self, initialWindow):
        _translate = QtCore.QCoreApplication.translate
        initialWindow.setWindowTitle(_translate("initialWindow", "Consultation System"))
        self.pushButton.setText(_translate("initialWindow", "Sign up"))
        self.pushButton_2.setText(_translate("initialWindow", "Login"))
        self.pushButton_3.setText(_translate("initialWindow", "Forgot password?"))
        self.Title.setText(_translate("initialWindow", "Consultation System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    initialWindow = QtWidgets.QMainWindow()
    ui = Ui_initialWindow()
    ui.setupUi(initialWindow)
    initialWindow.show()
    sys.exit(app.exec_())
