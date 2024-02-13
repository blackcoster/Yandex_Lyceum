numbers = [int(x) for x in input().split()]
minimum = min(numbers)
maximum = max(numbers)
dic = dict.fromkeys(range(minimum, maximum + 1), 0)
for x in set(numbers):
    dic[x] = numbers.count(x)
print(dic)
