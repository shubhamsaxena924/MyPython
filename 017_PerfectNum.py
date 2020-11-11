n=int(input("Enter a number to check whether it is PERFECT or NOT: "))
sum=0
for i in range(1,n//2+1):
    if(n%i==0):
        sum=sum+i
    if(sum>n):
        break
if(n==sum):
    print(n,"is PERFECT Number.")
else:
    print(n,"is NOT a PERFECT Number.")
