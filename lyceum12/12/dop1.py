hours = int(input())
minutes = int(input())
if minutes == 30 and (hours == 10 or hours == 11):
    print('Да')
else:
    print('Нет')