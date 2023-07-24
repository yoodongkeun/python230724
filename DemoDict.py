# DemoDict.py
device = {"아이폰":5, "갤럭시":10, "윈도우":30}

print(device["아이폰"])

device["맥북"]= 15
print(device)

device["아이폰"]=6
print(device)

for item in device.items():
    print(item)

for key in device.keys():
    print(key)

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone.values())
print("kim" in phone)
print( "kang" not in phone)

p = phone
print(p)
print(id(phone), id(p))

isRight = True

print( True or True or False)