import mylib

print('1. 영화 순위 2. 멜론차트 100')
num = input('입력 : ')
if num == '1':
    mlist = mylib.get_dmv()
    for m in mlist:
        print(m[1])
elif num == '2':
    mylib.melon()

else:
    print('Error')