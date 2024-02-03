import random

temp = list(range(1, 16)) + ['']

random.shuffle(temp)
tags = [temp[i:i + 4] for i in range(0, 16, 4)]
for row in tags:
    for elem in row:
        print(elem, end='\t')
    print()
