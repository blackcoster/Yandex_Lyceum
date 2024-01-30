base = int(input())
number = input()

res = 'ДА'
for i in range(len(number)-1,-1,-1):
    if int(number[i]) >= base:
        res = len(number) - 1 - i
        break

print(res)