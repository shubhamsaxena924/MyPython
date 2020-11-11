#Lambda or Anonymous(without name) functions:- Functions only for instant use.
##Syntax:- lambda input:output
s=lambda a,b:a+b
print(s(int(input("Enter a number: ")),int(input("Enter other number: "))))

x=lambda :int(input("\n\nEnter a number to square: "))**2
print(x())


#Functions that take another functions as arguments
    #1  filter()    :   to apply condition or filter a sequence
    #2  map()       :   executes a specified function for each item in a interable.
    #3  reduce()    :   executes a speci. func. for each item in a seq. It is in functools module. Internally, it take 1st 2 elem. of the seq., executes the func. and the result value is executed along with the next value of the seq.


##filter()
def evenhaikya(n):
    if n%2==0:
        return 1
    else:
        return 0
l=[10,20,11,21,45,6,52,41,3]
l=filter(evenhaikya,l)
print("\n\nFilter(): ",type(l))
l=list(l)
print(l)


##map()
def f(x):
    return x*10
l=[1,2,3,4]
m=map(f,l)                    #alternative: m=list(map(lambda x:x*10,l))
print("\n\nMap(): ",type(m))
m=list(m)
print(m)

m=list(map(int,input("\nEnter space-separated numbers for list 1: ").split()))
s=list(map(int,input("\nEnter space-separated numbers for list 2: ").split()))
print(m)
print(s)
l=list(map(lambda x,y:x*y,m,s))
print(l)


##reduce()
from functools import reduce
l=[1,2,3,5,4]
m=reduce(lambda a,b:a+b,l)
print("\n\nReduce(): ",type(m))
m=int(m)
print(m)
