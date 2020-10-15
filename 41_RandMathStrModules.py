#Modules and inbuilt functions

##1 Random Module
import random as r
print("Random Module:")
print(r.random())                   #return a random float number 15 digits after . between 0 <= x < 1
print(r.randint(0,15))              #returns a random integer in a given range. From 0 to 15 inclusively
print(r.uniform(0,15))              #returns a random float number 15 digits after . in a given range
print(r.choice("Shubham"))          #returns random element from a sequence
print(r.randrange(15,18,2))         #returns a random integer from start to end-1 with specified steps
l=[1,2,3,4]
print("Original list: ",l)
print(r.shuffle(l))                 #returns None, shuffles a list, changes original
print("After shuffling: ",l)
#print(r.shuffle("Shubham"))        #Error as str is immutable



##2 Math Module
from math import *
print("\n\nMath Module:")
print(ceil(2.1))                    #returns nearest greater integer
print(floor(2.9))                   #returns nearest smaller integer
print(fabs(-1.52))                  #returns a float absolute value of float number
print(factorial(10))                #returns factorial of a integer
print(copysign(-4,-2))              #returns value of a but sign of b; -4.0 is returned here
print(gcd(5,2))                     #returns gcd-greatest common divisor; hcf
print(exp(4.5))                     #returns e**4.5
print(2**10)                        #int if both operands are int
print(pow(2,10))                    #returns 2**10, float even if both arguments are int
print(sqrt(15))                     #returns a square root of a number in float
print(log(5.2,2.5))                 #returns log of 5.2 with base 2.5, if base is not given then natural log is computed
print(log(17,2))
print(log2(17))                     #returns log of 17 with base 2 more accurately
print(log(121,10))
print(log10(121))                   #returns log of 121 with base 10 more accurately
print(sin(0))                       #sin of an angle in radians
print(cos(1.5707963267948966))      #cos of an angle in radians
print(tan(pi/2))                    #tan of an angle in radians
print(hypot(3,4))                   #hypotenuse in float
print(degrees(pi/2))                #returns degrees of radians; pi is a constant in math module = 3.141592
print(radians(e**8))                #returns radians of degrees; e is a constant in math module = 2.718281



##3 String Module
#Mostly covered in StringOperations.py
#isalum, islapha, isdecimal, isdigit, isidentifier, isspace, isupper, replace, find, index, rindex, rfind, split, capitalize, lower, upper, swapcase, title, count, split, rsplit,
s="Shubham Saxena"
print("\n\nString Module:")         #We need not import string, these are attributes related to String object
print(s.startswith("Sh"))           #True if a string starts with a specified substring
print(s.endswith("as"))             #True if a sring starts with a specified substring
s="       Shubham Saxena          \n"
print(s.rstrip())                   #Returns a string after removing the spaces from the right side of the String
print(s.lstrip())                   #Returns a string after removing the spaces from the left side of the string
print(s.strip())                    #Returns a string after removing the spaces from both sides of the string
