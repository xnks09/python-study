from operator import truediv
import sys
import io
import time
import collector
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('이제 일을 시작하려구나~♥')
print('내가 자동으로 해줄게~')
print('자 밑에 보고 선택해줘~')
print()
print('==================================')
print('수집을 하고 싶다 숫자 1 넣고 엔터!')
print('등록을 하고 싶다 숫자 2 넣고 엔터!')
print('==================================')

workType = int(input('숫자를 입력해줘'))

if(workType == 1 or workType == 2):
    if(workType == 1):
        print('[수집]을 시작해볼게용~♥')
        collector.init()
    else:
        print('[등록]을 시작해볼게용~♥')
else:
    print('숫자 1, 2 둘 중 하나만 넣어야지~')
    print('프로그램을 다시 시작해줘요~')
    time.sleep(2)
    sys.exit(1)
    
    


    