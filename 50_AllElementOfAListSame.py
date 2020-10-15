#Program 1 to check if all elements of a list are identical
def check(list):
   return list[1:] == list[:-1]

# Driver code
print(check(['a', 'b', 'c']))
print(check([1, 1, 1]))

#Program 2
def check(list):
    s=set(list)
    return True if len(s)==1 else False
print(check(['a', 'b', 'c']))
print(check([1, 1, 1]))

#Program 3
def check(list):
    return True if list.count(list[0])==len(list) else False
print(check(['a', 'b', 'c']))
print(check([1, 1, 1]))
