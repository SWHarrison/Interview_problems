def gray_code(n):

    if n <= 0:
        return []

    code = ["0","1"]

    for i in range(0,n):

        code_reversed = code[::-1]
        code = code + code_reversed
        for j in range(len(code)//2):
            code[j] += "0"
        for j in range(len(code)//2, len(code)):
            code[j] += "1"

        print(code)

    return code

gray_code(5)
