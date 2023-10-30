#UTH - Nhap mon CNTT

"""
Assignment 2.2 - Float calculator
1.  Write a program that asks the user to enter two float numbers and display output in following format:

Sample Output:

a     b     a+b a-b   a*b           a/b     sqrt(a)

5.5  4.0  9.5  1.5   22.0    1.38     2.345
"""

import math
firstNum = float(input("Type the first number(a Num) that you want to calculate: "))
lastNum = float(input("Type the first number(b num) that you want to calculate: "))

print("First Number from user: " + str(firstNum))
print("Last Number from user: " + str(lastNum))

sumFunc = firstNum + lastNum
minusFunc = firstNum - lastNum
multiFunc = firstNum * lastNum
divideFunc = firstNum / lastNum


print("Sum: " + str(sumFunc))
print("Subtraction: " + str(minusFunc))
print("Multiplication: " + str(multiFunc))
print("Division: " + str(divideFunc))
print("Can bac hai cua so a: " + str(math.sqrt(firstNum)))



