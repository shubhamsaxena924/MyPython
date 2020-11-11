#PVM:- Python Virtual Machine; Checks for any syntax errors when we execute a program.
#Exceptions:- Run-Time Errors are also known as Exceptions.
#Exceptional Handling is important to prevent wastage of resources(CPU and Memory) and terminate program gracefully.
##Ex:-
try:
    x=int(input())
    y=int(input())
    print(x/y)
except ZeroDivisionError:
    print("Enter a non-zero number!!")
except ValueError:
    print("Enter valid number")
except:                                                 #For KeyboaardInterruptError for example; Default except should be at last otherwise it will be an error.
    print("Other Error")
finally:
    print("Finally Block")
#ZeroDivisionError and ValueError are types of ArithmeticError
#We can also group different types of error in one except using comma.
#try: Risky Code        except: Alternate code of there is error in try block                   finally: Always executed, no matter whether try or except is/are executed or not, exit() will also not work.

##Raising error explicitly
try:
    n=int(input("Enter a number: "))
    if(n>0):
        print(n)
    elif(n==0):
        raise ValueError("No. cannot be 0  ")           #Providing explicit message to error.
    elif(n<0):
        raise ValueError("No. cannot be negative  ")
except ValueError as msg:
    print(msg)
    print(type(msg))
