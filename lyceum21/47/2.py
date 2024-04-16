def letters(lines):
    res = []
    words = lines.split()
    for word in words:
        s = set()
        for letter in word:
            if letter.isalpha():
                s.add(letter.lower())
        s = list(s)
        s.sort()
        res.append(''.join(s))
    return res
