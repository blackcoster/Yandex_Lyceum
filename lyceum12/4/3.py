language_1 = 'ruby'
language_2 = 'kotlin'
language_3 = 'Python'
# language_3 = language_2
# language_1 = language_3

language_3,language_1 = language_2,language_3
print(language_1,language_2,language_3)

# first_name, last_name = input(), input()
# print(first_name,last_name)


name1 = 'Саша'
name2 = 'Паша'
name3 = 'Маша'
name4 = 'Даша'
name1, name2 = name2, name3  # 1 - pasha 2 - mashan  
name3, name4 = name4, name1  # 3 - dasha, 4 - pasha

print(name1,name2,name3,name4)