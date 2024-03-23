# легкий вариант

n = int(input())
dic = {}
for _ in range(n): # может быть цикл while
    word = input()
    dic[word] = ''  # обязательно
    for letter in word:
        if letter.lower() not in 'aeouiy':
            dic[word] += letter.upper()
    dic[word] = list(set(dic[word]))
    dic[word].sort(reverse=True)
    dic[word] = ''.join(dic[word]) # обязательно
print(dic) # обязательно

# идеи для других вариантов

#     for i in range(len(word)-1):
#         if word[i] in 'aeouiy':
#             dic[word].append(word[i+1])

#     for letter in word.lower():
#         if word.lower().count(letter) == 1:
#             dic[word].append(letter)

#     dic[word] = [w.upper() for w in word[1::2]]

#     dic[word] = [w.lower() for w in word]
#     dic[word] = list(set(dic[word]))


# если нужны уникальные значение и/или сортировка
#     dic[word] = list(set(dic[word]))
#     dic[word].sort()




# то что писали на уроке
#
# dic = {}
# word = input()
# while word:
#     word = word.lower()
#     dic[word] = []
#     for i in range(len(word) - 1):
#         if word[i] in 'aeouiy':
#             dic[word].append(word[i+1])
#     dic[word] = list(set(dic[word]))
#     dic[word].sort()
#     dic[word] = ''.join(dic[word])
#     word = input()
# print(dic)

dic = {}
n = int(input())
for _ in range(n):
    word = input()
    dic[word] = []
    for letter in word:
        if letter not in 'aeouiy':
            dic[word].append(letter.upper())
            dic[word].sort(reverse=True)
            dic[word] = ''.join(dic[word])
            # Wow
    for letter in word:
        if word.lower().count(letter) == 1:
            dic[word].append(letter)
print(dic)
