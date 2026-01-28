# book491.py
num = 0 #변수 
try:
    num = int(input('숫자를 기술>>> '))
except:
    print('에러가 발생했습니다 정확한 데이터를 다시 입력하세요')
else:
    print('결재금액 =', num*5 ,'원' )
finally:
    print('열려라 참깨 ~~~')
    print('열려라 들깨 ~~~')
    print('열려라 호박 ~~~')