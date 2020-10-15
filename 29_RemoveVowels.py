#Remove vowels from a String
s=input("Enter your String:  ")
s2=''
for i in s:
    if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
        s2=s2+i
s=s2
print("String after removing vowels from it: ",s)



#Program 2
s=input("Enter your String:  ")
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        s=s.replace(i,'')
    if 'a' not in s and 'e' not in s and 'i' not in s and 'o' not in s and 'u' not in s:
        print("Done!")
        break
print("String after removing vowels from it: ",s)
