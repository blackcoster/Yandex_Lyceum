# Напиши программу, которая принимает натуральное чётное число n. Выведи список чётных чисел от 1 до n: [2,4,6..8]
print([x for x in range(0, int(input())+1, 2)])

# есть два списка 4 5 6 7 8 и 1 2 3 4 5 получить список сумм
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [a[i]+b[i] for i in range(len(a))]
print(*c)

#приходят числа через пробел. посчитать разность и записать 2 3 4 5 -> 2 - 3 - 4 - 5 = 120
a = [int(x) for x in input().split()]
product = a[0]
for num in a[1:]:
    product = product-num
print(*a, sep=' - ', end= ' = ')
print(product)

# длины слов. придут слова через пробел
length = [len(x) for x in input().split()]
average = sum(length)/len(length)
min1 = min(length)
max1 = max(length)
longer_than_avg = len([x for x in length if x > average])
shorter_than_avg = sum([1 for x in length if x < average]) # same as above [1 1 1]

# надо изменить слова. приходят слова через пробел в каждом слове поменять 1 и ласт буквы. если слово из 1 символа то дубдтровать
new = [word[-1]+ word[1:-1] + word[0] for word in input().split()]
# new = [word[-2:]+ word[2:-2] + word[:2] for word in input().split()]
print(*new)
