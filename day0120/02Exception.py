# 02Exception.py
num = 0 #변수 
try:
    num = int(input('숫자를 기술>>> '))
except Exception as ex:
    print('에러', ex)
else:
    print('결재금액 =', num*5 ,'원' )
finally:
    print('열려라 토요일 ~~~')
    print('열려라 일요일 ~~~')
    print('열려라 월요일 ~~~')