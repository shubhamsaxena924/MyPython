#Program to check if two strings are cyclic permutations
s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
if(len(s1)==len(s2)):
    n=s1+s1
    if(n.find(s2)!=-1):
        print("Yes, they are cyclic permutations")
    else:
        print("No, they are not cyclic permutations")
else:
    print("Sorry! Unequal lengths")
