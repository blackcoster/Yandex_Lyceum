def fifth_a(line):
    words = line.split()
    count = 0
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j].lower() == 'a':
                count += 1
                if count == 5:
                    return i+1, j+1
    return -1, -1
