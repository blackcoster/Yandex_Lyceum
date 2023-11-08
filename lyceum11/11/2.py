age = int(input('age: '))
grade = int(input())
city = input()


if age > 12 and grade > 7 and city=='Moscow':
    print('OK')
else:
    print('not OK')


#
# if age > 12 and grade > 7 and (city=='Moscow' or city=='Samara'):
#
#     a or not (b and c)
#
#  a = False
#  b = false
#  c = true
#
#  False or False and True
#  False or False = False


