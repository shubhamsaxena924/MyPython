n=int(input("Enter a num to check whether it is STRONG or NOT: "))
b=n
sum=0
if(n==0):   #special case n=0
    sum=1
while(b>0):
    dig=b%10
    b=b//10
    a=1
    for j in range(2,dig+1):
        a=a*j
    sum=sum+a
if(n==sum):
    print(n,"is a STRONG Number.")
else:
    print(n,"is NOT a STRONG Number.")
