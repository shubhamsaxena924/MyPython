for i in range(int(input("Enter num of testcases: "))):
    n=int(input("Enter a num to find sum of its digits: "))
    sum=0
    num=n
    while(num>0):
        dig=num%10
        sum=sum+dig
        num=num//10
    print("The sum of digits of the number",n,"is",sum)





# NOTE: Program 2
for i in range(int(input("Enter num of testcases: "))):
    n=input("Enter a num to find sum of its digits: ")
    sum=0
    for i in n:
        dig=int(i)
        sum=sum+dig
    print("The sum of digits of the number",n,"is",sum)
