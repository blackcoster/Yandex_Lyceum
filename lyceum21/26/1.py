line = [int(i) for i in input().split()]
left = list(range(len(line)))
stack = []
for i in range(len(line)):
    while stack and line[i] < line[stack[-1]]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    stack.append(i)

# # 4 9 4 2 3 1 5
# i = 0 stack = [0] left =[0 1 2 3 4 5 6]
# i = 1 stack = [0 1] left =[0 0 2 3 4 5 6]
# i = 2 stack = [0 2] left =[0 0 0 3 4 5 6]
# i = 3 stack = [3] left =[0 0 0 3 4 5 6]
# i = 4 stack = [3 4] left =[0 0 0 3 3 5 6]
# i = 5 stack = [5] left =[0 0 0 3 3 5 6]
# i = 6 stack = [5 6] left =[0 0 0 3 3 5 5]


