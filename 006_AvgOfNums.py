for _ in range(int(input("Enter the num of testcases: "))):
    n=int(input("Enter number of values: "))
    sum=0
    for i in range(n):
        sum=sum+int(input("Enter a number: "))
    avg=sum/n
    print("Average of the",n,"numbers you entered is: ",avg)
