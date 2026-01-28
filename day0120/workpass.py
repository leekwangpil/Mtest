# workpass.py 
def main(): 
    message = '합격여부메세지'
    x = 90
    y = 65
    total = x+y
    avg = total//2
    if avg >= 70 :
        message = '축합격'
    else:
       message = '재시험'
    return message

if __name__ == '__main__' :
    result = main()
    print('결과 내용을 아래에서 확인하세요')
    print('*****', result, '*****')
    print()
