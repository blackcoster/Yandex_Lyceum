num = int(input())
count = 0
while num != 0:
    if num % 4 == 0 and num % 10 ==2:
        count += 1
    num = int(input())
print(count)
