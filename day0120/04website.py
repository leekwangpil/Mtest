# 04website.py
site = 'www.google.org'

def connect_login(): #구현=기술=정의 
    id = input('관리자본인인증 email입력 ')
    pwd = int(input('관리자본인인증 pwd입력 '))
    if id=='sky@gg.com' and pwd==1234 :
        return True
    else:
        return False
        
ok_success = connect_login() #함수호출=함수call
if ok_success:
    print(site , '관리자 전용 사이트 접속가능합니다')
else:
    print('메일인증을 정확히 다시 하세요')



