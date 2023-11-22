# 1 task
print('p')
print('po')
print('pol')
print('poli')
print('polin')
print('polina')

# 2 task

symbol = input()
shirina = int(input())
visota = 3

print(symbol * shirina)
print(symbol + ' ' * (shirina - 2) + symbol)
print(symbol * shirina)
# **********
# *        *
# **********

# task3

# 2345 % 100 = 45
# 4000 % 100 = 0
n = int(input())
if n % 100 == 0:  # для ДВУХ последних чисел
    print('....')
else:
    print('...')

# task 4
age = int(input())
city = input()
if 10 <= age <= 15 and city == 'Moscow':
    print('...')
else:
    print('...')

# task 5
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
n = (x1 + y1 + x2 + y2) % 2 
if n == 0:
    print ('Да')
else:
    print ('Нет')


# 1 1 нечет+нечет = чет
#
# 0 0 чет+чет = чет
#
# 1 0
# 0 1