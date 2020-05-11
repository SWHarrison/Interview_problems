def fast_trailing_zero_factorial(n):

  num_zeros = 0

  for i in range(n+1):

      num = i
      while(num//5 == num/5 and num > 1):
          num_zeros += 1
          num /= 5

  return num_zeros

for i in range(0,101):

    print(str(i) + "! has this many trailing 0: " + str(fast_trailing_zero_factorial(i)))
