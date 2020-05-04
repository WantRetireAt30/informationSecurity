# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exp1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    def setupUi(self, Form):  # self就是用于存储对象属性的集合，就算没有属性self也是必备的
        Form.setObjectName("Form")
        Form.resize(966, 850)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_Caesar = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Caesar.setFont(font)
        self.pushButton_Caesar.setObjectName("pushButton_Caesar")
        self.horizontalLayout_8.addWidget(self.pushButton_Caesar)
        self.pushButton_Virginia = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Virginia.setFont(font)
        self.pushButton_Virginia.setObjectName("pushButton_Virginia")
        self.horizontalLayout_8.addWidget(self.pushButton_Virginia)
        self.pushButton_Decode = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Decode.setFont(font)
        self.pushButton_Decode.setObjectName("pushButton_Decode")
        self.horizontalLayout_8.addWidget(self.pushButton_Decode)
        self.pushButton_Reset = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Reset.setFont(font)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.horizontalLayout_8.addWidget(self.pushButton_Reset)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_Key = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Key.setFont(font)
        self.label_Key.setObjectName("label_Key")
        self.gridLayout.addWidget(self.label_Key, 1, 0, 1, 1)
        self.label_CipherText = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_CipherText.setFont(font)
        self.label_CipherText.setObjectName("label_CipherText")
        self.gridLayout.addWidget(self.label_CipherText, 5, 0, 1, 1)
        self.lineEdit_CipherText = QtWidgets.QLineEdit(Form)
        self.lineEdit_CipherText.setText("")
        self.lineEdit_CipherText.setObjectName("lineEdit_CipherText")
        self.gridLayout.addWidget(self.lineEdit_CipherText, 6, 0, 1, 1)
        self.lineEdit_PlainText = QtWidgets.QLineEdit(Form)
        self.lineEdit_PlainText.setText("")
        self.lineEdit_PlainText.setObjectName("lineEdit_PlainText")
        self.gridLayout.addWidget(self.lineEdit_PlainText, 4, 0, 1, 1)
        self.lineEdit_Key = QtWidgets.QLineEdit(Form)
        self.lineEdit_Key.setText("")
        self.lineEdit_Key.setObjectName("lineEdit_Key")
        self.gridLayout.addWidget(self.lineEdit_Key, 2, 0, 1, 1)
        self.label_PlainText = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_PlainText.setFont(font)
        self.label_PlainText.setObjectName("label_PlainText")
        self.gridLayout.addWidget(self.label_PlainText, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 2, 1, 1)

        self.retranslateUi(Form)
        self.pushButton_Reset.clicked.connect(self.lineEdit_Key.clear)
        self.pushButton_Reset.clicked.connect(self.lineEdit_PlainText.clear)
        self.pushButton_Reset.clicked.connect(self.lineEdit_CipherText.clear)
        self.pushButton_Caesar.clicked.connect(self.caesarEncode)
        self.pushButton_Virginia.clicked.connect(self.virginiaEncode)
        self.pushButton_Decode.clicked.connect(self.decode)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def caesarEncode(self):
        key = int(self.lineEdit_Key.text())
        plainText = self.lineEdit_PlainText.text()
        cipherText = ""
        for x in plainText:
            if 'a' <= x <= 'z':
                cipherText += chr(ord('a') + ((ord(x) - ord('a')) + key) % 26)  # ord()将字符串返回int类型
            elif 'A' <= x <= 'Z':
                cipherText += chr(ord('A') + ((ord(x) - ord('A')) + key) % 26)
            else:
                cipherText += x  # 空格等特殊符号，直接相加
        self.lineEdit_CipherText.setText(cipherText)

    def virginiaEncode(self):
        key = self.lineEdit_Key.text()
        plainText = self.lineEdit_PlainText.text()
        keyLen = len(key)
        cipherText = ""
        count = 0
        for i in plainText:
            keyHasUsed = False
            if key[count % keyLen].islower():
                k = ord(key[count % keyLen]) - ord('a')
            else:
                k = ord(key[count % keyLen]) - ord('A')
            if 'a' <= i <= 'z':
                cipherText += chr(ord('a') + ((ord(i) - ord('a')) + k) % 26)
                keyHasUsed = True
            elif 'A' <= i <= 'Z':
                cipherText += chr(ord('A') + ((ord(i) - ord('A')) + k) % 26)
                keyHasUsed = True
            else:
                cipherText += i
            if keyHasUsed:
                count += 1
        self.lineEdit_CipherText.setText(cipherText)

    def decode(self):
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "1712480133_Zrz"))
        self.pushButton_Caesar.setText(_translate("Form", "Caesar Cipher"))
        self.pushButton_Virginia.setText(_translate("Form", "Vigenere Cipher"))
        self.pushButton_Decode.setText(_translate("Form", "Decode"))
        self.pushButton_Reset.setText(_translate("Form", "Reset"))
        self.label_Key.setText(_translate("Form", "Key"))
        self.label_CipherText.setText(_translate("Form", "CipherText"))
        self.label_PlainText.setText(_translate("Form", "PlainText"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
