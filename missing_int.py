def first_missing_positive_integer(ints):

    swap_index = len(ints) - 1
    i = 0
    while(i < swap_index):

        if(ints[i]< 1):
            ints[swap_index], ints[i] = ints[i], ints[swap_index]
            swap_index -= 1
        i += 1

    print(ints)

    for i in range(0,swap_index+1):
        print(i)
        ints[ints[i]-1] *= -1

    print(ints)



ints = [4,3,-1,1]
#ints = [0,1,2]
print(first_missing_positive_integer(ints))
