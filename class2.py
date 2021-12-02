# class2.py

#1)클래스 형식을 정의(원본)
class Person:
    #클래스에 소속된 데이터 공유하는 멤버변수
    num_person = 0
    #_언더바 2개
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성(복사본),객체(object)
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 갯수 : {0}" . format(Person.num_person))

p1.age = 30
print(p1.age)
#print(p2.age)