# Defexample.py

def setValue(newValue):
    x= newValue
    print("지역변수:", x)

result = setValue(5)
print(result)

def swap(x,y):
    return y,x

print(swap(3,4))

def intersect(prelist, postlist):
    result =[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)

    return result

print(intersect("HAM", "SPAM"))