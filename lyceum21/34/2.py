a = input().upper()
dic = {}
for ch in set(a):
    if ch.isalpha():
        dic[ch] = a.count(ch)
for k,v in dic.items():
    print(f'{k} - {v}')
