# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1]) #결과 : 10000
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1]) # 결과 : Base
print('e - ', list(e[-1][1])) # 결과 : ['B', 'a', 's', 'e']

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3]) # 결과 : [1000, 10000, 'Ace']
print('d - ', d[2:])  # 결과 : ['Ace', 'Base', 'Captine']
print('e - ', e[2][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d - ', c + d) # 결과(list+list) : [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captine']
print('c * 3 - ', c * 3) # 결과 : [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])

# 같은 id 값
temp = c
print(c == temp)


# 리스트 수정, 삭제
print('>>>>>> 리스트 수정, 삭제')
c[0] = 4 # 결과 : [4, 75, 80, 85]
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c) # 결과 : [4, 'c', 80]

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()   # 결과 : [1, 2, 3, 4, 5, 6]
print('a - ', a)
a.reverse()  # 결과 : [6, 5, 4, 3, 2, 1]
print('a - ', a) 
print('a - ', a.index(5)) # 결과 : 1
a.insert(2, 7) # 결과 : [6, 5, 7, 4, 3, 2, 1]
print('a - ', a)
a.reverse()
a.remove(1) # 제거할 값을 넣는 것임
print('a - ', a)
print('a - pop', a.pop()) # 결과 : 6, 마지막 요소를 보여주고 원본에서 지움
print('a - pop', a.pop()) # 결과 : 5, 마지막 요소를 보여주고 원본에서 지움
print('a - ', a)
print('a - ', a.count(4)) # 결과 : 1, 4의 갯수가 1개 있다.
ex = [8, 9]
a.extend(ex) # 결과 : [2, 3, 4, 7, 8, 9]
print('a - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)