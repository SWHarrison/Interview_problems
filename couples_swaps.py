'''
N couples sit in 2N seats arranged in a row and want to hold hands.
We want to know the minimum number of swaps so that every couple is
sitting side by side. A swap consists of choosing any two people, then
they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the
couples are numbered in order, the first couple being (0, 1), the
second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of
the person who is initially sitting in the i-th seat.
'''

# helper to check if couples are sitting adjacent
def check_couples(row):
    out_of_place = 0
    for i in range(0,len(row),2):

        #print("indices",i, i + 1)
        person_A = row[i]
        person_B = row[i+1]
        #print("persons", person_A, person_B)

        if abs(person_A - person_B) != 1 or max(person_A,person_B) % 2 != 1:
            print(person_A, person_B, "are not couples")
            out_of_place += 1

    return out_of_place - 1 if out_of_place > 0 else 0

def minSwapsCouples(row):
    """
    :type row: List[int]
    :rtype: int
    """
    seats = {} # store the two people on couch i
    cur_pos = {} # store the couch person x is sitting now
    for i in range(0, len(row), 2):
        seats[i] = [row[i], row[i+1]]
        cur_pos[row[i]] = i
        cur_pos[row[i+1]] = i

    # check each couch, if the two people are already couple, skip
    # otherwise iteratively find the partner for the small one
    ans = 0
    for i in range(0, len(row), 2):
        print("seats",seats)
        print("curr",cur_pos,"\n")
        x, y = seats[i]
        if x > y:
            x, y = y, x
        if x % 2 == 0 and y % 2 == 1:
            continue
        pre = i
        print(x,y)
        while not (x % 2 == 0 and y % 2 == 1): # not couple yet
            print("inner loop seats",seats)
            print("inner loop curr",cur_pos,"\n")
            ans += 1
            partner = (x+1) if x % 2 == 0 else (x-1)
            partner_cur_pos = cur_pos[partner]
            seats[pre] = [x, partner]
            seats[partner_cur_pos].remove(partner)
            seats[partner_cur_pos].append(y)
            cur_pos[y] = partner_cur_pos
            cur_pos[partner] = pre
            pre = partner_cur_pos
            x, y = seats[pre]
            if x > y:
                x, y = y, x
    return ans

row = [1,4,8,7,6,3,2,9,0,5]
#     [1,0,4,5,8,7,6,3,2,9] swap 0 and 4
#     [1,0,4,5,8,9,6,3,2,7] swap 7 and 9
#     [1,0,4,5,8,9,2,3,6,7] swap 6 and 2
#row_2 = [3, 2, 0, 1]

print(minSwapsCouples(row))

#print(check_couples(row))
#print(check_couples(row_2))
