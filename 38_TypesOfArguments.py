#-->Types of function arguments:
    #1  Positional arguments:- Assigned according to position of arguments in funtion definition.
    #2  Default arguments:- If user doesnot provide all the arguments, then function uses default values for those varibales.
    #3  Keyword arguments:- If someone doesnot remember the order to pass arguments, argument names are used in function calling to assign value in any order.
    #4  Variable number of arguments:- Some function may be needed that take variable number of arguments.

#Default Arguments
def sum(a,b=0):
    c=a+b
    print(c)
sum(0)            #a=0,b=0
sum(1)            #a=1,b=0
sum(10,20)        #a=10,2b=20

#Keyword Arguments
def sum(name,age,address):
    print(name,age,address)
sum(age=10,name="Shubham",address="Narora")

#Variable number of Arguments
def sum(*n):      #internally arguments are stored as tuple
    print(type(n))#tuple
    total=0
    for x in n:
        total=total+x
    print(total)
sum()
sum(4,1,3,2)
sum(1,2,3,4,5,6)
