n = int(input("Enter the number of terms you want in the series...: "))
a, b = 0, 1
if(n >= 1):
    print(0)
    if(n >= 2):
        print(1)
        for i in range(n-2):
            c = a+b
            print(c)
            a = b
            b = c


# NOTE: Program 2
n = int(input("Enter the number of terms you want in the series...: "))
a, b = 0, 1
for i in range(0, n):
    if(i <= 1):
        print(i)
        continue
    c = a+b
    print(c)
    a = b
    b = c
