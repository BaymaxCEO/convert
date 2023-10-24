import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_interface import Ui_MainWindow
from music import *
from collections import Counter

class testwindow(QtWidgets.QMainWindow,Ui_MainWindow): 
    def __init__(self):
        super(testwindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("简谱转笛谱")
        # 自定义槽函数，获取列表选中项的值
        self.selected_item = "陶笛"
        self.check_num = True
        self.listWidget.itemClicked['QListWidgetItem*'].connect(self.dixing_selection_changed)
        self.selected_value = 0
        self.spinBox.valueChanged.connect(self.value_changed)

        self.dic = {}
        for i in range(1, 8): 
            self.dic[str(i)] = i
            self.dic['.'+str(i)] = i-7
            self.dic[str(i)+'.'] = i+7

        self.text = ""
        self.update_textBrowser()
        # self.textEdit.setText(self.text)

        self.pushButton_d1.clicked.connect(self.d1_input)
        self.pushButton_d2.clicked.connect(self.d2_input)
        self.pushButton_d3.clicked.connect(self.d3_input)
        self.pushButton_d4.clicked.connect(self.d4_input)
        self.pushButton_d5.clicked.connect(self.d5_input)
        self.pushButton_d6.clicked.connect(self.d6_input)
        self.pushButton_d7.clicked.connect(self.d7_input)

        self.pushButton_m1.clicked.connect(self.m1_input)
        self.pushButton_m2.clicked.connect(self.m2_input)
        self.pushButton_m3.clicked.connect(self.m3_input)
        self.pushButton_m4.clicked.connect(self.m4_input)
        self.pushButton_m5.clicked.connect(self.m5_input)
        self.pushButton_m6.clicked.connect(self.m6_input)
        self.pushButton_m7.clicked.connect(self.m7_input)

        self.pushButton_h1.clicked.connect(self.h1_input)
        self.pushButton_h2.clicked.connect(self.h2_input)
        self.pushButton_h3.clicked.connect(self.h3_input)
        self.pushButton_h4.clicked.connect(self.h4_input)
        self.pushButton_h5.clicked.connect(self.h5_input)
        self.pushButton_h6.clicked.connect(self.h6_input)
        self.pushButton_h7.clicked.connect(self.h7_input)

        self.textEdit.textChanged.connect(self.onTextChanged)
        self.pushButton_next.clicked.connect(self.next_row)
        self.pushButton_upload.clicked.connect(self.upload)
        self.pushButton_back.clicked.connect(self.back)

        self.result = ""
        self.tests = [" ", "\n"]
        self.max, self.min = "1", "1"

    def back(self): 
        if self.text != "": 
            while self.text[-1] in self.tests: 
                self.text = self.text[:-1]
            self.text = self.text[:-1]
            self.textEdit.setText(self.text)
        else: self.max, self.min = "1", "1"

    def next_row(self): 
        self.text += "\n"
        self.textEdit.setText(self.text)

    def upload(self): 
        if self.check_num is True and self.selected_value >= self.min_key and self.selected_value <= self.max_key: 
            if self.selected_item == "陶笛": 
                self.result = func_td(self.text, self.selected_value, dic_td)
            if self.selected_item == "哨笛": 
                self.result = func(self.text, self.selected_value, dic)
            self.textBrowser_2.setText(self.result)
        else: 
            self.textBrowser_2.setText("输入有错，无法提交")

    def update_textBrowser(self): 
        self.check_num = self.check()
        if self.check_num is True: 
            ss = self.compute_suggest()
            show_text = "笛谱: "+self.selected_item+"\t"+"当前升key: "+str(self.selected_value)+"\n当前音域: "+self.min+"-"+self.max + ss
        else: 
            show_text = "笛谱: "+self.selected_item+"\t"+"当前升key: "+str(self.selected_value)+"\n当前输入有问题"
        self.textBrowser.setText(show_text)

    def compute_suggest(self): 
        if self.selected_item == "陶笛": 
            # if self.dic[self.max] - self.dic[self.min] > 10: 
            if self.dic[self.max] - self.dic[self.min] > 11: 
                ss = "\n音域跨度太大"
            else: 
                # left = self.dic[self.min] - self.dic["1"]
                # right = self.dic[self.max] - self.dic["7."]
                # self.min_key = self.dic[".3"] - self.dic[self.min]
                # self.max_key = self.dic["3."] - self.dic[self.max]
                self.min_key = 1 - self.dic[self.min]
                # self.max_key = 11 - self.dic[self.max]
                self.max_key = 12 - self.dic[self.max]
                # self.min_key = min(left, right)
                # self.max_key = max(left, right)
                # self.max_key = self.dic[".3"] + (10 - (self.dic[self.max] - self.dic[self.min]))
                # self.max_key = self.min_key + (10 - (self.dic[self.max] - self.dic[self.min]))
                # ss = "\n建议升key: "+"最低: "+str(self.min_key)+"\t最高: "+str(self.max_key)
                ss = "\n建议升key: "+"最低: "+str(self.min_key)+"\t最高: "+str(self.max_key)


        if self.selected_item == "哨笛": 
            if self.dic[self.max] - self.dic[self.min] > 15: 
                ss = "\n音域跨度太大"
            else: 
                # left = self.dic[self.min] - self.dic[".3"]
                # right = self.dic[self.max] - self.dic["3."]
                # self.min_key = self.dic["1"] - self.dic[self.min]
                # self.max_key = self.dic["7."] - self.dic[self.max]
                self.min_key = 1 - self.dic[self.min]
                self.max_key = 15 - self.dic[self.max]
                # self.min_key = min(left, right)
                # self.max_key = max(left, right)
                # self.max_key = self.dic["1."] + (15 - (self.dic[self.max] - self.dic[self.min]))
                # self.max_key = self.min_key + (15 - (self.dic[self.max] - self.dic[self.min]))
                # ss = "\n建议升key: "+"最低: "+str(self.min_key)+"\t最高: "+str(self.max_key)
                ss = "\n建议升key: "+"最低: "+str(self.min_key)+"\t最高: "+str(self.max_key)

        return ss


    def dixing_selection_changed(self): 
        # 获取当前选中项目的文本
        self.selected_item = self.listWidget.currentItem().text()
        self.update_textBrowser()

    def value_changed(self): 
        # 获取当前选中项目的文本
        self.selected_value = self.spinBox.value()
        self.update_textBrowser()

    def onTextChanged(self): 
        self.text = self.textEdit.toPlainText()
        self.update_textBrowser()
        # print(self.text)

    def check(self): 
        # 需要知道当前text中字符的最高和最小
        ss = self.text.replace("\n", " ")
        ss_list = ss.split(" ")
        ss_list = [x for x in ss_list if x != "" and x != "."]
        count_result = dict(Counter(ss_list))
        # max_key, min_key = "1", "1"
        max_key, min_key = "1", "1"
        if len(ss_list) > 0: 
            # print(ss_list)
            max_key = list(count_result.keys())[0]
            min_key = max_key
            for key in count_result.keys(): 
                if key not in self.dic.keys(): 
                    return False
                if self.dic[key] < self.dic[min_key]: 
                    min_key = key
                if self.dic[key] > self.dic[max_key]: 
                    max_key = key
        self.max, self.min = max_key, min_key
        return True


    def d1_input(self): 
        self.text += ".1 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def d2_input(self): 
        self.text += ".2 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def d3_input(self): 
        self.text += ".3 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def d4_input(self): 
        self.text += ".4 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def d5_input(self): 
        self.text += ".5 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def d6_input(self): 
        self.text += ".6 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def d7_input(self): 
        self.text += ".7 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def m1_input(self): 
        self.text += "1 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def m2_input(self): 
        self.text += "2 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def m3_input(self): 
        self.text += "3 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def m4_input(self): 
        self.text += "4 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def m5_input(self): 
        self.text += "5 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def m6_input(self): 
        self.text += "6 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def m7_input(self): 
        self.text += "7 "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def h1_input(self): 
        self.text += "1. "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def h2_input(self): 
        self.text += "2. "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def h3_input(self): 
        self.text += "3. "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def h4_input(self): 
        self.text += "4. "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def h5_input(self): 
        self.text += "5. "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def h6_input(self): 
        self.text += "6. "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

    def h7_input(self): 
        self.text += "7. "
        self.textEdit.setText(self.text)
        self.update_textBrowser()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = testwindow()
    window.show()
    sys.exit(app.exec_())