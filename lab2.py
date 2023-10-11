nums = [int(x) for x in input()]
if len(nums) != 7 or any([x not in '01' for x in map(str, nums)]):
    print("Invalid number")
else:
    s1 = (nums[0] ^ nums[2] ^ nums[4] ^ nums[6]) * 1
    s2 = (nums[1] ^ nums[2] ^ nums[5] ^ nums[6]) * 2
    s3 = (nums[3] ^ nums[4] ^ nums[5] ^ nums[6]) * 4
    s = s1 + s2 + s3 - 1
    if s > 0:
        nums[s] = int(not(nums[s]))
        print('Number', ''.join(map(str, [nums[2], nums[4], nums[5], nums[6]])))
        print('Error in number', s + 1)
    else:
        print('Without errors')
        print('Number', ''.join(map(str, [nums[2], nums[4], nums[5], nums[6]])))