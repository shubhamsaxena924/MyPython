#Program which generated a 2D array The element X(i,j)=i*j. For ex:- x=3,y=5 --> [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]
x=int(input("Enter the value of rows: "))
y=int(input("Enter the no. of columns: "))
l=[]
for i in range(x):
    m=[]
    for j in range(y):
        m.append(i*j)
    l.append(m)
print(l)
