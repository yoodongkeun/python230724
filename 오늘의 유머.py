# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 베스트 게시판 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #간혹한글이 깨지는 경우
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
#<td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=469720&amp;s_no=469720&amp;page=1" target="_top"> EBS : "탄수화물 해로우니 먹지마!!"</a><span class="list_memo_count_span"> [29]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span><img src="http://www.todayhumor.co.kr/board/images/list_icon_shovel.gif?2" alt="펌글" style="margin-right:3px;top:2px;position:relative"> <span style="color:#999">3일</span></td>
#<a href="/board/view.php?table=bestofbest&amp;no=469720&amp;s_no=469720&amp;page=1" target="_top"> EBS : "탄수화물 해로우니 먹지마!!"</a>


        for item in list:
                try:
                        title = item.find("a").text
                        # href = item.find("a")["href"]
                        # print(title.strip())
                        # print(href.strip())
                        if (re.search('한국', title)):
                                print(title.strip())                         
                except:
                        pass
        
