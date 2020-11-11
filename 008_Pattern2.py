for _ in range(int(input("Enter the num of testcases: "))):
    n=int(input("Enter a num for pattern: "))
    for i in range(n):
        print((n-i)*" ",end="")
        print(i*"*_",end="*")
        print()
    for i in range(n):
        print((i+1)*" ",end="")
        print((n-i-1)*"*_",end="*")
        print()
