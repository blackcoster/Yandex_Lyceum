# variant 1
# def reader(*lines,substr='dog',order=False):
#     lines = [line for line in lines if substr in line]
#     lines.sort(reverse=order)
#     return lines

# variant 3
# def suit_ordering(*lines,buttons=1,mode=True):
#     lines = [line for line in lines if len(line)%buttons==0]
#     if mode:
#         lines = [line for line in lines if 'dog' in line.lower()]
#     else:
#         lines = [line for line in lines if 'dog' not in line.lower()]
#     return sorted(lines)

