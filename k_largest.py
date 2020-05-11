'''Given an array a of n numbers and a count k,
find the k largest values in the array a. 
Example: a = [5, 1, 3, 6, 8, 2, 4, 7], k=3 -> [6, 8, 7]'''

# idea 1: make a max heap and remove k elements
# runtime: O(N) to heapify then k * log(N) to remove k elements

# idea 2: keep track of k largest values in another data structure
# runtime: O(N) to parse through array and log(k) to insert/replace largest values
# overall would be n * log(k)

# Since k is likely much smaller than N, first implementation seems better

def merge(arr1, arr2):

    to_return = []
    i1 = 0
    i2 = 0

    while i1 < len(arr1) and i2 < len(arr2):

        if arr1[i1] < arr2[i2]:
            to_return.append(arr1[i1])
            i1 += 1
        else:
            to_return.append(arr2[i2])
            i2 += 1

    if i1 < len(arr1):
        to_return += arr1[i1:]
    else:
        to_return += arr2[i2:]

    return to_return

def merge_sort(arr):

    if(len(arr) < 2):

        return arr

    mid = len(arr) // 2

    left = arr[0:mid]
    right = arr[mid:]

    new_left = merge_sort(left)
    new_right = merge_sort(right)

    return merge(new_left,new_right)

arr = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3

tup_arr = []
for i in range(len(arr)):

    tup_arr.append((arr[i],i))

tup_arr = merge_sort(tup_arr)

pos_arr = []
for i in range(len(tup_arr) - k,len(tup_arr)):

    pos_arr.append((tup_arr[i][1],tup_arr[i][0]))

pos_arr = merge_sort(pos_arr)
final_arr = []
for value in pos_arr:
    final_arr.append(value[1])

print(final_arr)
