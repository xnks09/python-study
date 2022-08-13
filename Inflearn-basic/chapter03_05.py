# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
e =  dict([
	 ( 'Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])

f =  dict(
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(c), e)
print('f - ', type(c), f)

# 출력
print('a - ', a['name'])  # 결과: Kim, 존재X -> 에러 발생
print('a - ', a.get('name'))  # 결과: Kim, 존재X -> None 처리, 그래서 get을 많이 쓴다.
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))

# 딕셔너리 추가
a['address'] = 'seoul' # 기존에 키가 중복으로 존재했으면, 덮어씀
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(d))
print(len(e))

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print('a - ', a.keys()) # 결과 : dict_keys(['name', 'phone', 'birth', 'address', 'rank'])
print('b - ', b.keys()) # 결과 : dict_keys([0])
print('c - ', c.keys()) # 결과 : dict_keys(['arr'])
print('d - ', d.keys()) # 결과 : dict_keys(['Name', 'City', 'Age', 'Grade', 'Status'])

print('a - ', list(a.keys())) # 결과 : ['name', 'phone', 'birth', 'address', 'rank']
print('b - ', list(b.keys())) # 결과 : [0]
print('c - ', list(c.keys())) # 결과 : ['arr']
print('d - ', list(d.keys())) # 결과 : ['Name', 'City', 'Age', 'Grade', 'Status']

print('a - ', a.values()) # 결과 : dict_values(['Kim', '01012345678', '870124', 'seoul', [1, 2, 3]])
print('b - ', b.values()) # 결과 : dict_values(['Hello python!'])
print('c - ', c.values()) # 결과 : dict_values([[1, 2, 3, 4]])
print('d - ', d.values()) # 결과 : dict_values(['Niceman', 'Seoul', '33', 'A', True])

print('a - ', list(a.values())) # 결과 : ['Kim', '01012345678', '870124', 'seoul', [1, 2, 3]]
print('b - ', list(b.values())) # 결과 : ['Hello python!']
print('c - ', list(c.values())) # 결과 : [[1, 2, 3, 4]]
print('d - ', list(d.values())) # 결과 : ['Niceman', 'Seoul', '33', 'A', True]

print('a - ', a.items()) # 결과 : dict_items([('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', [1, 2, 3])])
print('b - ', b.items()) # 결과 : dict_items([(0, 'Hello python!')])
print('c - ', c.items()) # 결과 : dict_items([('arr', [1, 2, 3, 4])])
print('d - ', d.items()) # 결과 : dict_items([('Name', 'Niceman'), ('City', 'Seoul'), ('Age', '33'), ('Grade', 'A'), ('Status', True)])

print('a - ', list(a.items())) # 결과 : [('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', [1, 2, 3])]
print('b - ', list(b.items())) # 결과 : [(0, 'Hello python!')]
print('c - ', list(c.items())) # 결과 : [('arr', [1, 2, 3, 4])]
print('d - ', list(d.items())) # 결과 : [('Name', 'Niceman'), ('City', 'Seoul'), ('Age', '33'), ('Grade', 'A'), ('Status', True)]

print('a - ', a.pop('name')) # 결과 : Kim
print('b - ', b.pop(0)) # 결과 : Hello python!
print('c - ', c.pop('arr')) # 결과 : [1, 2, 3, 4]
print('d - ', d.pop('City')) # 결과 : Seoul

print('f - ', f.popitem()) # 결과 : ('Status', True)
print('f - ', f.popitem()) # 결과 : ('Grade', 'A')
print('f - ', f.popitem()) # 결과 : ('Age', '33')
print('f - ', f.popitem()) # 결과 : ('City', 'Seoul')
print('f - ', f.popitem()) # 결과 : ('Name', 'Niceman')
# 예외
# print('f - ', f.popitem())

print('a - ', 'name' in a) # 결과 : false, name이라는 키가 있나라는 의미
print('a - ', 'addr' in a) # addr이라는 키가 있나라는 의미

# 수정
f.update(Age=36)

temp = {'Age': 27}

print('f - ', f)

f.update(temp)

print('f - ', f)
