def sum_ls(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+sum(l[1:])
print("This program will calculate sum of all elements of a list. ")
ls=[]
ch='1'
while(ch=='1'):
    ls.append(int(input("Enter the number to append to list: ")))
    ch=input("\n\nPress '1' to add more  ")
print("List: ",ls)
print("Sum of all elements of the list: ",sum_ls(ls))
