# DemoRE.py
import re

# 숮자가 0에서 n번th
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

# ctrl + / 선택한 블럭주석처리

result = re.search("apple", "빅테크에서 apple의 위상")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")
print(result.group())
result = re.search("\d{5}", "우리동네는 42300")
print(result.group())

print("---대소문자----")
data = "Apple is big company and apple is very delicious"
c = re.compile("apple", re.IGNORECASE)
print(c.findall(data))

print("----다중라인검색------")
data2 = """파이썬을 
배워서

누구나 사용"""
c = re.compile("^.+", re.MULTILINE)
print(c.findall(data2))