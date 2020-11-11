#Print index of all the occurences of substring
a=input("Enter the main string: ")
b=input("Enter the substring to search for: ")
c=0
while(a.find(b,c,len(a)+1)!=-1):
    d=a.find(b,c)
    print(d)
    c=d+1


#Program 2
s=input("Enter the main string: ")
s2=input("Enter the substring to search for: ")
if(s2 not in s):
    print("Not Found! ")
add=0
for i in range(s.count(s2)):
    add=s.find(s2,add)
    print(add)
    add=add+1                           #to search after address of previous match
