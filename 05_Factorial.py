for _ in range(int(input("Enter num of testcases: "))):
    start=int(input("Enter start num of range, for factorial: "))
    end=int(input("Enter end num of range, for factorial: "))
    print("Factorial of: ")
    for n in range(start,end+1):
        a=1
        for i in range(1,n+1):
            a=a*i
        print(n," is ",a)
