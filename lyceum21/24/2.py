2
line = input().split()
print(' '.join([line[i] for i in range(1,len(line)) if len(line[i])>len(line[i-1])]))

3
print('\n'.join([f'Число {i} кратно трём' if i % 3 == 0 else f'Число {i} не кратно трём' for i in range(int(input()),int(input())+1)]))

4
word = input()
print('\n'.join([word[i:]+word[:i] for i in range(len(word)+1)]))

5
a = input().split()
n, m, k = int(a[0]), int(a[1]), int(a[2])
print('\n'.join([f'{j} + {i} = {j + i}' for j in range(n, m + 1) for i in range(m, k + 1)]))