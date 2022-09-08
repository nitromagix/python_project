
#   by Martin Prost


#   Write a Python function called max_num()to find the maximum of three numbers.

def max_num(first, second, third):
    return max(first, second, third)


print(max_num(17, 56, 23))  #  56
print(max_num(13, 1, 7))  #  13
print(max_num(66, 77, 99))  #  99




#   Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(number_list, i=0):
      if len(number_list) == 0 and i == 0:
          return 0
      if len(number_list) == 0:
          return 1
      return number_list.pop(0) * mult_list(number_list, i+1)


print(mult_list([1, 2, 3, 4, 5]))  #  120
print(mult_list([]))  #  0




#   Write a Python function called rev_string() to reverse a string.

def rev_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + rev_string(s[:-1])

print(rev_string("this is a string in reverse"))  #  esrever ni gnirts a si siht




#   Write a Python function called num_within() to check whether a number falls in a given range.
#   - The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#   - Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(number, start_range, end_range):
    return number in range(start_range, end_range) or number == end_range

print(num_within(2,1,7))  #  true
print(num_within(6,6,10))  #  true
print(num_within(20,3,20))  #  true
print(num_within(15,4,13))  #  false
print(num_within(2,7,9))  #  false



#   Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#   - The function accepts the number n, the number of rows to print
#   - Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together. 

#
#
#
#       VVVVV       COPIED FROM SOLUTION!!!  I couldn't figure this out!       VVVVV
#
#
#


triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)