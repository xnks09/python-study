import sys
import inspect
# from ..sub2 import module2

# module2.py
def mod1_test1():
	print ("Module1 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe())) #이 파일의 위치 경로를 호출해주는 method

def mod1_test2():
	print ("Module1 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))