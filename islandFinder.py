import random

islands = list()
'''islands.append([0,1,0,1,0])
islands.append([1,0,0,1,0])
islands.append([0,0,0,0,0])
islands.append([0,0,0,1,0])
islands.append([1,1,1,0,1])'''

dim = random.randint(4,6)

for x in range(0,dim):
    a_list = list()
    for y in range(0,dim):
        a_list.append(random.randint(0,1))

    islands.append(a_list)

has_not_checked = list()
index = -1
for a_list in islands:
    index += 1
    has_not_checked.append(list())
    for num in a_list:
        has_not_checked[index].append(True)

for a_list in islands:
    print(a_list)

def count_islands():
    num_islands = 0
    for r in range(0,index+1):
        for c in range(0,index+1):
            if(islands[r][c] == 1 and has_not_checked[r][c]):
                print("New Island")
                print(str(r) + "," + str(c))
                num_islands += 1
                expand_island(r,c,num_islands)

    return num_islands

def expand_island(r,c,island_num):
    if(is_not_in_bounds(r,c)):
        #print(str(r) + "," + str(c))
        return 0

    #print("R: " + str(r) + " C: " + str(c))
    #if(has_checked[r][c]):
    #    return 0

    #has_checked[r][c] = True
    if(has_not_checked[r][c]):
        has_not_checked[r][c] = False
        if(islands[r][c] == 1):
            islands[r][c] = island_num
            expand_island(r+1,c,island_num)
            expand_island(r-1,c,island_num)
            expand_island(r,c+1,island_num)
            expand_island(r,c-1,island_num)
            '''expand_island(r+1,c+1,island_num)
            expand_island(r-1,c-1,island_num)
            expand_island(r-1,c+1,island_num)
            expand_island(r+1,c-1,island_num)'''


def is_not_in_bounds(r,c):
    return (r < 0 or r > index or c < 0 or c > index)

num_islands = count_islands()
print(num_islands)

for a_list in islands:
    print(a_list)
