a=int(input("Enter a number: "))
b=a
c=0
while(b>0):
    b=b//10
    c+=1
print(c)
b=a
rev=0                                 #  rev=[]
for i in range(c):                    #  for i in range(c):
    rev=rev*10+(b%10)                 #     rev.append(str(b%10))
    b=b//10                           #     b//=10
                                      #  rev=int("".join(rev))
print("Reversed number is: ",rev)
