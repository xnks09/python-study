# Chapter03-6
# 집합(Sets) 특징
# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} #키가 없는 상태로 원소만 나열한다면 set으로 인식(딕셔너리는 키와 밸류가 들어간 형태)
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t) # <class 'tuple'> (1, 2, 3, 4)
print('t - ', t[0], t[1:3]) #  1 (2, 3)


# 리스트 변환
l = list(c)
l2 = list(e)
print('l - ', type(l), l) # <class 'list'> [1, 4, 5, 6]
print('l - ', l[0], l[1:3]) # 1 [4, 5]
print('l2 - ', type(l2), l2) # <class 'list'> ['bar', 'baz', 'qux', 'foo']

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('l - ', s1 & s2) # {4, 5, 6} 교집합
print('l - ', s1.intersection(s2)) # {4, 5, 6}

print('l - ', s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9} 합집합
print('l - ', s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print('l - ', s1 - s2) # {1, 2, 3} 차집합
print('l - ', s1.difference(s2)) # {1, 2, 3}

# 중복 원소 확인
print('l - ', s1.isdisjoint(s2)) # false, false가 나오면 교집합이 있다는 의미임

# 부분 집합 확인
print('subset - ', s1.issubset(s2))
print('superset - ', s1.issuperset(s2))


# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2) # 없는 원소를 삭제하려면 에러가 발생함, 따라서 먼저 있는지 체크하는 코드가 필요함
print('s1 - ', s1)
# s1.remove(7)

s1.discard(3)
print('s1 - ', s1)

#s1.discard(7)

# 모두 제거
s1.clear()