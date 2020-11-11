n=int(input("Enter a num: "))
c=2
if(not n%2):
    c=1
for i in range(1,n+1):
    if(i<=(n+1)/2):
        print(i*'*')
    else:
        print((i-c)*'*')
        c=c+2
