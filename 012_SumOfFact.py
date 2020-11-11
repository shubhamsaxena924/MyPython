for _ in range(int(input("Enter the number of testcases: "))):
    n=int(input("Enter the number of terms you want in the series 1! + 2! + 3! + ... + n! : "))
    sum=0
    for i in range(1,n+1):
        fact=1
        for j in range(2,i+1):
            fact=fact*j
        sum=sum+fact
    print("The sum of the series upto",n,"terms is",sum)
