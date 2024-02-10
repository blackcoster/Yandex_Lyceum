line = input()
dic = {}
while line:
    tale, hero = line.split(': ')
    dic[hero] = tale
    line = input()
n = int(input())
for i in range(n):
    request = input()
    if request in dic:
        print(dic[request])
    else:
        print('Нет информации')