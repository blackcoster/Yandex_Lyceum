dic = {}
words = input().split()
for word in words:
    bukvs = set(word.lower())
    bukvs = sorted(list(bukvs))
    bukvs = ''.join(bukvs)
    dic2 = {'length': len(word),
            'has_upper': bool([x for x in word if x.isupper()]),
            'has_digit': bool([x for x in word if x.isdigit()]),
            'letters': bukvs}
    dic[word] = dic2
print(dic)