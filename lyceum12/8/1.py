num = 12
first_digit = num // 10
last_digit = num % 10
print(first_digit,last_digit)


num = 345

# c = num % 10
# b = num % 100 - c
# a = num % 1000 - b

first_digit = num // 100
# center_digit = num // 10 % 10
center_digit = num % 100 // 10
last_digit = num % 10
print(first_digit,center_digit,last_digit)

n = 12345

a = n // 10000
b = n % 10000 // 1000
c = n % 1000 // 100
d = n % 100 // 10
e = n % 10