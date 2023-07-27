#web2.py
import requests

from bs4 import BeautifulSoup

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
# <div class="card-desc">
#       <h2 class="card-title">먹태깡 60봉</h2>
#       <div class="card-price ">
#         1,500원
#       </div>
#       <div class="card-region-name">
#         경기도 김포시 장기동
#       </div>
     