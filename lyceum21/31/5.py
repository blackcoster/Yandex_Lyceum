elements = [int(x) for x in input().split()]
n = int(len(elements) ** 0.5)
matrix = [elements[i:i + n] for i in range(0, len(elements), n)]
main_diag = []
side_diag = []
for i in range(n):
    for j in range(n):
        if i == j:
            main_diag.append(matrix[i][j])
        if i == n - j - 1:
            side_diag.append(matrix[i][j])
        print(matrix[i][j], end='\t')
    print()
side_diag = side_diag[::-1]

result = []
for i in range(n):
    result.append(main_diag[i] * side_diag[i])
print(result)
