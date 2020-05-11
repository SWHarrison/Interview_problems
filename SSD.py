def sum_of_squares(k, b, n):

    to_return = 0
    while n != 0:
        remainder = n % b
        n = int(n / b)
        to_return += remainder * remainder

    print(k,b,to_return)



# read first line
'''number_of_lines = int(input())

# read all remaining lines
for i in range(number_of_lines):
 line = input()
 args = line.split();
 k = int(args[0]);
 b = int(args[1]);
 n = int(args[2]);

 sum_of_squares(k, b, n)'''

print(sum_of_squares(1,10,1234))
print(sum_of_squares(2,3,98765))
print(sum_of_squares(3,16,987654321))
