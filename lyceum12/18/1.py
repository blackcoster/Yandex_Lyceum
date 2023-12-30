# num = int(input())
# while num != 0:
#     print(num**2)
#     num = int(input())
#
# for i in range(0):
#     print()
#

p = 1
num = 1948
while num != 0:
    digit = num % 10
    # p*=digit
    print(digit)
    num = num//10
# print(p)