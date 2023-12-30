a = 'polina-was-sick-now-she-is-fine'
words = a.split('-',maxsplit=3)
print(words)

b = '+'.join(words)
print(b)


arr = [1,2,3]
print(' '.join(a))
result = []
for n in arr:
    result.append(str(n))
print('; '.join(result))  # 1; 2; 3

print('_'.join('Аглицкую блоху на подковы подковали!'))
