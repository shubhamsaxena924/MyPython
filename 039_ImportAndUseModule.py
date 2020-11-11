import ModuleFactSum as p               #Stored in same file as the current file, Name should be as it is (no change in case), extension of the module file should be .py
print("Factorial of 4 is:",p.fact(4))
print("Sum of 1 and 2 is:",p.sum(1,2))

from ModuleFactSum import sum           #when we import function instead of the whole module, then we dont have to specify the name of the module while calling the function, if we specify then it will give error.
print("Sum of 1 and 2 is:",sum(1,2))
#print("Factorial of 4 is:",fact(4))    #Error: fact not defined

from ModuleFactSum import *             #Import * means import everything, we dont have to specify name of the module in function calling.
print("Factorial of 4 is:",fact(4))
print("Sum of 1 and 2 is:",sum(1,2))
