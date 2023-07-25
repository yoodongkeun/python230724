class MyClass:
    def __init__(self, value):
        self.Value = value 
        print("Class is created! Value = ", value)
    # 소멸다 메서드    
    def __del__(self):
        print("Instatance is deleted!")
        

c = MyClass(10)

# 언젠가 가비지 컬렉션
del c 


del c_copy
