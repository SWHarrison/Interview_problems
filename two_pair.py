def two_pair(target, nums):

    hash_list = {}
    to_return = []

    for num in nums:
        pair = target - num
        if num in hash_list:
            to_return.append((num,pair))
        else:
            hash_list[pair] = 1

    return to_return

print(two_pair(7,[3,5,2,-4,8,11,4]))
