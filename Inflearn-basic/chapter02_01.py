# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# 기본 출력
print('Python Start!') 
print("Python Start!") 
print("""Python Start!""")
print('''Python Start!''')

print()

# separator 옵션 사용
print('P', 'Y', 'T', 'H','O','N', sep='')
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션 사용
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용(d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

# %s
print('%10s' % ('nice',)) #10자리를 맞춰서 보여줌
print('{:>10}'.format('nice')) #공백을 왼쪽부터 채움

print('%-10s' % ('nice',)) #공백을 오른쪽에서 채움
print('{:10}'.format('nice')) #공백을 오른쪽부터 채움

print('{:_<10}'.format('nice'))
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('pythonstudy',)) # 5글자만 보여줌
print('{:.5}'.format('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42,))
print('{:4d}'.format(42))

# %f
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))