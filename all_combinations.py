import itertools
from pprint import pprint

def all_combs(n):

    '''list_of_list = []

    for i in range(0,n):
        num_list = []
        for i in range(0,n):
            num_list.append(i+1)

        list_of_list.append(num_list)

    print(list_of_list)'''

    list_of_list = [["a","b","c"],["d","e","f"],["g","h","i","j"]]

    #for list in itertools.product(*list_of_list):
    #    print(list)

    to_return = []
    for i in range(len(list_of_list[0])):
        to_return.append([list_of_list[0][i]])

    print("to return", to_return)

    for i in range(1,len(list_of_list)):

        to_add = []#to_return * len(list_of_list[i])
        for j in range(len(to_return)*len(list_of_list[i])):
            to_add.append(to_return[j%len(to_return)].copy())
        print("to add before adding", to_add)
        print("length of to_add", len(to_add))

        for j in range(0, len(to_add)):

            #print("j",j)
            new_value = list_of_list[i][j//(len(to_add)//len(list_of_list[i]))]
            #print("new value",new_value)
            #print("current to add ",to_add[j])
            to_add[j].append(new_value)

        #print("to add", to_add)
        to_return = to_add.copy()


    print("returning")
    return to_return

value = all_combs(4)
pprint(value)
print(len(value))
