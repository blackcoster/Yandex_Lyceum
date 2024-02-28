with open('numbers.txt') as in_file, open('smallest.txt','w') as out_file:
    data = []
    for line in in_file:
        line = line.rstrip()
        temp = [line.count(x) for x in line]
        nums = sorted(list(set([x for x in line if line.count(x) == max(temp)])))
        if nums[0] == '0' and len(nums)>1:
            nums[0],nums[1] = nums[1],nums[0]
        print(''.join(nums),file=out_file)
