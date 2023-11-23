# task 1
n = int(input())
if n % 3 == 0 and n % 7 == 0:  # числа в условиях могут отличаться
    print('...')  # принты вписать самостоятельно
elif n % 3 == 0:
    print('...')
elif n % 7 == 0:
    print('...')
else:
    print('...')

# task 2

stroka = input()
count = 0
dlina = 0
while stroka != 'СЕКРЕТ':  # стоп-слово может быть другим
    if 'цвет' in stroka or 'капуст' in stroka:  # слова для поиска могут быть другими
        count += 1
        dlina += len(stroka)
    stroka = input()
if count == 0:
    print(count) # может быть нужно вывести еще ноль (count, 0)
else:
    print(count, round(dlina / count, 3))  # количество знаков после запятой может отличчаться

# task 3

n = int(input())
for i in range(n):
    start = int(input())
    stop = int(input())
    step = int(input())
    if start > stop or step <= 0:
        print('ОШИБКА')
        break
    for j in range(start, stop + 1, step):
        print(j, end=' ')
    print()
