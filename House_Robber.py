def rob(houses):

    """
    nums: list of ints
    output: most gold stolen
    """
    if len(houses) == 0:
        return 0

    curr_max = 0
    prev_max = 0

    for house in houses:
        new_max = max(curr_max,prev_max + house)
        prev_max = curr_max
        curr_max = new_max
        print(curr_max)

    return curr_max

rob([3,1,1,6,1,1,7])
