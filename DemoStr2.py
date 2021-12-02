#DemoStr2.py
#정규표현식

import re

string = "<<< data << data2"
#서브스트링 ("패턴","",데이터)
result = re.sub("<<<","",string)
print(result)

#특정 문자열 패턴:숫자가 0번에서 N번 th
result = re.match("[0-9]*th","35th")
result2 = re.search("[0-9]*th","35th")
print(result)
print(result2)
#약간 가공
print(result.group())

print("---함정 추가---")
#함정을 추가
#특정한 규칙을 정의(패턴)
#match는 정확하게 일치
result = re.match("[0-9]*th","   35th")
#search는 내부에 있으면
result2 = re.search("[0-9]*th","   35th")

print(result)
print(result2)


#년도를 검색
result = re.match("\d{4}","올해는 2021년입니다.")
#search는 내부에 있으면
result2 = re.search("\d{4}","올해는 2021년입니다.")
print(result)
print(result2)

#우편번호를 검색
result = re.search("\d{5}","우리 동네는 52300입니다.")
print(result.group())