#1
a = input()
unique = set()
while a != '':
    unique.add(a.capitalize())
    unique.add(a.upper())
    unique.add(a.lower())
    a = input()
for i in unique:
    print(i)

#2
s = input().split(' - ')
s[1::2] = ['Word'] * len(s[1::2])
print(' @ '.join(s))

# 3 сортировка
# polina sahsa 6
# a b 6

s = input()
listok = []
while s != 'ВАШЕ СТОП_СЛОВО':
    s = s.split()
    s[2] = int(s[2])
    listok.append(s)
    s = input()
for i in range(len(listok) - 1):
    for j in range(len(listok) - 1 - i):
        if listok[j][2] < listok[j + 1][2]:
            listok[j], listok[j + 1] = listok[j + 1], listok[j]
        if listok[j][2] == listok[j + 1][2]:
            if listok[j][0] < listok[j + 1][0]:
                listok[j], listok[j + 1] = listok[j + 1], listok[j]
            elif listok[j][0] == listok[j + 1][0]:
                if listok[j][1] < listok[j + 1][1]:
                    listok[j], listok[j + 1] = listok[j + 1], listok[j]

for i in listok:
    print(i[0], i[1])

