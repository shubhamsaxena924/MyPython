start=int(input("Enter the start of the range to print prime numbers: "))
end=int(input("Enter the end of the range to print prime numbers: "))
for i in range(start,end+1):
    if(i==2):
        print(i)
    elif(i%2==0):
        pass
    else:
        for j in range(3,int(i**(1/2))+1,2):
            if(i%j==0):
                break
        else:
            print(i)
