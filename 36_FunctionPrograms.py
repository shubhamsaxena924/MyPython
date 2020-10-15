#function to calculate factorial
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
z=fact(int(input("Program 1:\nEnter a number to find factorial: ")))
print(z)



#function to calculate sum of all members of a list
def sumls(l):
    sum=0
    for i in l:
        sum=sum+i
    return(sum)
print("\n\nProgram 2:\nSum of elements of list: ",sum([10,20,30]))



#function that takes tow integer and calculates there sum, difference and product
def operate(a,b):
    sum=a+b
    diff=a-b
    prod=a*b
    return sum,diff,prod
x,y=int(input("\n\nProgram 3:\nEnter x: ")),int(input("Enter y: "))
s,d,p=operate(x,y)
print("Sum is: ",s)
print("Difference is: ",d)
print("Product is: ",p)



#functioon that will remove duplicates in a list
def rem_dup(l):
    m=[]
    for i in l:
        if i in m:
            continue
        m.append(i)
    return m
print("\n\nProgram 4:\n",rem_dup([10,1,2,10,2,1,4,5,6,7,8,9,45,4,5]),sep='')
