from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        self.lc_only = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.all_sym = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=']

        self.uc_only = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.ucnum_only = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.ucsym_only = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                           't', 'u', 'v', 'w', 'x', 'y', 'z',
                           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                           'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                           '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=']

        self.numsym_only = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                            't', 'u', 'v', 'w', 'x', 'y', 'z',
                            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=']

        self.num_only = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z',
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.sym_only = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z',
                         '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=']

        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(1096, 645)
        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.number_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.number_checkbox.setGeometry(QtCore.QRect(450, 340, 161, 21))
        self.number_checkbox.setObjectName("number_checkbox")
        self.capital_letter_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.capital_letter_checkbox.setGeometry(QtCore.QRect(450, 310, 161, 21))
        self.capital_letter_checkbox.setObjectName("capital_letter_checkbox")
        self.symbol_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.symbol_checkbox.setGeometry(QtCore.QRect(450, 370, 161, 21))
        self.symbol_checkbox.setObjectName("symbol_checkbox")
        self.generate_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.generate_pushbutton.setGeometry(QtCore.QRect(450, 410, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.generate_pushbutton.setFont(font)
        self.generate_pushbutton.setObjectName("generate_pushbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 0, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam Mono CLM")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 50, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Miriam Mono CLM")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(450, 250, 42, 22))
        self.spinBox.setMinimum(6)
        self.spinBox.setMaximum(32)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 230, 171, 16))
        self.label_3.setObjectName("label_3")
        PasswordGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 21))
        self.menubar.setObjectName("menubar")
        PasswordGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordGenerator)
        self.statusbar.setObjectName("statusbar")
        PasswordGenerator.setStatusBar(self.statusbar)
        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)
        self.generate_pushbutton.clicked.connect(self.clicked)


    def clicked(self):
        self.password = []
        if self.capital_letter_checkbox.isChecked() == False and self.number_checkbox.isChecked() == False and self.symbol_checkbox.isChecked() == False:
            for i in range(self.spinBox.value()):  # lc_only
                self.random = randint(0, len(self.lc_only) - 1)
                self.password.append(self.lc_only[self.random])

        elif self.capital_letter_checkbox.isChecked() == True and self.number_checkbox.isChecked() == True and self.symbol_checkbox.isChecked() == True:
            for i in range(self.spinBox.value()):  # all_sym
                self.random = randint(0, len(self.all_sym) - 1)
                self.password.append(self.all_sym[self.random])

        elif self.capital_letter_checkbox.isChecked() == True and self.number_checkbox.isChecked() == False and self.symbol_checkbox.isChecked() == False:
            for i in range(self.spinBox.value()): # uc_only
                self.random = randint(0, len(self.uc_only) - 1)
                self.password.append(self.uc_only[self.random])

        elif self.capital_letter_checkbox.isChecked() == True and self.number_checkbox.isChecked() == True and self.symbol_checkbox.isChecked() == False:
            for i in range(self.spinBox.value()):  # ucnum_only
                self.random = randint(0, len(self.ucnum_only) - 1)
                self.password.append(self.ucnum_only[self.random])

        elif self.capital_letter_checkbox.isChecked() == True and self.number_checkbox.isChecked() == False and self.symbol_checkbox.isChecked() == True:
            for i in range(self.spinBox.value()):  # ucsym_only
                self.random = randint(0, len(self.ucsym_only) - 1)
                self.password.append(self.ucsym_only[self.random])

        elif self.capital_letter_checkbox.isChecked() == False and self.number_checkbox.isChecked() == True and self.symbol_checkbox.isChecked() == True:
            for i in range(self.spinBox.value()):  # numsym_only
                self.random = randint(0, len(self.numsym_only) - 1)
                self.password.append(self.numsym_only[self.random])

        elif self.capital_letter_checkbox.isChecked() == False and self.number_checkbox.isChecked() == True and self.symbol_checkbox.isChecked() == False:
            for i in range(self.spinBox.value()):  # num_only
                self.random = randint(0, len(self.num_only) - 1)
                self.password.append(self.num_only[self.random])

        elif self.capital_letter_checkbox.isChecked() == False and self.number_checkbox.isChecked() == False and self.symbol_checkbox.isChecked() == True:
            for i in range(self.spinBox.value()):  # sym_only
                self.random = randint(0, len(self.sym_only) - 1)
                self.password.append(self.sym_only[self.random])

        else:
            sys.exit(0)
        self.final = "".join(self.password)

        msg = QMessageBox()
        msg.setWindowTitle("New Password")
        msg.setText("Your new password has been generated:")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText(self.final)
        msg.setDetailedText(f"Your new password has been generated, the password is {self.final}\n"
                            f"The code successfully executed and can be run again to generate a new password.")
        msg.exec_()

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
        self.number_checkbox.setText(_translate("PasswordGenerator", "Numbers (0-9)"))
        self.capital_letter_checkbox.setText(_translate("PasswordGenerator", "Capital Letters"))
        self.symbol_checkbox.setText(_translate("PasswordGenerator", "Symbols (!@#$%^&*_-+=)"))
        self.generate_pushbutton.setText(_translate("PasswordGenerator", "Generate Password"))
        self.label.setText(_translate("PasswordGenerator", "Password Generator"))
        self.label_2.setText(_translate("PasswordGenerator", "Select boxes to create a structure you want for your password, "
                                                             "if certain symbols aren't allowed on a website you can remove them or swap in another symbol"))
        self.label_3.setText(_translate("PasswordGenerator", "Password Length: (6-32 chars long)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(app.exec_())
