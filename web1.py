# web1.py
#크롤링을 하기 위한 선언
from bs4 import BeautifulSoup

#페이지를 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한객체 생성
soup = BeautifulSoup(page, "html.parser")
#페이지 보기
#print(soup.prettify())
#<p> 전체를 검색
#print(soup.find_all("p"))
#<p> 하나를 검색
#print(soup.find('p'))
#<p class='outer=text'> 조건검색
#print(soup.find_all("p", class_='outer-text'))
#attrs:Attribues(속성들)
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#id=first
#print(soup.find_all(id="first"))
#태그 내부 문자열 가져오기(.text속성)
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)