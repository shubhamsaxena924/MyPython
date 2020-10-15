a=[1,1,2,3,4,2,5,6,7]
print(len(a))           #printed
a.insert(2,4)
a                       #returns list but not stored or Printed
print(a.insert(2,4))    #printed "None"
print(a)                #printed
len(a)
a.remove(1)             #not printed, removes 1 if present otherwise error
print(a.remove(1))      #printed "None"
print(a)                #Printed
print(a.append(1))      #Printed "None"
print(a.append(1))      #Printed "None"
print(a)                #Printed
a.pop()                 #Nothing printed but pops last element and is returned but not stored or printed
print(a)                #Printed
print(a.pop())          #last element printed
print(a.pop(3))         #element at 3 index printed
#print(a.pop(11))       #IndexError: pop index out of range
print(a.pop(-2))        #Negative indexing, no error
a.insert(-2,6)
print(a)                #printed
a.count(2)
print(a.count(4))       #prints count of 4
a.insert(15,3)          #inserts at last even if index is out of range
print(a)                #printed
print(a.insert(-18,3))  #prints "None" and inserts at beginning if index is below negative indexing range
print(a)                #Printed
#a.pop(-18)             #IndexError: pop index out of range
b=[]
#b.pop()                #IndexError: pop from empty list
print(a.index(2))       #Printed; returns index of 2 if present, otherwise ValueError: ... is not in list
b.append(10)
b.append(11)
print(b)                #printed
a.extend(b)             #extends a with elements of b at the end
print(a.extend(b))      #Printed "None" and extends a with elements of b at the end
print(a,b)              #Printed, a and b
a+b                     #returns concatenated a and b but not stored, used or printed
print(a+b)              #returns concatenated a and b and printed but not stored
print(a,b)              #No change after concatenation in original lists
a=a+b                   #a is replaced with concatenated list a+b
print(a)                #printed
a=a*4                   #multiplies list; same as string
print(a)                #Printed
a.sort()                #sorts a list in ascending order
print(a)                #printed
print(a.sort(reverse=1))#sorts and updates the original list in descending order, Prints "None"... Sort method is only for lists
print(a)                #printed
c=sorted(a)             #No change in original; returns a sorted list and can be displayed and stored in variable. General function to sort any data type.
print(a)                #Printed
print(c,"List C")       #printed
c=sorted(c,reverse=True)#Sorted in descending order and then stored in itself
print(c,"List C")       #Printed
