# workGame.py

def zerg():
    print('zerg() 종족')
    print('Drone, Zergling, Hydralisk, Brood Lord\n')


def maple(season,cnt):
    print('메이플 시즌은', season)
    print('메이플 총 참여인원수', cnt)
    print('카이저, 제논, 카데나, 아크, 일리움\n')


def add(a,b): #계산만 빨리 처리할 용도 
    total = a+b
    return total

data = add(11,22)
print('총금액 =', data)
print('총금액 =', add(11,22))

def myTestpass(x,y): #계산후 if제어문으로 축합격/재시험 판단후 
    message = '합격여부메세지'
    total = x+y
    avg = total//2
    if avg >= 70 :
        message = '축합격'
    else:
       message = '재시험'
    return message

kor = 90  # kor = int(input('국어점수'))
eng = 80  # eng = int(input('영어점수'))
result = myTestpass(kor, eng)
print('당신의 시험결과는 *****🆗', result, '🆗*****')