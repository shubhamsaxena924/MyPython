a="I'm Shubham Saxena. And I am from Narora.And I am a B. Tech Student."

#Converting list to string and vice-versa
l=list(a)                               #Will create a list l; each character of string a will be a different element of the list
ls=l
print("\nList L: ",l)
l=''.join(l)                            #Convert the list back to string and store to l variable.
print("\nString L using ''.join(): ",l)
ls='$'.join(ls)                         #Convert the list back to string with $ between each element-junction.{Each character in this case.}
print("\nString LS using '$'.join(): ",ls)

#converting list to string and vice-versa using loops
b='s'
l2=[1,2,3,4,b]
s=''
for i in l2:
    s=s+str(i)
print("\n\nString from list using loop: ",s)
l3=[]
for i in s:
    try:                                #to avoid error if character comes in int()
        l3.append(int(i))
    except:
        l3.append(i)
print("List from string using loop: ",l3)

#find(),rfind(),index(),rindex(),count()
print("\n\nFirst 'And' in String A is at place: ",a.find('And'))  #returns index of the first character of the first occurence of a specified substring in the specified string
print("Second 'And' in the String A is at place: ",a.find('And',21,len(a)+1))   #We can specify the index range in the string where we want to search our substring.
print("Result of finding 'and' in String A: ",a.find('and'))      #find() is case-sensitive. If there is no match, the function returns -1.
print("First 'am' from the end of the string is at place: ",a.rfind('am'))      #rfind() searches the substring from the end of the main string.
print("First 'am' from the beginnning of the string: ",a.index('am'))           #index(),rindex() give error if there is no match, unlike find(),rfind() which return -1, so it is better to check beforehand using 'in'
print("First 'And' from the end of the string is at place: ",a.rindex('And'))   #rindex() searches from the end
print("Number of And in String A: ",a.count('And'))


#Slice Operator: for both list and string
add1,add2=0,0
if 'And' in a:
    add1=a.find('And')                  #Address of first 'And'
if 'And' in a[add1+1:]:                 #Check if there is any othe 'And' after index of first 'And'
    add2=a.find('And',add1+1)           #find 'And' after first occurence
print("\n\nAddress 1: ",add1,"\nAddress 2: ",add2)
print(a[add2+2:add2-1:-1])              #printing second 'And' in reverse; Actual-background end position is end+1 in negative steps {let end be the position specified in operator by user}
print(a[add2:add2+len('And')])          #printing second 'And'; Actual-background end position is end-1 in positive steps {end--> position specified in operator by user}
print(a[::-1])                          #prints whole string in reverse
print("Number of And after its first occurence in String A: ",a.count('And',add1+1,))

#Replace function
x=a.replace('Shubham Saxena','Priya   Jain')                    #No change to original string
print("\n\nNew string with replacement is: ",x)
print(x.replace('','|'))                #It puts '|' between each character; even between multiple spaces.
x=x.replace('  ','')                    #There is no remove or pop function; replace() have replaced them(Haha!); This statement will remove extra two spaces between 'Priya ' and 'Jain'
print(x)
print(x.replace(' am',"'m",1))          #It will only replace first occurence of ' am'
print(x[:add1+1]+x[add1+1:].replace('And','Also,',1))           #This will replace only second 'And'

#Formatting Functions
strls=a.split()                         #splits a string according to a specified separator, secod=nd argument specifies how much splits to perform, by default its value is -1  which means all occurences
strls[1]=strls[1].upper()               #Will block the First Name
strls[2]=strls[2].lower()               #Will lower the Sur Name
strls[6]=strls[6].capitalize()          #Will capitalize the first letter of string 'from'
strls[3]=strls[3].swapcase()            #Will swap the cases of 'And'
x=' '.join(strls)
print("\n\n",x,sep='')
x=x.title()
print(x)
