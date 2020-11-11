s1=set()                 #empty set created using set(); {} will create a dictionary
print(type(s1))          #set; Set has no duplicate entries and it is unordered
d={}
print(type(d))           #dictionary
s1={1,2,3}
print("Set s1: ",s1)
s2=set([2,3,4])
print("Set s2: ",s2)

print("\n\nIntersection of s1 and s2 & s2 and s1 is same: ")
print(s1.intersection(s2))          #returns intersection
print(s2&s1)                        #returns intersection

print("\n\nUnion of s1 and s2 & s2 and s1 is same: ")
print(s1.union(s2))                 #returns union
print(s1|s2)                        #returns union

print("\n\nDifference of s1 and s2 & s2 and s1 is different: ")
print(s1.difference(s2))            #returns difference:- present in s1 but not in s2
print(s2-s1)                        #returns difference

print("\n\nSymmetric difference of s1 and s2 & s2 and s1 is same: ")
print(s1.symmetric_difference(s2))  #returns symmetric difference:- present only in s1 or s2
print(s1^s2)                        #returns symmetric difference

print("\n\nUpdate(): ")
print(s1.update(s2))                #updates s1 with elements present in s2 but not in s1, returns None; Changes original
print("Set s1 after updating with s2: ",s1)

print("\n\nRemove(): ")
print(s1.remove(4))                 #removes a particular element, returns None; changes original
print("Set s1 after removing 4: ",s1)
#print(s1.remove(5))                #Error: Key Error as 5 is not present in s1

print("\n\nClear(): ")
s1.clear()                          #returns None; changes original
print("Set s1 after clearing: ",s1)

print("\n\nIssubset() and add(): ")
print(s1.issubset(s2))              #True if s1 is subset of s2
s1.add(1)                           #adds 1 in s1 set, changes original; returns None
s1.add(5)
print("Set s1 after adding 1 and 5: ",s1)
print(s1.issubset(s2))              #False if s1 is not a subset of s2

print("\n\nissuperset(): and pop(): ")
print(s2.issuperset(s1))            #False if s2 is not a superset of s1
print(s2.issuperset(s1))
s2.add(1)

s1.remove(5)
print("Set s2 after adding 1: ",s2)
print("Set s1 after adding 1 and removing 5: ",s1)
print(s2.issuperset(s1))            #True if s2 is a superset of s1
