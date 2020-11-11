import math
import time
a=int(input("Enter a num:       "))
start=time.time()
n=int(math.log(a)/math.log(10)+1)
print("No. of digits:               ", n)
first=a//(10**(n-1))
print("First digit:                 ",first)
last=a%10
print("Last digit:                  ",last)
d=a//10
c=d%(10**(n-2))
print("Middle part:                 ",c)
print("Number after operation:      ",last*(10**(n-1))+(c*10)+first)
end=time.time()
print("Time taken ",end-start)




# NOTE: Program 2
import math
import time
a=input("Enter a num:       ")
start=time.time()
first=a[0]
last=a[-1]
middle=a[1:-1]
print("First digit:                 ",first)
print("Last digit:                  ",last)
print("Middle part:                 ",middle)
print("Number after operation:      ",int(last+middle+first))
end=time.time()
print("Time taken ",end-start)
