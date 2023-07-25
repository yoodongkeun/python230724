# function2.py
x=1
def func(a):
    return a+x
print(func(1))

def func2(a):
    x=5
    return a+x
print(func2(1))


def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURI = "http://" +server + ":" + port
    return strURI

print(connectURI("credu.com", "80"))
print(connectURI(port="8080", server='credu_com'))


