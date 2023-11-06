#maximum
biggest_book = 0
n = int(input())
while n > 0:
    if n > biggest_book:
        biggest_book = n
    n = int(input())
print(biggest_book)

# 1,2 maximum
max_1 = 0
max_2 = 0
n = int(input())
while n > 0:
    if n > max_1:
        max_1,max_2 = n,max_1
    elif n > max_2:
        max_2 = n
    n = int(input())
print(biggest_book)