meals = []
line = input()
while line:
    meal, caloric, rating = line.split()
    meals.append((int(caloric), int(rating), meal))
    line = input()
for c,r,m in sorted(meals):
    print(f'{m}\t{c}\t{r}')