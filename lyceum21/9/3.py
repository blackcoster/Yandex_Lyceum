longest = ''
for i in range(int(input())):
    st = input()
    if len(st) > len(longest):
        longest = st
    elif len(st) == len(longest):
        if st > longest:
            longest = st
print(longest)