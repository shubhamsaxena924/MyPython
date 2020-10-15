for _ in range(int(input("Enter the number of testcases: "))):
    num1=int(input("Enter the first nummber: "))
    num2=int(input("Enter the second number: "))
    hcf=1
    n=num1 if num1<num2 else num2   #ternary operator
    for i in range(2,n+1):
        if(num1%i==0 and num2%i==0):
            hcf=i
    print("HCF of",num1,"and",num2,"is:- ",hcf)
