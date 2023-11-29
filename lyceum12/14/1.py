#1

# print('She said: "Hello! I\'m Anna."')
print('She said: "Hello! ' + "I'm " + 'Anna."')

#2
s = input()
print('Строка ' + s + ' имеет длину ' + str(len(s)) + '.')
# print('Строка', s, 'имеет длину', len(s), '.')

#3
string = '=^_^==^_^==^_^==^_^==^_^==^_^==^_^==^_^==^_^==^_^='
print(len(string))

#4
s = input()
if 'роб' in s or 'Роб' in s:
    print('Да')
else:
    print('Нет')

#5
s = input()
if '@' in s and '.' in s:
    print('Да')
else:
    print('Нет')

#6
s = input()
if 'суббота' in s or 'воскресенье' in s:
    print('Ура! Выходные!')
else:
    print('Ждём выходные...')