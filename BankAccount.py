# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화메서드
    def __init__(self, id, name, balance):
        #인스턴스 멤버 변수
        # self.id = id
        # self.name = name 
        # self.balance = balance
        #언더바 2개 붙이면 이름을 숨김
        self.__id = id
        self.__name = name 
        self.__balance = balance
    #입금 메서드 
    def deposit(self, amount):
        self.__balance += amount
    #출금 메서드     
    def withdraw(self, amount):
        self.__balance -= amount
    #문자열을 출력하는 메서드(ToString())    
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1._BankAccount__balance)
print(account1)



