# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kuklnakl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QComboBox, QPushButton, QHBoxLayout
import math
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 596)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 491, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.inputtext_field = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.inputtext_field.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputtext_field.setReadOnly(False)
        self.inputtext_field.setObjectName("inputtext_field")
        self.verticalLayout.addWidget(self.inputtext_field)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.outputcode_field = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.outputcode_field.setObjectName("outputcode_field")
        self.verticalLayout.addWidget(self.outputcode_field)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.outputdecode_field = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.outputdecode_field.setObjectName("outputdecode_field")
        self.verticalLayout.addWidget(self.outputdecode_field)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(510, 10, 271, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")


        self.sum_table = QtWidgets.QTableWidget()
        self.sum_table.setGeometry(QtCore.QRect(800, 10, 281, 431))
        self.sum_table.setRowCount(1)
        self.sum_table.setColumnCount(1)
        self.sum_table.setObjectName("sum_table")
        self.sum_table.setColumnWidth(0, 280)

        self.layoutbox = QtWidgets.QWidget(self.centralwidget)
        self.layoutbox.setGeometry(QtCore.QRect(800, 10, 281, 431))
        self.layoutbox.setObjectName("layoutbox")
        self.layout = QtWidgets.QHBoxLayout(self.layoutbox)
        self.layout.setObjectName("layout")
        self.layout.addWidget(self.sum_table)

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.reginput_box = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.reginput_box.setObjectName("reginput_box")
        self.gridLayout.addWidget(self.reginput_box, 0, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.suminput_box = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.suminput_box.setObjectName("suminput_box")
        self.gridLayout.addWidget(self.suminput_box, 1, 1, 1, 1)


        # self.sum_table.setItem(0, 0, QTableWidgetItem("smth"))


        # self.searchBtn = QPushButton("????????????????")
        # self.searchBtn.setDown(True)
        # self.searchBtn.setStyleSheet('QPushButton{margin:3px}')
        # self.sum_table.setCellWidget(0, 1, self.searchBtn)

        self.message_field = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_field.setGeometry(QtCore.QRect(515, 211, 271, 151))
        self.message_field.setObjectName("message_field")

        self.clean_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_button.setGeometry(QtCore.QRect(510, 470, 81, 71))
        self.clean_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clean_button.setObjectName("clean_button")

        self.test_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_button.setGeometry(QtCore.QRect(510, 390, 81, 71))
        self.test_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.test_button.setObjectName("test_button")

        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(600, 390, 81, 71))
        self.zero_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero_button.setObjectName("zero_button")

        self.main_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(600, 470, 171, 71))
        self.main_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_button.setObjectName("main_button")

        self.inputrezsum_button = QtWidgets.QPushButton(self.centralwidget)
        self.inputrezsum_button.setGeometry(QtCore.QRect(690, 390, 81, 71))
        self.inputrezsum_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inputrezsum_button.setObjectName("zero_button_3")

        # self.inputsum_field = QtWidgets.QLineEdit(self.centralwidget)
        # self.inputsum_field.setGeometry(QtCore.QRect(800, 420, 281, 41))
        # self.inputsum_field.setObjectName("inputsum_field")

        self.in_button = QtWidgets.QPushButton(self.centralwidget)
        self.in_button.setGeometry(QtCore.QRect(800, 470, 281, 71))
        self.in_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.in_button.setObjectName("in_button")

        self.sum_label = QtWidgets.QLabel(self.centralwidget)
        self.sum_label.setGeometry(QtCore.QRect(800, 390, 281, 21))
        self.sum_label.setText("")
        self.sum_label.setObjectName("sum_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.block_chek = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????????? ????????????????????"))
        self.label.setText(_translate("MainWindow", "?????????????? ??????????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????????????????? ??????????????????"))
        self.label_3.setText(_translate("MainWindow", "???????????????????????????? ??????????????????"))
        self.label_4.setText(_translate("MainWindow", "?????????????????????? ??????????????????"))
        self.label_5.setText(_translate("MainWindow", "?????????????????????? ????????????????????"))
        self.clean_button.setText(_translate("MainWindow", "??????????\n""??????????"))
        self.test_button.setText(_translate("MainWindow", "???????????????? \n""????????????????????"))
        self.zero_button.setText(_translate("MainWindow", "??????????\n""??????????"))
        self.main_button.setText(_translate("MainWindow", "??????????????????????????\n""????????????"))
        self.inputrezsum_button.setText(_translate("MainWindow", "???????????????? \n""?????????????????? \n""???????????????????? \n""????????????????????"))
        self.in_button.setText(_translate("MainWindow", "???????????? ??????-???? \n""???????????????????? ?? ??????????????????"))


    def clean(self):
        self.inputtext_field.setText("")
        self.reginput_box.setValue(0)
        self.suminput_box.setValue(0)
        self.sum_table.setRowCount(0)
        self.sum_table.setColumnCount(1)
        self.message_field.setText("")
        self.sum_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.block_chek = True
        return 0


    def test(self):
        self.inputtext_field.setText("?????????????? ?????????? ?????????????? ?? ?????? ???????????????? hsald97236l91yluoydls97zag7sp-9 [v-a9fd8gkcdgd0f7bv0as[d07cggdf")
        self.reginput_box.setValue(3)
        self.suminput_box.setValue(4)
        k = self.reginput_box.value()
        g = self.suminput_box.value()
        self.sum_table.setRowCount(g)
        self.sum_table.setColumnCount(1)
        # self.sum_table.setObjectName("sum_table")
        print(k)

        self.sum_table.setItem(0, 0, QTableWidgetItem("011"))
        self.sum_table.setItem(1, 0, QTableWidgetItem("110"))
        self.sum_table.setItem(2, 0, QTableWidgetItem("101"))
        self.sum_table.setItem(3, 0, QTableWidgetItem("111"))

        self.sum_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.get_data()

        self.layout.addWidget(self.sum_table)
        self.block_chek = True

        return 0


    def zero(self):
        self.inputtext_field.setText("")
        self.reginput_box.setValue(0)
        self.suminput_box.setValue(0)
        self.sum_table.setRowCount(0)
        self.sum_table.setColumnCount(1)
        self.message_field.setText("")
        self.sum_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.block_chek = True
        return 0


    def main(self):

        input_text = self.inputtext_field.toPlainText()
        code_text = ""
        output_text = ""
        reg_count = self.reginput_box.value()
        sum_count = self.suminput_box.value()

        reg_all_chek = False
        sum_count_chek = False
        sum_dif_chek = False
        sum_content_chek = False
        sum_dig_chek = True

        for i in range(self.sum_table.rowCount()):
            print(self.sum_table.item(i, 0).text())
            if bool(re.fullmatch('[01]+', self.sum_table.item(i, 0).text())) != True:
                print("?????? ????????")
                sum_dig_chek = False

        print("xnj-nj yt nj", sum_dig_chek)
        if sum_dig_chek:
            sum_mass = self.get_data()
            print("?????? ?????????? ", sum_mass)

            sum_content_chek = True
            for i in range(0, len(sum_mass), 1):
                if len(sum_mass[i]) != reg_count:
                    sum_content_chek = False
        else:
            self.message_field.append("??????????-???? ???? ???????????????????? ???????????????? ???????????????????????? ??????????????")


        # ???????????????????????????? ???????????? ?? ???????????????? ?????? (utf-8)
        def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
            bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
            return bits.zfill(8 * ((len(bits) + 7) // 8))

        # ???????????????????????????? ???????????????? ???????? (utf-8) ?? ????????????
        def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
            n = int(bits, 2)
            return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

        # ???????????????? ?????????? ?????????????? ?????? ?????????? i(x)*gi(x)
        def displacement(m, n):
            c = m.copy()
            for i in range(len(c) - 1, n - 1, -1):
                c[i] = c[i - n]
            for i in range(len(c) - (len(c) - n), 0, -1):
                c[i - 1] = 0
            return c

        # ?????????????????? ?????????? ???? ???????????? 2 ?????? i * gi
        def xorforc(m):
            c = []
            for i in range(0, len(m[0]), +1):
                x = m[0][i]
                for j in range(1, len(m), +1):
                    x = int(x) ^ int((m[j][i]))
                c.append(x)
            return c

        # ???????????????????? Ci
        def multip(i, gi):
            c = []
            for j in range(0, len(gi), +1):
                if gi[j] == 1:
                    x = i.copy()
                    x = displacement(x, j)
                    c.append(x)
            # print(c)
            c = xorforc(c)
            return c

        # Ci?????? ???????????????????????? ?? ??????
        def codding(m):
            c = []
            for i in range(0, len(m[0]), +1):
                for j in range(0, len(m), +1):
                    c.append(m[j][i])
            return c

        # ???????????? ?????????????? ?????????????????????? ???? ???????? ??????-???? ??????????????????, ?????????? ???????????????????? ?? ?????????? ?? ??????????
        def generalincod(k, g, inpb):
            i = inpb.copy()
            out = []

            print("????-???? ?????????????????? =", k, ", ???????????? ???????????????????? =", g, ", ?????????? ?? ?????????? =", i)

            for j in range(0, k, +1):
                i.append(0)

            for p in range(0, len(g), +1):
                for j in range(len(g[p]), len(i), +1):
                    g[p].append(0)

            for j in range(0, len(g), +1):
                # print(list(g[j]))
                out.append(multip(i, g[j]))
                print("c", j, "=", multip(i, g[j]))

            out = codding(out)
            print("???????????????????????????? ??????????: ", out)
            return out

        # ?????????????????? ??????????????????
        def summat(s, g):
            out = ""

            for i in range(0, len(g), 1):
                x = 0
                for j in range(0, len(g[i]), 1):
                    if g[i][j] == 1:
                        x = x ^ int(s[j])
                        # print(x, i, j, int(s[j]), g[i][j], x ^ int(s[j]))
                out = out + str(x)

            return out

        # ???????????????? ???????????? ?????????? ???????????????????? ?????????????????? ?? ?????????????????? ??????????????????
        def hell(k, g):
            mass = []  # mass[i] = [???????????????? ??????????????????],[???????????????? ????????????????????],[?????????????????????? ??????],[?????????????????? k-1 ????????????????],[???????????? k-1 ????????????????]

            for i in range(0, 2 ** k, 1):
                a = format(i, 'b').rjust(k, '0')
                mass.append([a, summat(a, g), a[0], a[1:], a[:-1]])

            print("?????????????? ????????????")
            for i in range(0, 2 ** k, 1):
                print(mass[i])

            return mass

        # ???????????? ?????????????? ?????????????????????????? ???? ???????? ???????????????????????????? ???????????? ?? ??????????, ??????-???? ???????????????????? ?? ?????????????? ????????????
        def generaldecod(s, gcount, tab, k):
            out = ""
            chek = "0" * (k - 1)
            for i in range(0, len(s), gcount):
                buf = ""
                for k in range(0, gcount, 1):
                    buf = buf + str(s[i + k])
                # print(buf)
                for j in range(0, len(tab), 1):
                    if buf == tab[j][1] and chek == tab[j][3]:
                        out += tab[j][2]
                        chek = tab[j][4]
                        # print("chek=", chek, 'mimiout=', out, "postupilo", tab[j][2])
                        break
            print('??????????', out)
            return out


        # ???????????????????????? ?????????????????????? ???????????????????? ???? k ????????????????
        def exeptioncount(g, k):
            chek = False
            max = 0

            for i in range(k, 0, -1):
                max += (math.factorial(k)) / ((math.factorial(i)) * (math.factorial(k - i)))
            if max > g:
                chek = True

            return chek

        # ?????? ?????????????????? ????????????????
        def exeptiondiffer(m):
            g = m.copy()
            chek = True
            for i in range(0, len(g), +1):
                g[i] = "".join(map(str, g[i]))
            for i in range(0, len(g), +1):
                for j in range(i + 1, len(g), +1):
                    if g[i] == g[j]:
                        chek = False
                        break
            return chek

        # ?????? ???????????????? ????????????????????????
        def exeptionalluse(m, k):
            g = m.copy()
            chek = False
            c = []
            for i in range(0, k, +1):
                x = g[0][i]
                for j in range(1, len(g), +1):
                    x = int(x) | int((g[j][i]))
                c.append(x)
            a = "".join(map(str, c))
            b = "".join(['1'] * k)
            if a == b:
                chek = True
            return chek

        if sum_content_chek:
            reg_all_chek = exeptionalluse(sum_mass, reg_count)
            sum_dif_chek = exeptiondiffer(sum_mass)
            sum_count_chek = exeptioncount(sum_count, reg_count)

        print("?????? ?? ??????????????", sum_content_chek , sum_dif_chek , sum_count_chek , reg_all_chek)

        if sum_content_chek and sum_dif_chek and sum_count_chek and reg_all_chek:
            print(input_text, code_text, output_text, reg_count, sum_count, sum_mass)

            input_text = list(text_to_bits(input_text))
            print(input_text)
            code_text = generalincod(reg_count, sum_mass, input_text)
            print(code_text)
            code_text = "".join(map(str, code_text))
            print(code_text)
            self.outputcode_field.setText(code_text)
            output_text = generaldecod(code_text, sum_count, hell(reg_count, sum_mass), reg_count)
            print(output_text)
            print(type(output_text))
            output_text_end = text_from_bits(output_text[:-reg_count])
            print(output_text_end)
            self.outputdecode_field.setText(output_text_end)
        else:
            self.outputcode_field.setText("")
            self.outputdecode_field.setText("")
            self.message_field.setText("")
            if sum_content_chek == True:
                if sum_dif_chek == False:
                    self.message_field.append("??????????-???? ?????????????????? ???? ????????????????")
                if sum_count_chek == False:
                    self.message_field.append("??????-???? ???????????????????? ?????????????????? ?????????????????????????? ?????????????????? ?????? ?????????????? ????-???? ??????????????????")
                if reg_all_chek == False:
                    self.message_field.append("???? ?????? ???????????????? ?????????????????????????? ?? ????????????????????")
            else:
                self.message_field.append("??????????-???? ???? ???????????????????? ???????????????? ???????????????????????? ??????????????")
        return 0


    def inputrezsum(self):
        k = self.reginput_box.value()
        #mass = self.get_data()
        #print("?????? ?????????? ", mass)
        main_local_chek = True
        for i in range(self.sum_table.rowCount()):
            print(self.sum_table.item(i, 0).text())
            if bool(re.fullmatch('[01]+', self.sum_table.item(i, 0).text())) != True:
                print("?????? ????????")
                main_local_chek = False

        print(main_local_chek)
        if main_local_chek:
            mass = self.get_data()
            print("?????? ?????????? ", mass)

            local_check = False
            for i in range(0, len(mass), 1):
                if len(mass[i]) != k:
                    local_check = True

            if local_check == True:
                self.message_field.setText("???????????? ????????????-???? ???? ???????????????????? ?????????????????? ??????-???? ??????????????????")

            print(self.block_chek)
            if (self.block_chek == False):
                print("??????????????????")
                self.sum_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.block_chek = True
            else:
                print("???? ??????????????????")
                self.sum_table.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
                self.block_chek = False
        else:
            self.message_field.setText("??????????-???? ???? ???????????????????? ???????????????? ???????????????????????? ??????????????")
        return 0


    def input(self):
        print('kakoem')
        k = self.reginput_box.value()
        g = self.suminput_box.value()

        self.sum_table.setRowCount(g)
        self.sum_table.setColumnCount(1)

        print(k)
        for x in range(0, g, 1):
            self.sum_table.setItem(int(x), 0, QTableWidgetItem("0"*k))
            print(k)


        #self.get_data()

        self.layout.addWidget(self.sum_table)
        self.sum_table.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.block_chek = False
        # self.layout.replaceWidget(self.sum_table, self.sum_table)
        return 0

    massofsum = []

    def get_data(self):
        self.massofsum = []
        for i in range(self.sum_table.rowCount()):
            self.massofsum.append(self.sum_table.item(i, 0).text())
            print(self.sum_table.item(i, 0).text())
        for i in range(len(self.massofsum)):
            self.massofsum[i] = list(map(int, list(self.massofsum[i])))
        print("xexvtrb", self.massofsum)
        return self.massofsum

    def add_functions(self):
        self.clean_button.clicked.connect(self.clean)
        self.test_button.clicked.connect(self.test)
        self.zero_button.clicked.connect(self.zero)
        self.main_button.clicked.connect(self.main)
        self.inputrezsum_button.clicked.connect(self.inputrezsum)
        self.in_button.clicked.connect(self.input)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

