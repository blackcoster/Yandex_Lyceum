primes = [2, 3, 5, 7, 11]


a = []
a = list()

a = [1,2,3]
print(a*3)

a = [0]*8
print(a)

print(primes[0],primes[1],primes[-1])
primes.append(13)
primes.append(17)
primes.append(19)
print(primes)

odd_numbers = [1,3,5,7,9]
kusok = [11,13,15]
odd_numbers.extend(kusok)
print(odd_numbers)

stroki = ['polina','masha']
stroki.extend('lena')
stroki.append('lena')
print(stroki)

a = {1,2,3}
stroki.extend(a)
print(stroki)

odd_numbers.append(17)
odd_numbers.append(18)
print(odd_numbers)
odd_numbers[-1] = 19
print(odd_numbers)

print(len(primes))  # выводим длину списка
primes += [23, 29]  # списки можно складывать, как и строки
print(primes)  # выведет [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
if 1 in primes:  # можно проверять, содержится ли в списке элемент
    print('Мы считаем единицу простым числом.')
else:
    print('Мы, как и все остальное человечество, не считаем 1 простым числом.')

for i in range(len(primes)):
    # выведем по очереди все элементы списка...
    print('Простое число номер', i + 1, '-', primes[i])
for p in primes:
    print('Квадрат числа', p, '-', p ** 2)  # и их квадраты


months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август',
          'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
spring = months[2:5]  # spring == ['март', 'апрель', 'май']
for month in spring:
    print(month)
months[6:8] = ['June', 'July', 'August']
print(months)
del months[6]
print(months)

months.remove('март')
del month[0]
print(months)

