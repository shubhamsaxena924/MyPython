for _ in range(int(input("Enter the number of testcases: "))):
    n=int(input("Enter a num to find its smallest factor other than 1: "))
    if(n%2==0):
        print(2,"is the smallest factor of",n)
    else:
        for i in range(3,n+1,2):    #till n, as it can be a prime number.
            if(n%i==0):
                print(i,"is the smallest factor of",n)
                break
