# DemoFile.py
for i in range(0,10):
    url = "http://www.credu.com/?page="+str(1)
    print(url)

# -----오른쪽 정렬---------
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))
#-------- 0으로 채우기--------
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(5))

print("----서식지정-----")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(1500000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일쓰기
f= open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번재\n두번째\n세번째\n")
f.close()

f= open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read()
f.close()
print(result)
