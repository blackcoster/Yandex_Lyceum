n = int(input())
count = 0
max = 0
while n!=0:
    if n > max:
        max = n
        count = 1
    elif n == max:
        count+=1
    n = int(input())
print(count,max)