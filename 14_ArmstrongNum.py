n=int(input("Enter the num to check whether it is ARMSTRONG or NOT: "))
b=n
c=0
sum=0
while(b>0):
    b=b//10
    c=c+1
b=n
for i in range(n):
    dig=b%10
    b=b//10
    sum=sum+dig**c
if(sum==n):
    print(n,"is ARMSTRONG NUMBER")
else:
    print("The number is not ARMSTRONG")
