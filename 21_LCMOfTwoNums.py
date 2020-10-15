a=int(input("Enter the first number to find LCM: "))
b=int(input("Enter the second number to find LCM: "))
hcf=1
min= a if a<b else b
for i in range(2,min+1):
    if(a%i==0 and b%i==0):
        hcf=i
lcm=(a*b)//hcf
print(lcm)

#Program 2, core logic, but less efficient then Program 1
a=int(input("Enter the first number to find LCM: "))
b=int(input("Enter the second number to find LCM: "))
max= a if a>b else b
while(True):
    if(max%a==0 and max%b==0):
        lcm=max
        break
    max=max+1
print(lcm)
