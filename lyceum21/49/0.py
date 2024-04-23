count = 0


def tic_tac():
    global count
    if count % 2 == 1:
        print('ТАК')
    else:
        print('ТИК')
    count += 1


