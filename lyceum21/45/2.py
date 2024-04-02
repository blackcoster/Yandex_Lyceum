with open('triangles.txt') as in_file:
    lines = [[int(x) for x in line.split()] for line in in_file]
    max_square = 0
    largest = []
    for item in lines:
        a, b, c = item
        if a+b>c and a+c>b and b+c>a:
            p = sum(item)/2
            s = (p*(p-a)*(p-b)*(p-c))**0.5
            if s > max_square:
                largest = item[:]
                max_square = s
    print(*largest)

