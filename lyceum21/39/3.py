with open('triangles.txt') as in_file:
    lines = [[int(x) for x in line.split()] for line in in_file]
    count = 0
    for item in lines:
        a, b, c = item
        if a < b + c and b < a + c and c < b + a:
            count += 1
    print(count)
