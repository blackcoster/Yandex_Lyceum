text = input()
if 'хорош' in text and 'плох' not in text:
    print('Текст имеет положительную эмоциональную окраску.')
elif 'плох' in text and 'хорош' not in text:
    print('Текст имеет отрицательную эмоциональную окраску.')
else:
    print('Текст имеет нейтральную или смешанную эмоциональную окраску.')

