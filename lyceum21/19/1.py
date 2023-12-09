# num = '894563'
# chot = nechot = 0
# for i in range(0,len(num),2): # 0 2 4
#     chot += int(num[i])
# for i in range(1,len(num),2): # 1 3 5
#     nechot += int(num[i])
# if chot==nechot:
#     print('lucky')
# else:
#     print('unlucky')

num = '2333'
sign = 1
sum = 0
for i in range(len(num)):
    sum += sign * int(num[i])
    sign = -sign
if sum == 0:
    print('lucky')