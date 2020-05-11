arr = [0,1,1,0,2,0,0,0,2,1,0,2,1,1,2,0,1,1,2,0,2]

zero_stop = 0
one_stop = 0
two_stop = len(arr) - 1
i = -1

#print(str(arr) + " zero stop: " + str(zero_stop) + " one stop: " + str(one_stop) + " two stop: " + str(two_stop))

while(i < two_stop):

    i += 1
    print(i)
    if(arr[i] == 0):
        arr[i], arr[zero_stop] = arr[zero_stop], arr[i]
        zero_stop += 1
        one_stop += 1
        #two_stop += 1
    elif(arr[i] == 1):
        arr[i], arr[one_stop] = arr[one_stop], arr[i]
        one_stop += 1
        #two_stop += 1
    else:
        arr[i], arr[two_stop] = arr[two_stop], arr[i]
        while(arr[i] == 2):
            two_stop -= 1
            arr[i], arr[two_stop] = arr[two_stop], arr[i]
        while(arr[i] == 0):
            arr[i], arr[zero_stop] = arr[zero_stop], arr[i]
            zero_stop += 1
            one_stop += 1
        two_stop -= 1

    print(str(arr) + " zero stop: " + str(zero_stop) + " one stop: " + str(one_stop) + " two stop: " + str(two_stop))

print(str(arr) + " zero stop: " + str(zero_stop) + " one stop: " + str(one_stop) + " two stop: " + str(two_stop))
