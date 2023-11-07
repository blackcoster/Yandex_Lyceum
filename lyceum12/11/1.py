print('how old are you?')
age = int(input())
print('what grade are you in?')
grade = int(input())
print('what city are you in?')
city = input()

# if age>=12:
#     if grade>=7:
#         print('dostup razreshen')
#     else:
#         print('dostup zapreschen')
# else:
#     print('dostup zapreschen')

if  age >= 12 and grade >=7 and (city =='Moscow' or city=='Saint-Petersburg'):
    print('dostup razreshen')
else:
    print('dostup zapreschen')

# #
# a = 1
# if a == 1 or input('what ') == '5':
#     print(5)
#
# a = 6
# if a == 1 and input('what ') == '5':
#     print(5)

# if 5<=x<=7 and
