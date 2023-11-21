# task1
print('п')
print('по')
print('пол')
print('поли')

# task2
symbol = input()
shirina = int(input())

print(symbol * shirina)
print(symbol + ' ' * (shirina - 2) + symbol)
print(symbol * shirina)
# *********
# *       *
# *       *
# *********

# task3
n = int(input())
last = n % 10
pred_last = n % 100 // 10
if last == 1 and pred_last == 1:
    print('')
else:
    print('')

# task4
age = int(input())
school = input()

if 10 <= age <= 20 and school == "46":
    print('')
else:
    print('')

# task5
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print('')
else:
    print('')
