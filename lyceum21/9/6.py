#prostoe chislo

#
# n = int(input())
# prime = 1  # определяет, простое число или нет
# for i in range(2, int(n ** 0.5) + 1):
#     if n % i == 0:
#         prime = 0
#         break
# if prime == 1:
#     print('Простое')
# else:
#     print('Не простое')


for i in range(10):
    print('Итерация номер', i, 'начинается...')
    if i == 3:
        print('Ха! Внезапный выход из цикла!')
        break
    print('Итерация номер', i, 'успешно завершена.')
print('Цикл завершён.')


for i in range(10):
    print('Итерация номер', i, 'начинается...')
    if i == 3:
        print('...но её окончание таинственно пропадает.')
        continue
    print('Итерация номер', i, 'успешно завершена.')
print('Цикл завершён.')


count = 1
while count < 100:
    if count % 5 == 0:
        count += 1
        continue
    print(count)
    count += 1

a = True
print(a * 41)
print(a + 9.5)
print(a + True)

b = False
print(b * 2)
print(b + 5)
