# Given a base-10 integer,n , convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum
# number of consecutive 1's in n's binary representation.

d = int(input())
n = 0
max = 0
while(d > 0):
    remainder = d % 2
    d = d//2
    if remainder == 1:
        n = n+1
        if n > max:
            max = n
    else:
        n = 0
print(max)
