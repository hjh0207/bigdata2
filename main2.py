import goose

print('길을 가다가 거위를 만났습니다.')
print('먹이를 주면 안잡아 먹지')
print('1. 먹이를 준다 2. 그냥간다') 
user = 1
egg = 0
if user == 1:
    egg = goose.goldegg()

mymoney = 3000
mymoney = goose.moneybbung(mymoney)
print(f'황금알: {egg}, 내 돈: {mymoney}원')