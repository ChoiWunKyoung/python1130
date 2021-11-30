# DemoLoop3.py

lst = [1,2,3,4,5,6,7,8,9,10]
print("---break---")
for i in lst:
    if i>5:
        break
    print("Item:{0}".format(i))

print("---continue---")
for i in lst:
    if i%2==0:
        continue
    print("Item:{0}".format(i))

print("---수열함수---")
result = list(range(1,11))
print(result)

for i in range(1,5):
    print(i)


lst = list(range(1,11))
for i in lst:
    if i > 5 :
        print(i**2)
#ctrl + / : 다중라인 주석 처리
#위에 코드 한줄로 하려면 이렇게!
# result2 = [i**2 for i in lst if i>5]
# print(result2)

tp = ("apple","kiwi","orange")
print([len(i) for i in tp])

d={100:"apple",200:"orange",300:"kiwi"}
print([v.upper() for v in d.values()])