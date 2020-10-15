for _ in range ( int(input("Enter the num of testcases: ")) ) :
    n=int(input("Enter the num of terms in the series 1 + 1/2! + 1/3! + ... + 1/n! : "))
    sum=0
    for i in range ( 1 , n + 1) :
        fact = 1
        for j in range ( 1 , i + 1 ) :
            fact = fact * j
        sum = sum + (1 / fact)
    print(sum)
