def stretching(line, spaces):
    words = [(' ' * spaces).join(word) for word in line.split()]
    print((' ' * (spaces+1)).join(words))


stretching('hello world', 5)
