girl = 'pavel'
boy = 'lena'
#
# temp = girl
# girl = boy # girl = lena
# boy = temp # boy = lena
# print(girl,boy)


girl,boy = boy,girl
print(girl,boy)

name1 = 'sasha'
name2 = 'pasha'
name3 = 'masha'
name4 = 'dasha'
name1,name2 = name2,name3 # name1 = pasha, name2 = masha
name3,name4 = name4,name1 # name3 = dasha, name4 =pasha

print(name1, name2, name3, name4)

# выводит список зарезервированных слов
# eklgmelkgm
print(help('keywords'))  # komment