#Remove duplicate characters from a String
s=input("Enter your string:  ")
s2=''
for i in s:
    if i not in s2 or i==' ':           #Spaces will not be removed
        s2=s2+i
s=s2
print("The string after removing duplicates is: ",s)
