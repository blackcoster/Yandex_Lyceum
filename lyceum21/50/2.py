def reversed_item(item):
    return item[::-1]

words = []
line = input()
while line:
    words.append(line)
    line = input()

for word in sorted(words, key=reversed_item):
    print(word)