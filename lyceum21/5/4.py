n = int(input('How many numbers?'))
minimum = 1001
for i in range(n):
    num = int(input())
    if num < minimum and num > 0:
        minimum = num
print(minimum)


# 45 6 30 1 3
# min = 1001
# 45 - min=45
# 6 - min = 6
# 30- min =6
# 1: min = 1
# 3: min = 1
