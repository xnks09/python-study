# Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog' # 이것은 클래스 변수
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# 클래스 정보
print(Dog) # <class '__main__.Dog'>

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b)) # False 2428059680720 2428059679808

# 네임스페이스
print('dog1', a.__dict__) # dog1 {'name': 'mikky', 'age': 2}
print('dog2', b.__dict__) # dog2 {'name': 'baby', 'age': 3}    
    
# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age)) # mikky is 2 and baby is 3

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species) #클래스로도 바로 접근 가능
print(a.species) # 인스턴스로 접근
print(b.species) # 인스턴스로 접근

# 예제2
# self의 이해
class SelfTest:
    def func1(): #클래스 메소드이므로 바로 호출, 아무것도 매개변수가 없기 때문에
        print('Func1 called')
    def func2(self): # self가 붙은 것은 인스턴스 매소드 이므로, 인스턴스로 호출을 하던가 바로 호출시 인스턴스를 넘겨줘야 함
        print(id(self))
        print('Func2 called')


f = SelfTest()

# print(dir(f))

print(id(f))
# f.func1() # 예외발생
f.func2() #정상, 인스턴스를 호출하면 알아서 self가 넘어감
SelfTest.func1()
# SelfTest.func2() # 예외. self가 없음
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 
    stock_num = 0 # 재고
    
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1 #객체가 만들어질 때 1을 증가
    
    def __del__(self):
        Warehouse.stock_num -= 1 # 객체가 소멸될 때 1을 감소

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num) #2
# Warehouse.stock_num = 0.0094
print(user1.name) # Lee
print(user2.name) # Cho
print(user1.__dict__) # {'name': 'Lee'}
print(user2.__dict__) # {'name': 'Cho'}
print('before', Warehouse.__dict__) #before {'__module__': '__main__', 'stock_num': 2, '__init__': <function Warehouse.__init__ at 0x0000023553A1EF80>, '__del__': <function Warehouse.__del__ at 0x0000023553A1F010>, '__dict__': <attribute '__dict__' of 'Warehouse' objects>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None}
print('>>>', user1.stock_num) # >>> 2

del user1
print('after', Warehouse.__dict__) # after {'__module__': '__main__', 'stock_num': 1, '__init__': <function Warehouse.__init__ at 0x0000023553A1EF80>, '__del__': <function Warehouse.__del__ at 0x0000023553A1F010>, '__dict__': <attribute '__dict__' of 'Warehouse' objects>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None}

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
        
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))