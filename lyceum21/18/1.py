a = 'polina'
# index = int(input())
# print(a[index])

# a[0] ='k'   # WRONG !!!
# print(a)


for i in range(len(a)):
    print(a[i])

for ch in a:
    print(ch)

text = 'hello, my dear friends!'
vowels = 0
for letter in text:
    if letter in {'a', 'e', 'i', 'o', 'u', 'y'}:
        vowels += 1
print(vowels)

text = 'hello, my dear friends!'
vowels = 0
for i in range(len(text)):
    if text[i] in {'a', 'e', 'i', 'o', 'u', 'y'}:
        vowels += 1
print(vowels)

# print('\u2603')
print(ord('P'))
print(chr(126))

for i in range(26):
    print(chr(ord('A') + i))

a = 'polina'
for i in range(len(a)-2):
    print(a[i+2])


line = input()
increment = decrement = line[0]
# ABCDCDCBA
# inc = abcd a
# dec = dcba

for i in range(1, len(line)):
    if ord(line[i]) > ord(increment[-1]):
        increment += line[i]
    else:
        if len(increment) > 1:
            print(increment)
        increment = line[i]
    if ord(line[i]) < ord(decrement[-1]):
        decrement += line[i]
    else:
        if len(decrement) > 1:
            print(decrement)
        decrement = line[i]
if len(increment) > 1:
    print(increment)
if len(decrement) > 1:
    print(decrement)