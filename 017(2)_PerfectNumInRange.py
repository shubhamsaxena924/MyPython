start=int(input("Enter the start of the range to find PERFECT NUMBER: "))
end=int(input("Enter the end of the range to find PERFECT NUMBER: "))
for n in range(start,end+1):
    sum=0
    for i in range(1,n//2+1):
        if(n%i==0):
            sum=sum+i
        if(sum>n):
            break
    if(n==sum):
        print(n,"is PERFECT Number.")
