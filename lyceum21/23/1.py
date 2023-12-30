from math import sin, radians, cos, gcd
r1,r2,a,b = int(input()), int(input()), int(input()),int(input())
result = []
for t in range(0,360//gcd(a,b)+1):
    x = r1 * cos(a * radians(t))
    y = r2 * sin(b * radians(t))
    result.append((round(x,2),round(y,2)))
print(result)