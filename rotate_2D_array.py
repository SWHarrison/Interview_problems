def rotate(matrix):

    start_index = 0
    end_index = len(matrix) - 1

    # number of boxes
    while start_index < end_index:

        pos1 = [start_index,start_index]
        pos2 = [start_index,end_index]
        pos3 = [end_index,end_index]
        pos4 = [end_index,start_index]

        #print("rotation positions", pos1,pos2,pos3,pos4)
        # number of groups of 4
        for i in range(start_index, end_index):
            # 4 rotations for each group
            temp1 = get(matrix,pos1)
            temp2 = get(matrix,pos2)
            temp3 = get(matrix,pos3)
            temp4 = get(matrix,pos4)
            #print("to rotate",temp1,temp2,temp3,temp4)
            matrix[pos1[0]][pos1[1]] = temp4
            matrix[pos2[0]][pos2[1]] = temp1
            matrix[pos3[0]][pos3[1]] = temp2
            matrix[pos4[0]][pos4[1]] = temp3

            #print(matrix)

            pos1[1] += 1
            pos2[0] += 1
            pos3[1] -= 1
            pos4[0] -= 1

        start_index += 1
        end_index -= 1

    #print(matrix)


def get(matrix, pos):

    return matrix[pos[0]][pos[1]]

#to_rotate = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
to_rotate = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
rotate(to_rotate)
print(to_rotate)
