line = input()
lines = []
while line:
    lines.append(line)
    line = input()
dust = input()

for i in range(len(lines)):
    temp = lines[i]
    for letter in dust:
        temp = temp.replace(letter, ' ')
    lines[i] = ' '.join(temp.split())
print('\n'.join(lines))

