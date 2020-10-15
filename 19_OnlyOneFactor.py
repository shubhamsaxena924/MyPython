start=int(input("Enter the start of range to find numbers that only have one factor other tha 1 and itself: "))
end=int(input("Enter the end of range to find numbers that only have one factor other tha 1 and itself: "))
for i in range(start,end+1):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count=count+1
            if(count>1):
                break
    if(count==1):
        print(i)
print("\n\n\nTHANK YOU!!!")
