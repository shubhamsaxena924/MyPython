#Program that will return expanded form of a4b5c as aaaabbbbbc...
a=input("Enter a string in format such as: a3b4c, ab1, a3b4 ; {a char & a 1-digit num w/out any space}  :    ")
l=list(a)
for i in range(len(l)):
    if(l[i].isdigit()):
        l[i]=l[i-1]*(int(l[i])-1)
a=''.join(l)
print("Expanded form is: ",a)


#Program that will return contracted form of aaaabbbbbc as a4b5c...
s=input("Enter a pattern string in format such as: aaabbbbcccc, aaabbaaccbbaa;  :    ")
s2=''
for i in range(len(s)):
    if(i==0 or s[i]!=s[i-1]):       #for first character or if a new character is encountered in string.
        s2=s2+s[i]
    elif s[i]==s[i-1]:              #if previous character was same as the current character
        if s2[-1].isdigit():        #if there are more than 2 same character, aa'a'... or aaa'a'... and so on
            count=int(s2[-1])+1
            s2=s2[:len(s2)-1]+str(count)
        elif s2[-1].isalpha():      #if we encounter the same character 2nd time, a'a'...
            s2=s2+'2'
s=s2
print("Contracted form is: ",s)
