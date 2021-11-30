#Function3.py
#함수의 기본값이 있는 경우
def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))
print(times(5,))
print(times(b=5))

#키워드 인자 방식으로 전달한다.
def userURL(server,port):
    strURL = "http://" + server + ":" + port
    return strURL
#호출
print(userURL("credu.com","80"))
print(userURL(port="8080",server="credu.com"))

#가변인자는 입력되는 인자의 갯수가 가변적인 경우
#인자에 *를 붙이면 가변인자(내부에서 Tuple)
def union(*ar):
    #지역변수 리스트 초기화
    result =[]
    #HAM(0)|EGG(1) 가변인자 
    for item in ar:
        #H(0) | A(1) | M(2)
        #E(0) | G(1) | G(2)
        for x in item:
            if x not in result:
            #result에 포함되지 않을 경우
                result.append(x)
    return result

print( union("HAM","EGG"))
print( union("HAM","EGG","SPAM"))

#정의되지 않은 인자 처리(필수,옵션도 섞여 있는 경우)
#내부에서 딕셔너리(dict)
def userURIBuilder(server,port,**user):
    strURL = "http://" +server + ":" +port +"/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&" 
    return strURL[:-1]

print(userURIBuilder("naver.com","80",id="kim",pasword="1234"))
print(userURIBuilder("naver.com","80",id="kim",pasword="1234",name="mike",age="30"))

#람다 함수(간단하게 함수를 정의,익명함수)
g = lambda x,y:x*y
print(g(3,4))
