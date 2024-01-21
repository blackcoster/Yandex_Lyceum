#1
n = int(input())
for j in range(n, 0, -1):
    print(j * str(j))
# 333
# 22
# 1

#2 произведение нечетных цифр
n = int(input())
total = 1 # начальное значение для произведения!!!!
while n > 0:
    if n % 2 != 0:
        total *= n % 10
    n //= 10
print(total)

#3 количество нечет чисел  ghbybvftv (вводятся 10 чисел меньше 20)
counter = 0
minimum = 20 #мб отрицательноное
for i in range(10):
    x = int(input())
    if x % 2 != 0:
        counter += 1
        if x < minimum:
            minimum = x
if counter > 0:
    print(counter)
    print(minimum)
else:
    print('Нет')

#4 принимаем 6 чисел  ( все по модулю меньше 50) вывести кол-во кратных 7 и максимальное из кратных 7
counter = 0
maximum = -50
for i in range(6):
    x = int(input())
    if x % 7 == 0:
        counter += 1
        if x > maximum:
            maximum = x
if counter > 0:
    print(counter)
    print(maximum)
else:
    print('Нет')

#5 четвертая цифра с начала (для 123456789 ответ 4)
n = int(input())
while n > 9999:
    n //= 10
print(n % 10)
