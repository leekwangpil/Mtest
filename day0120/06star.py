# 0star.py

# 해결1] for반복문에 for 중첩
# 해결2] while 반복 한번 
# 해결3] while반복문에  while중첩
"""
★             1행  1열
★ ★          2행  2열
★ ★ ★       3행  3열
★ ★ ★ ★    4행  4열
★ ★ ★ ★ ★  5행  5열
"""
a = 0
while a<5:
    a=a+1
    print('🌻' * a)


print()
print()
for k  in range(1,6): #1행일때 1개별출력 2행일때 2개별출력
    for j in range(0,k,1): #0~1  0~2  0~3
        print('★', end=' ' )
    print()



