def translate():
    n = input()
    res = 'Неверный ввод'
    for symbol in n:
        if symbol not in '01':
            break
    else:
        res = int(n, 2)
    print(res)
# translate()