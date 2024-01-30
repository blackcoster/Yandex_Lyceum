n = int(input())
set1 = set()
set2 = set()
set3 = set()
for i in range(n):
    m = int(input())
    if m > 40:
        set1.add(m)
    if m % 2 == 0:
        set2.add(m)
    if m % 3 == 0:
        set3.add(m)
result = (set1.intersection(set2).union(set1.intersection(set3)).union(set2.intersection(set3))
          - set1.intersection(set2).intersection(set3))
for item in result:
    print(item, end=' ')

