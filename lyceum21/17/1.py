mammals = {'cat', 'dog', 'fox', 'elephant', 'dog'}
# print(mammals)
#
#
# a = set() #empty set

for i in mammals:
    print(i)
print('fox' in mammals)
if 'fox' in mammals:
    print('Элемент в множестве')
else:
    print('Элемента нет в множестве')

# print(),input(),min,max,
# print()

mammals.add('deer')
print(mammals)

my_set = set()
my_set.add('a')
my_set.add('b')
my_set.add('a')
print(my_set)

a = {1,2,3}
# a = set(1,2,3) # WRONG !!
print(a)

a = my_set.pop()
print(a)

my_set = {'a', 'b', 'c'}

print('до удаления:', my_set)
elem = my_set.pop()
print('удаленный элемент:', elem)
print('после удаления:', my_set)