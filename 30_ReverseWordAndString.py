#Reverse each word of the String
s=input("Enter your string: ")
ls=s.split()
for i in range(len(ls)):
    ls[i]=ls[i][::-1]
s=' '.join(ls)
print("String after reversing each word: ",s)

#Reverse whole String using loop
s=input("Enter your string: ")
s2=''
for i in s:
    s2=i+s2
s=s2
print("Reversed String is: ",s)

#Reverse whole string using slice operator
s=input("Enter your string: ")
s=s[::-1]
print("Reversed string is: ",s)

#Reverse whole string using reversed() function: Function that iterates a sequence(str,list etc.) in reverse order
s=input("Enter your string: ")
s2=''
for i in reversed(s):
    s2=s2+i
s=s2
print("Reversed String is: ",s)
