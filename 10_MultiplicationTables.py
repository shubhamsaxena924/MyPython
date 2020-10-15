a=int(input("Enter the start of multiplication tables: "))
b=int(input("Enter the end of multiplication tables: "))
c=int(input("Till what number do you want to multiply each number: "))
for i in range(a,b+1):
    print("Multiplication table of",i,"is: ")
    for j in range(1,c+1):
        print(i,"x",j,"=",i*j)
    print(end="\n\n\n")
