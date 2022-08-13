# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서O, 중복O, 수정X,삭제X) 불변

# 선언
a = ()
b = (1,) # 2개일 경우는 관계없지만, 1개만 있을 경우 마지막은 쉼표(,)가 와야지 튜플로 인식
c = (11,12,13,14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d - ', type(d), d) # <class 'tuple'> (100, 1000, 'Ace', 'Base', 'Captine')
print('d - ', d[1]) # 1000
print('d - ', d[0] + d[1] + d[1]) #2100
print('d - ', d[-1]) # Captine
print('e - ', e[-1][1]) # Base

# list로 형변환하는 순간 list와 동일하게 순서, 중복, 수정, 삭제가 모두 가능한 속성으로 변경됨
print('e - ', list(e[-1][1])) # ['B', 'a', 's', 'e']

# 수정 X
# d[0] = 1500
# print('d - ', d)

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3]) # (100, 1000, 'Ace')
print('d - ', d[2:]) # ('Ace', 'Base', 'Captine')
print('e - ', e[2][1:3]) #('Base', 'Captine')

# 튜플 연산
print('>>>>>')
print('c + d - ', c + d) # (11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'Captine')
print('c * 3 - ', c * 3) # (11, 12, 13, 14, 11, 12, 13, 14, 11, 12, 13, 14)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5)) # 0
print('a - ', a.count(4)) # 1

# 팩킹 & 언팩킹(Packing, and Unpacking)
# 괄호가 없어도 팩킹 및 언팩킹 가능

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(t) # ('foo', 'bar', 'baz', 'qux')
print(t[0]) # foo
print(t[-1]) # qux

# 언팩킹1
(x1, x2, x3, x4) = t

# 출력확인
print(x1) # foo
print(x2) # bar
print(x3) # baz
print(x4) # qux

# 언팩킹2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(x1)
print(x2)
print(x3)
print(x4)

# 팩킹 & 언팩킹
t2  =1, 2, 3
t3 = 4, 
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6 #언팩

# 출력 확인
print(t2) # (1, 2, 3)
print(t3) # (4,)
print(x1,x2,x3) # 1 2 3
print(x4,x5,x6) #4 5 6


# tuple(튜플)은 불변한 순서가 있는 객체의 집합입니다.
#list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없습니다.
#REPL에서 확인해봅니다.

#list와 마찬가지로 다양한 타입이 함께 포함될 수 있습니다.