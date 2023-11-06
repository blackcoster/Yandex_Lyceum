# n = int(input()) #1234
# while n!=0:
#     print(n%10)
#     n = n//10 # n//=10
#


# n = int(input()) #1234
# count = 0
# while n!=0:
#     count+=1
#     n = n//10 # n//=10
# print(count)


n = int(input()) #1234
count = 0
while n!=0:
    if (n % 10) % 2 == 1:
        count+=1
    n = n//10 # n//=10
print(count)