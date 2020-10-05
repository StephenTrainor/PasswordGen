from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        self.reg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z']
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(1096, 645)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON_PASSWORD.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PasswordGenerator.setWindowIcon(icon)
        PasswordGenerator.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.generate_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.generate_pushbutton.setGeometry(QtCore.QRect(10, 540, 201, 51))
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
        self.spinBox.setGeometry(QtCore.QRect(70, 480, 61, 51))
        self.spinBox.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(40)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.equal_box = QtWidgets.QCheckBox(self.centralwidget)
        self.equal_box.setGeometry(QtCore.QRect(910, 550, 181, 51))
        self.equal_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.equal_box.setObjectName("equal_box")
        self.plus_box = QtWidgets.QCheckBox(self.centralwidget)
        self.plus_box.setGeometry(QtCore.QRect(910, 500, 181, 51))
        self.plus_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.plus_box.setObjectName("plus_box")
        self.dash_box = QtWidgets.QCheckBox(self.centralwidget)
        self.dash_box.setGeometry(QtCore.QRect(910, 450, 181, 51))
        self.dash_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.dash_box.setObjectName("dash_box")
        self.underscore_box = QtWidgets.QCheckBox(self.centralwidget)
        self.underscore_box.setGeometry(QtCore.QRect(910, 400, 181, 51))
        self.underscore_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.underscore_box.setObjectName("underscore_box")
        self.asterik_box = QtWidgets.QCheckBox(self.centralwidget)
        self.asterik_box.setGeometry(QtCore.QRect(910, 350, 181, 51))
        self.asterik_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.asterik_box.setObjectName("asterik_box")
        self.and_box = QtWidgets.QCheckBox(self.centralwidget)
        self.and_box.setGeometry(QtCore.QRect(910, 300, 181, 51))
        self.and_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.and_box.setObjectName("and_box")
        self.carrot_box = QtWidgets.QCheckBox(self.centralwidget)
        self.carrot_box.setGeometry(QtCore.QRect(710, 550, 181, 51))
        self.carrot_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.carrot_box.setObjectName("carrot_box")
        self.percent_box = QtWidgets.QCheckBox(self.centralwidget)
        self.percent_box.setGeometry(QtCore.QRect(710, 500, 181, 51))
        self.percent_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.percent_box.setObjectName("percent_box")
        self.dollar_box = QtWidgets.QCheckBox(self.centralwidget)
        self.dollar_box.setGeometry(QtCore.QRect(710, 450, 181, 51))
        self.dollar_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.dollar_box.setObjectName("dollar_box")
        self.hash_box = QtWidgets.QCheckBox(self.centralwidget)
        self.hash_box.setGeometry(QtCore.QRect(710, 400, 181, 51))
        self.hash_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.hash_box.setObjectName("hash_box")
        self.at_box = QtWidgets.QCheckBox(self.centralwidget)
        self.at_box.setGeometry(QtCore.QRect(710, 350, 181, 51))
        self.at_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.at_box.setObjectName("at_box")
        self.exclamation_box = QtWidgets.QCheckBox(self.centralwidget)
        self.exclamation_box.setGeometry(QtCore.QRect(710, 300, 181, 51))
        self.exclamation_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.exclamation_box.setObjectName("exclamation_box")
        self.brackets_box = QtWidgets.QCheckBox(self.centralwidget)
        self.brackets_box.setGeometry(QtCore.QRect(910, 250, 181, 51))
        self.brackets_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.brackets_box.setObjectName("brackets_box")
        self.braces_box = QtWidgets.QCheckBox(self.centralwidget)
        self.braces_box.setGeometry(QtCore.QRect(910, 200, 181, 51))
        self.braces_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.braces_box.setObjectName("braces_box")
        self.parentheses_box = QtWidgets.QCheckBox(self.centralwidget)
        self.parentheses_box.setGeometry(QtCore.QRect(910, 150, 181, 51))
        self.parentheses_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.parentheses_box.setObjectName("parentheses_box")
        self.backslash_box = QtWidgets.QCheckBox(self.centralwidget)
        self.backslash_box.setGeometry(QtCore.QRect(530, 200, 181, 51))
        self.backslash_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.backslash_box.setObjectName("backslash_box")
        self.comma_box = QtWidgets.QCheckBox(self.centralwidget)
        self.comma_box.setGeometry(QtCore.QRect(710, 250, 181, 51))
        self.comma_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.comma_box.setObjectName("comma_box")
        self.period_box = QtWidgets.QCheckBox(self.centralwidget)
        self.period_box.setGeometry(QtCore.QRect(710, 200, 181, 51))
        self.period_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.period_box.setObjectName("period_box")
        self.question_box = QtWidgets.QCheckBox(self.centralwidget)
        self.question_box.setGeometry(QtCore.QRect(710, 150, 181, 51))
        self.question_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.question_box.setObjectName("question_box")
        self.colon_box = QtWidgets.QCheckBox(self.centralwidget)
        self.colon_box.setGeometry(QtCore.QRect(530, 300, 181, 51))
        self.colon_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.colon_box.setObjectName("colon_box")
        self.semicolon_box = QtWidgets.QCheckBox(self.centralwidget)
        self.semicolon_box.setGeometry(QtCore.QRect(530, 350, 181, 51))
        self.semicolon_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.semicolon_box.setObjectName("semicolon_box")
        self.doublequotes_box = QtWidgets.QCheckBox(self.centralwidget)
        self.doublequotes_box.setGeometry(QtCore.QRect(530, 400, 181, 51))
        self.doublequotes_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.doublequotes_box.setObjectName("doublequotes_box")
        self.nine_box = QtWidgets.QCheckBox(self.centralwidget)
        self.nine_box.setGeometry(QtCore.QRect(10, 0, 181, 51))
        self.nine_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.nine_box.setObjectName("nine_box")
        self.eight_box = QtWidgets.QCheckBox(self.centralwidget)
        self.eight_box.setGeometry(QtCore.QRect(10, 50, 181, 51))
        self.eight_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.eight_box.setObjectName("eight_box")
        self.zero_box = QtWidgets.QCheckBox(self.centralwidget)
        self.zero_box.setGeometry(QtCore.QRect(180, 0, 181, 51))
        self.zero_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.zero_box.setObjectName("zero_box")
        self.seven_box = QtWidgets.QCheckBox(self.centralwidget)
        self.seven_box.setGeometry(QtCore.QRect(10, 100, 181, 51))
        self.seven_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.seven_box.setObjectName("seven_box")
        self.six_box = QtWidgets.QCheckBox(self.centralwidget)
        self.six_box.setGeometry(QtCore.QRect(10, 150, 181, 51))
        self.six_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.six_box.setObjectName("six_box")
        self.five_box = QtWidgets.QCheckBox(self.centralwidget)
        self.five_box.setGeometry(QtCore.QRect(10, 200, 181, 51))
        self.five_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.five_box.setObjectName("five_box")
        self.four_box = QtWidgets.QCheckBox(self.centralwidget)
        self.four_box.setGeometry(QtCore.QRect(180, 200, 181, 51))
        self.four_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.four_box.setObjectName("four_box")
        self.three_box = QtWidgets.QCheckBox(self.centralwidget)
        self.three_box.setGeometry(QtCore.QRect(180, 150, 181, 51))
        self.three_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.three_box.setObjectName("three_box")
        self.one_box = QtWidgets.QCheckBox(self.centralwidget)
        self.one_box.setGeometry(QtCore.QRect(180, 50, 181, 51))
        self.one_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.one_box.setObjectName("one_box")
        self.two_box = QtWidgets.QCheckBox(self.centralwidget)
        self.two_box.setGeometry(QtCore.QRect(180, 100, 181, 51))
        self.two_box.setStyleSheet("font: 10pt \"MV Boli\";")
        self.two_box.setObjectName("two_box")
        self.uppercase_box = QtWidgets.QCheckBox(self.centralwidget)
        self.uppercase_box.setGeometry(QtCore.QRect(10, 380, 201, 41))
        self.uppercase_box.setStyleSheet("font: 10pt \"Swis721 Ex BT\";")
        self.uppercase_box.setObjectName("uppercase_box")
        self.lessthan_box = QtWidgets.QCheckBox(self.centralwidget)
        self.lessthan_box.setGeometry(QtCore.QRect(530, 550, 181, 51))
        self.lessthan_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.lessthan_box.setObjectName("lessthan_box")
        self.greaterthan_box = QtWidgets.QCheckBox(self.centralwidget)
        self.greaterthan_box.setGeometry(QtCore.QRect(530, 500, 181, 51))
        self.greaterthan_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.greaterthan_box.setObjectName("greaterthan_box")
        self.singlequotes_box = QtWidgets.QCheckBox(self.centralwidget)
        self.singlequotes_box.setGeometry(QtCore.QRect(530, 450, 181, 51))
        self.singlequotes_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.singlequotes_box.setObjectName("singlequotes_box")
        self.tilda_box = QtWidgets.QCheckBox(self.centralwidget)
        self.tilda_box.setGeometry(QtCore.QRect(910, 100, 181, 51))
        self.tilda_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.tilda_box.setObjectName("tilda_box")
        self.forwardslash_box = QtWidgets.QCheckBox(self.centralwidget)
        self.forwardslash_box.setGeometry(QtCore.QRect(530, 250, 181, 51))
        self.forwardslash_box.setStyleSheet("font: 9pt \"Swis721 Ex BT\";")
        self.forwardslash_box.setObjectName("forwardslash_box")
        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)
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

        if self.equal_box.isChecked() == True:
            self.reg.append('=')
        else:
            pass

        if self.plus_box.isChecked() == True:
            self.reg.append('+')
        else:
            pass

        if self.dash_box.isChecked() == True:
            self.reg.append('-')
        else:
            pass

        if self.underscore_box.isChecked() == True:
            self.reg.append('_')
        else:
            pass

        if self.asterik_box.isChecked() == True:
            self.reg.append('*')
        else:
            pass

        if self.and_box.isChecked() == True:
            self.reg.append('&')
        else:
            pass

        if self.carrot_box.isChecked() == True:
            self.reg.append('^')
        else:
            pass

        if self.percent_box.isChecked() == True:
            self.reg.append('%')
        else:
            pass

        if self.dollar_box.isChecked() == True:
            self.reg.append('$')
        else:
            pass

        if self.hash_box.isChecked() == True:
            self.reg.append('#')
        else:
            pass

        if self.at_box.isChecked() == True:
            self.reg.append('@')
        else:
            pass

        if self.exclamation_box.isChecked() == True:
            self.reg.append('!')
        else:
            pass

        if self.brackets_box.isChecked() == True:
            self.reg.append('[')
            self.reg.append(']')
        else:
            pass

        if self.braces_box.isChecked() == True:
            self.reg.append('{')
            self.reg.append('}')
        else:
            pass

        if self.parentheses_box.isChecked() == True:
            self.reg.append('(')
            self.reg.append(')')
        else:
            pass

        if self.backslash_box.isChecked() == True:
            self.reg.append(r""" \ """)
        else:
            pass

        if self.comma_box.isChecked() == True:
            self.reg.append(',')
        else:
            pass

        if self.period_box.isChecked() == True:
            self.reg.append('.')
        else:
            pass

        if self.question_box.isChecked() == True:
            self.reg.append('?')
        else:
            pass

        if self.colon_box.isChecked() == True:
            self.reg.append(':')
        else:
            pass

        if self.semicolon_box.isChecked() == True:
            self.reg.append(';')
        else:
            pass

        if self.doublequotes_box.isChecked() == True:
            self.reg.append(r""" " """)
        else:
            pass

        if self.nine_box.isChecked() == True:
            self.reg.append('9')
        else:
            pass

        if self.eight_box.isChecked() == True:
            self.reg.append('8')
        else:
            pass

        if self.seven_box.isChecked() == True:
            self.reg.append('7')
        else:
            pass

        if self.six_box.isChecked() == True:
            self.reg.append('6')
        else:
            pass

        if self.five_box.isChecked() == True:
            self.reg.append('5')
        else:
            pass

        if self.four_box.isChecked() == True:
            self.reg.append('4')
        else:
            pass

        if self.three_box.isChecked() == True:
            self.reg.append('3')
        else:
            pass

        if self.two_box.isChecked() == True:
            self.reg.append('2')
        else:
            pass

        if self.one_box.isChecked() == True:
            self.reg.append('1')
        else:
            pass

        if self.uppercase_box.isChecked() == True:
            self.counter = 0
            self.alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for i in range(len(self.alpha)):
                self.reg.append(self.alpha[self.counter])
                self.counter += 1
        else:
            pass

        if self.lessthan_box.isChecked() == True:
            self.reg.append('<')
        else:
            pass

        if self.greaterthan_box.isChecked() == True:
            self.reg.append('>')
        else:
            pass

        if self.singlequotes_box.isChecked() == True:
            self.reg.append(r""" ' """)
        else:
            pass

        if self.tilda_box.isChecked() == True:
            self.reg.append('~')
        else:
            pass

        if self.forwardslash_box.isChecked() == True:
            self.reg.append(r""" / """)
        else:
            pass
        for i in range(self.spinBox.value()):
            self.random = randint(0, len(self.reg) - 1)
            self.password.append(self.reg[self.random])
        self.semifinal = "".join(self.password)
        self.final = self.semifinal.replace(" ", "")
        msg = QMessageBox()
        msg.setWindowTitle("New Password")
        msg.setText("Your new password has been generated:")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText(self.final)
        msg.setDetailedText(f"Your new password has been generated: \n\n{self.final}\n\n"
                            f"The code successfully executed and can be run again to generate a new password.")
        msg.exec_()

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
        self.generate_pushbutton.setText(_translate("PasswordGenerator", "Generate Password"))
        self.label.setText(_translate("PasswordGenerator", "Password Generator"))
        self.label_2.setText(_translate("PasswordGenerator", "Select boxes to create a structure you want for your password"))
        self.label_3.setText(_translate("PasswordGenerator", "Password Length: (1-40 chars long)"))
        self.equal_box.setText(_translate("PasswordGenerator", "Include equal sign (=)"))
        self.plus_box.setText(_translate("PasswordGenerator", "Include plus sign(+)"))
        self.dash_box.setText(_translate("PasswordGenerator", "Include dash (-)"))
        self.underscore_box.setText(_translate("PasswordGenerator", "Include underscore (_)"))
        self.asterik_box.setText(_translate("PasswordGenerator", "Include asterik (*)"))
        self.and_box.setText(_translate("PasswordGenerator", "Include \'and\' symbol "))
        self.carrot_box.setText(_translate("PasswordGenerator", "Include carrot (^)"))
        self.percent_box.setText(_translate("PasswordGenerator", "Include percent sign (%)"))
        self.dollar_box.setText(_translate("PasswordGenerator", "Include dollar sign ($)"))
        self.hash_box.setText(_translate("PasswordGenerator", "Include hash mark (#)"))
        self.at_box.setText(_translate("PasswordGenerator", "Include \'at\' symbol (@)"))
        self.exclamation_box.setText(_translate("PasswordGenerator", "Include exclamation mark (!)"))
        self.brackets_box.setText(_translate("PasswordGenerator", "Include brackets [ ]"))
        self.braces_box.setText(_translate("PasswordGenerator", "Include braces { }"))
        self.parentheses_box.setText(_translate("PasswordGenerator", "Include parentheses ()"))
        self.backslash_box.setText(_translate("PasswordGenerator", "Include back slash \\"))
        self.comma_box.setText(_translate("PasswordGenerator", "Include commas (,)"))
        self.period_box.setText(_translate("PasswordGenerator", "Include periods (.)"))
        self.question_box.setText(_translate("PasswordGenerator", "Include question mark (?)"))
        self.colon_box.setText(_translate("PasswordGenerator", "Include colon (:)"))
        self.semicolon_box.setText(_translate("PasswordGenerator", "Include semicolon (;)"))
        self.doublequotes_box.setText(_translate("PasswordGenerator", "Include double quotes (\")"))
        self.nine_box.setText(_translate("PasswordGenerator", "Include the number 9"))
        self.eight_box.setText(_translate("PasswordGenerator", "Include the number 8"))
        self.zero_box.setText(_translate("PasswordGenerator", "Include the number 0"))
        self.seven_box.setText(_translate("PasswordGenerator", "Include the number 7"))
        self.six_box.setText(_translate("PasswordGenerator", "Include the number 6"))
        self.five_box.setText(_translate("PasswordGenerator", "Include the number 5"))
        self.four_box.setText(_translate("PasswordGenerator", "Include the number 4"))
        self.three_box.setText(_translate("PasswordGenerator", "Include the number 3"))
        self.one_box.setText(_translate("PasswordGenerator", "Include the number 1"))
        self.two_box.setText(_translate("PasswordGenerator", "Include the number 2"))
        self.uppercase_box.setText(_translate("PasswordGenerator", "Include uppercase letters"))
        self.lessthan_box.setText(_translate("PasswordGenerator", "Include <"))
        self.greaterthan_box.setText(_translate("PasswordGenerator", "Include  >"))
        self.singlequotes_box.setText(_translate("PasswordGenerator", "Include single quotes (\')"))
        self.tilda_box.setText(_translate("PasswordGenerator", "Include tilda (~)"))
        self.forwardslash_box.setText(_translate("PasswordGenerator", "Include forward slash /"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(app.exec_())
