# 클래스메서드.py
#부모클래스
class CoeffVar(object):
    coefficient = 1 
    @classmethod
    #cls 는 클래스 참조가 넘어오는 것
    def mul(cls, fact):
        return cls.coefficient * fact 

#자식클래스
#파생형식을 정의
class MulFive(CoeffVar):
    coefficient = 5 

#파이썬은 다 퍼블릭 변수 
x = MulFive.mul(4)
print(x)


