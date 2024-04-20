a = 1
b = 2
a = 3


def matrix_has_close_value(matrix, value, eps):
    for row in matrix:
        for cell in row:
            if abs(cell - value) <= eps:
                return True
    return False


table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = matrix_has_close_value(table, 3.75, 0.5)
print(result)