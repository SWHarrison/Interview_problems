def longest_path():

    matrix = [
    [1,2,9],
    [5,3,8],
    [4,6,7]
    ]

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):

            current_num = matrix[r][c]
            path_num = longest_path_helper(r,c,matrix)
            path = list(range(current_num,current_num + path_num))
            print(current_num, "path", path)


def longest_path_helper(r,c,matrix):

    if r + 1 < len(matrix) and matrix[r+1][c] == matrix[r][c] + 1:
        return 1 + longest_path_helper(r+1,c,matrix)
    if r - 1 >= 0 and matrix[r-1][c] == matrix[r][c] + 1:
        return 1 + longest_path_helper(r-1,c,matrix)
    if c + 1 < len(matrix[r]) and matrix[r][c+1] == matrix[r][c] + 1:
        return 1 + longest_path_helper(r,c+1,matrix)
    if c - 1 >= 0 and matrix[r][c-1] == matrix[r][c] + 1:
        return 1 + longest_path_helper(r,c-1,matrix)

    return 1

longest_path()
