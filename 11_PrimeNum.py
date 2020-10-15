n=int(input("Enter a number: "))
for x in range(2,int(n**(1/2))+1):
    if(n%x==0):
        print("The number is NOT PRIME.")
        break
else:
    print("The number is PRIME.")



# NOTE: Program 2, more efficient
n=int(input("Enter a number to check whether it is PRIME or not: "))
if(n==2):
    print("The number is PRIME.")
    exit()
if(n%2==0):
    print("The number is NOT PRIME.")
    exit()
for i in range(3,int(n**(1/2))+1,2):
    if(n%i==0):
        print("The number is NOT PRIME.")
        break
else:
    print("The number is PRIME.")


# NOTE: Program 3, C-language approach
n=int(input("Enter a number: "))
c=0
for x in range(2,int(n**(1/2))+1):
    if(n%x==0):
        c=1
        break
if(c==0):
    print("The number entered is PRIME.")
else:
    print("The number entered is NOT PRIME.")
