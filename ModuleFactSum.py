#function to calculate factorial
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


#function to calculate sum of numbers
def sum(*n):      #internally arguments are stored as tuple
    total=0
    for x in n:
        total=total+x
    return(total)
