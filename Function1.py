#Function1.py

#함수를 정의
def setValue(newvalue):
    #함수 내부에서 초기화하면 지역변수
    x = newvalue
    print("함수내부:",x)
#함수 안에 있으면 지역변수 , 바깥은 전역변수
#함수를 호출
result = setValue(5)
print(result)

def swap(x,y):
    return y,x

result = swap(5,6)
print(result)
print(result[0],result[1])

#디버깅연습(교집합문자를 리턴)
def union(prelist, postlist):
    #교집합 문자를 저장하기 위한 지역 변수는 result
    result = []
    #↑교집합 글자를 저장하기 위한 리스트 형식 초기화
    for x in prelist:
    #H(0) | A(1) | M(2)    
        if x in postlist and x not in result:
        #x라는 글자가 postlist에 있고 x가 result에 없으면
        #append는 추가하기 위해 remove는 제거하기 위해
            result.append(x)
    return result

print( union("HAM","SPAM"))