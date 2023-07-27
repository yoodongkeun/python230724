# DemoForm2.py
# DemoForm2.ui(화면단) + # DemoForm2.py (로직단)

import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

import requests
from bs4 import BeautifulSoup


#디자인된 문서 로딩(시그널+슬롯)
form_class = uic.loadUiType("DemoForm2.ui")[0]
#폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
    #슬롯매서드
    def firstClick(self):       
        url = "https://www.daangn.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class": "card-desc"})
        #파일에 저장
        f = open("c:\\work\\daangn.txt", "wt", encoding="utf-8")
        for post in posts:
            title = post.find("h2", attrs={"class": "card-title"})
            price = post.find("div", attrs={"class": "card-price"})
            addr = post.find("div", attrs={"class":"card-region-name"})
            title = title.text.replace("\n","")
            price = price.text.replace("\n","")
            addr = addr.text.replace("\n","")
            print("{0},{1},{2}".format(title, price, addr)) 
            f.write(f"{title}, {price}, {addr}\n")
        f.close()
        self.label.setText("당근마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")
#직접 모듈을 실행했는지 체크(진입점)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()