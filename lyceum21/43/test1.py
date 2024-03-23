# легкий вариант
with open('input.txt') as in_file:
    data = [x.rstrip() for x in in_file] # обязательно
    data = [x for x in data if len(x) % 2 == 1]
    data.sort()
with open('output.txt', 'w') as out_file:
    for line in data:
        print(line, file=out_file)

# другие вариации
# lower/ upper/ capitalize в зависимости от задачи

#     avg = sum([len(x) for x in data])/len(data)
#     data = [x.lower() for x in data if len(x) == avg]  # выбираем те что равны средней длине напрмер
#     data.sort() # либо data.sort(reverse=True) для обратного порядка сортировки

#     data = [x.upper() for x in data if 'P' in x.upper() or 'K' in x.upper()]
#     data.sort() # либо data.sort(reverse=True) для обратного порядка сортировки

#     data = [x.lower() for x in data if 'A' not in x.upper() and 'B' not in x.upper() and 'C' not in x.upper()
#             and 'D' not in x.upper() and 'E' not in x.upper()]
#     data.sort() # либо data.sort(reverse=True) для обратного порядка сортировки

#     data = [x[0::2].capitalize() for x in data] # для четных
#     data.sort() # либо data.sort(reverse=True) для обратного порядка сортировки



# то что писали на уроке

with open('input.txt') as in_file:
    data = [x.rstrip() for x in in_file]
    # data = [x for x in data if len(x) % 2 == 1] # нечетные длины

    # lengths = [len(x) for x in data]
    # avg = sum(lengths)/len(lengths)
    # data = [x.upper() for x in data if len(x) >= avg]

    # data = [x for x in data if 'S' in x or 'T' in x or 'P' in x]

    # data = [x for x in data
    #         if 'S' not in x and
    #         'T' not in x and
    #         'P' not in x]

    # data = [x[1::2].capitalize() for x in data]
    #

    data.sort(reverse=True) # обратный алф порядок

with open('output.txt', 'w') as out_file:
    for line in data:
        print(line, file=out_file)