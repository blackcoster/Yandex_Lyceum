# words = input().split()
#
# while len(words) > len(set(words)):
#     for word in words:
#         if words.count(word) > 1:
#             words.remove(word)
# print(' '.join(words))

a='Жил был у бабушки серенький козлик. Вот как, вот как, серенький козлик.'.split()
sep = 3
ap = list(range(sep, len(a), sep))[::-1]
print(ap)
for i in ap:
    a.insert(i,'555')
print(a)


# line = input()
# while line != '...':
#     if (len(line)==11 and line.startswith('8') and line.isdigit()) or (len(line)==12 and line.startswith('+7') and line[1:].isdigit()):
#         nomer = list(line)
#         if line[0] == '8':
#             nomer.pop(0)
#             nomer.insert(0,'7')
#             nomer.insert(0,'+')
#         nomer.insert(-2,'-')
#         nomer.insert(-5,'-')
#         nomer.insert(-9, ')')
#         nomer.insert(-13, '(')
#         print(''.join(nomer))
#     else:
#         print(line)
#     line = input()


