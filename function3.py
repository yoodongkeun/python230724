# function3.py

def union(*ar):
    result =[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))

g= lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

# 내장함수 필터
def getBiggerThan20(i):
    return i >20

lst = [10,25,30]
iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print(i)

print (" -----람다함수----")
iterL = filter(lambda x:x>20, lst)
for i in iterL:
    print(i)

