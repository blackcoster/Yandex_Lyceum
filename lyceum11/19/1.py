# total = 0
# count = 0
# mark = int(input())
# # while mark in [3,4,5]:
# while 3 <= mark <= 5:
#     count+=1
#     total+=mark
#     mark = int(input())
# print(total/count)

# num = int(input())
# while num != 0:   # пока в числе есть цифры
#     last_digit = num % 10   # получить последнюю цифру
#     print(last_digit)
#     num = num // 10   # удалить последнюю цифру из числа

# num = int(input())
# total = 1
# while num != 0:
#     last_digit = num % 10
#     total *= last_digit
#     num = num // 10
# print(total)


num = 77777

# flag = 1
# last = num%10
# while num//100 != 0:
# while num != 0:   # пока в числе есть цифры
#     digit = num % 10   # получить последнюю цифру
#     if digit != last:
#         flag = 0
#     num = num // 10   # удалить последнюю цифру из числа
# print(flag)

num = 1234
while num//100 != 0:
    num = num //10
    print(num)
print(num%10)