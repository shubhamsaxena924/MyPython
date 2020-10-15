#Numpy Array. Array is set of homogenous type of elements or objects.
import numpy as np
a=np.array([10,20,30,40])
a=a-10                              #Speciality of array; Gets subtracted from each element
print(a)
print("Multiplying array a by 5:\n",5*a,sep='')     #Similarly all arithmetic operators work on each element of array
b=np.array([10,15,20,30])
print(a-b)                          #Subtracts each corresponding elemwnt
print(a.shape)
print(a.ndim)                       #1D Array
a=a.reshape(1,4)                    #It becomes 2D Array with 1 row
print(a)
print(a.shape)
print(a.ndim)
print(a.reshape(2,2))
b=np.arange(16).reshape(4,4)        #arange(start,end,steps)
print(b)
c=np.array([[1,2],[3,4]])
print("\nArray C\n",c,sep='')
d=np.array([[5,6],[7,8]])
print("\nArray D\n",d,sep='')

print("\nV Stack:\n",np.vstack((c,d)),sep='')
print("\nH Stack:\n",np.hstack((c,d)),sep='')
print("\n\nSlicing on arrays: \n",b[2:4,2:4],"\n\n",b[2,2],sep='')
print("\n\nV Split:\n",np.vsplit(b,2),sep='')
print("\n\nH Split:\n",np.hsplit(b,2),sep='')


print("\n\nSum of all elements of Array b: ",b.sum())
print("\nMaximum element of Array b: ",b.max())
print("\nMean of all elements of array b: ",b.mean())
print("\nStandard deviation of elements of array b: ",b.std())
print("\nVariance of all elements of array b: ",b.var())
print("\n* operator on C and D\n",c*d,sep='')      #Each corresponding element gets multiplied

from numpy import linalg            #Mandatory to import linalg separately to use it
print("\n\nInverse of matrix C:\n",linalg.inv(c),sep='')
print("\n\nDeterminant of matrix C:",linalg.det(c))
print("\n\nEigen Values of matrix C:\n",linalg.eig(c),sep='')
print("\n\nTranspose of matrix C:\n",c.T,sep='')
print("\n\nTranspose of matrix C:\n",c.transpose(),sep='')
print("\n\nRank of matrix C:",linalg.matrix_rank(c))
print("\n\nMatrix C after power 4:\n",linalg.matrix_power(c,4),sep='')
print("\n\nSolution of Matrix C and D:\n",linalg.solve(c,d),sep='')
