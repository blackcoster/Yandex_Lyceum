s = 'hello, world'
new_s = s[1:5]
new_s = s[0:5]
new_s = s[1:]
new_s = s[:]
print(new_s)
full_name = 'Иванов Иvan И.'
surname = full_name[:-8]
surname = full_name[:6]
print(surname)

print(full_name[0:1])
print(full_name[0])
print(full_name[::-1])

text = 'СЕЛ В ОЗЕРЕ БЕРЕЗОВ ЛЕС'
text_reversed = text[::-1]
print(text == text_reversed)