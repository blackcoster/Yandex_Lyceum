symbol = ord(input())
with open('binary.txt', 'w') as file:
    print(bin(symbol)[2:], file=file)