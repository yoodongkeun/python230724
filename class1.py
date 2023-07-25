# class1.py
# 1) 클래스 형식 정의
class Person:
    # 초기화메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

# 2)인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.print()
p2.print()

# 런타임시에 변수 추가 -- (1.인스턴스 2.클래스 3.전역변수 순으로 찾음)
#print("숫자:{0}".format(Person.num_person))
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)