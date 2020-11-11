#Program to check if two strings are permutations of each other
s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
if(len(s1)!=len(s2)):
    print("Sorry! Unequal lengths")
    exit()
d1={}
d2={}
for i in s1:
    d1[i]=s1.count(i)
for j in s2:
    d2[j]=s2.count(j)
if(d1==d2):
    print("Yes, they are permutations")
else:
    print("No, they are not permutations")


#Program 2, more efficient
s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
if(len(s1)!=len(s2)):
    print("Sorry! Unequal lengths")
    exit()
a=sorted(s1)
b=sorted(s2)
if(a==b):
    print("Yes, they are permutations")
else:
    print("No, they are not permutations")
