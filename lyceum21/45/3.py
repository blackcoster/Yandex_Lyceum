numbers = [int(x) for x in input().split()]
dic = {x: numbers.count(x) for x in set(numbers)}
for number in dic:
    if dic[number] == 1:
        print(number)
        break
