# variant 1
# import sys
#
# data = list(map(str.strip, sys.stdin))
# good = []
# for d in data:
#     name, days = d.split(' ?? ')
#     days = [int(day) for day in days.split()]
#     chetnie = [day for day in days if day % 2 == 0]
#     if len(chetnie) > 0:
#         good.append(name)
#
# good.sort(key=lambda s: (-len(s), s))
# print(*good, sep='\n')

# variant 5
# import sys
# height = int(input())
# data = list(map(str.strip, sys.stdin))
# good = []
# for d in data:
#     name, n = d.split(' ## ')
#     n = int(n)
#     if n >= height:
#         good.append(name)
# good.sort(key=lambda s: (len(s), s))
# print(*good, sep='\n')