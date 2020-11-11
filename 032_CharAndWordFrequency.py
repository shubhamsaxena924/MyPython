#Frequency of each character
s=input("Enter a string to count frequency of each character: ")
d={}
for i in s:
    if(i==' ' or i in d):   #avoid space and skip if a character has already been counted; To make more effective make set of characters and break if all chars in set have been counted and stored in d
        continue
    d[i]=s.count(i)
for i,j in d.items():
    print("Frequency of",i,"=",j)


#Frequency of each word
s=input("Enter a string to count frequency of each word: ")
d={}
for i in s.split():
    if i in d:
        continue
    d[i]=s.count(i)
for i,j in d.items():
    print("Frequency of",i,"=",j)
