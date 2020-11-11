a=input("Enter the number: ")
b=""
for i in a:
    b=b+i
    print(b)
c=len(a)
for i in range(c):
    print(b[0:c-i])
