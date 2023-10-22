n = int(input('сколько чисел будет всего?')) # сколько чисел принимать НАТУРАЛЬНЫЕ
maximum = -1
for i in range(n):
    number = int(input())
    if number > maximum:
        maximum = number

print(maximum)

