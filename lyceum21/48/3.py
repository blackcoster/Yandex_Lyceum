def buzzing(line, letter):
    li = [word for word in line.split() if letter.lower() in word.lower()]
    return li
