def freezing(arr):
    a = sum([1 for i in range(len(arr)) for j in range(len(arr[i])) if arr[i][j] < 0])