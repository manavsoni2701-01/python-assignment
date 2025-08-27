#Calculate a function using a factorial.
#Task 1
def factorial(n):
    result = 1
    for i in range( 1, n+1):
     result = result * i
    return result
num=int(input("Enter a number: "))

print(f"factorial of {num} is: {factorial(num)}")


#Task 2

import math
num= float(input("enter a number: "))

square_root= math.sqrt(num)
logarithm= math.log(num)
sine_value= math.sin(num)

print(f" square root: {square_root}")
print(f" logarithm: {logarithm}")
print(f" sine: {sine_value}")
