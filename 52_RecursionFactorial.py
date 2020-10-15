#Factorial using recursion
def f(n):
    if(n==1 or n==0):           #ending condition
        return 1
    else:
        return n*f(n-1)

n=int(input("Enter a number to find its factorial: "))
fact=f(n)
print("Factorial of",n,"is: ",fact)
