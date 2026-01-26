# Program to print a symmetric number pyramid pattern
# Demonstrates: Nested for-loops, string concatenation, and spacing logic
# Author: Kavya (Dr. AIT, ECE)

n = int(input())

# Part 1: Increasing Pyramid
k = 1
z = n - 1
for i in range(n):
    row_str = ""
    for j in range(1, k + 1):
        row_str = row_str + str(j) + " "
    
    leading_spaces = " " * z
    print(leading_spaces + row_str)
    k += 1
    z -= 1

# Part 2: Decreasing Pyramid
o = n
f = 1
for i in range(1, n):
    row_str = ""
    for j in range(1, o):
        row_str = row_str + str(j) + " "
    
    leading_spaces = " " * f
    print(leading_spaces + row_str)
    o -= 1
    f += 1