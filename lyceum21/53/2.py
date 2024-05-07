*rest, mult, step = [int(x) for x in input().split()]
result = [x for x in rest[::step] if x % mult == 0]
print(*result, sep=' ')
