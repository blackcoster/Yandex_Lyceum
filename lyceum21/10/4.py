print('Тренажер по вводу палиндрома:')
while True:
    print('Введите число палиндром:')
    number = n = int(input())
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10
    if number == reverse:
        print('Вы ввели палиндром! Программа остановлена.')
        break
    print('Введенное число не палиндром, попробуйте еще раз.')
    #

    # n = 123
    # reverse = 0
    #
    # rev = 3
    # n = 12
    #
    # rev = 32
    # n = 1
    #
    # rev = 321
    # n = 0
    #