start=int(input("Enter the start of the range to find ARMSTRONG NUMBER: "))
end=int(input("Enter the end of the range to find ARMSTRONG NUMBER: "))
for n in range(start,end+1):
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
