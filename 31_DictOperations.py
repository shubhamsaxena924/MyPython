d={}                        #creates empty dictionary, and dictionaries are mutable
d[1]=20                     #d[key]=value, keys and values can be of heterogenous type
d[2]=30                     #keys cannot be duplicate and there is no such boundation on value.
d={1:50,1:30,2:30}          #Error will not be there, but d will actually be d={1:30} as 1 is updated with 30
print(d)                    #{1:30,2:30}
d[3]=50
print(d)
for x in d:                 #iterates for keys
    print("Key:",x,"    Value:",d[x])
#print(d[11])               #Error: Key Error
print("List of Keys is:             ",d.keys())           #returns list of keys and prints
print("List of Values is:           ",d.values())         #returns list of values and prints
print("List of key-value pair:      ",d.items())          #returns list of tuples of key-value pair
for x in d.items():         #iterates for list of tuples of key-value pair
    print("Key:",x[0],"   Value:",x[1])
for a,b in d.items():       #iterates for list of tuples, a stores element at index 0 of tuple-->keys and b stores element at index 1 of tuples-->values
    print(a,b)
print(d.get(4,None))        #if 4 is a key present in d then it will be returned otherwise None(default_value) will be returned; To save from Key Error
a=dict()                    #creates empty dictionary same as a={}
a[15]=2
print("d:",d)
print("a:",a)
a.update(d)                 #update a with entries present in d but not in a
print("Updated a:",a)
d.clear()                   #empties a dictionary
print("After clear() d=",d)
d=a.copy()                  #copy elements of a in d
print("Copied from a, now d=",d)
