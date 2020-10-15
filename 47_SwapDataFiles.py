#This program will swap the contents of the two files wuthout using any third file.
def create(file_name):              #function to create and wirte file if it doesnot exist
    print("FILE",file_name,"NOT FOUND. FIRST CREATE A FILE...")
    ch=input("\nPress '1' to create a blank file and write into it...")
    if ch=='1':
        f=open(file_name,'w+')
        ch2='1'
        while ch2=='1':
            f.write(input("\nEnter line to write in file: "))
            f.write("\n")
            ch2=input("\nPress '1' if you want to enter more  ")
        return(f)                   #return file handle to as it is local variable here
try:
    file_name1=input('Enter the name of the file 1: ')
    f=open(file_name1,'r')
except:
    f=create(file_name1)
try:
    file_name2=input('Enter the name of the file 2: ')
    g=open(file_name2,'r')
except:
    g=create(file_name2)
p=f.read()
d=g.read()
print("\n\nOriginal Content of Created.txt\n",p,sep='')
print("\nOriginal Content of FileHandlingFile.py\n",d,sep='')
f=open(file_name1,'w+')
g=open(file_name2,'w+')
f.write(d)
g.write(p)
f.seek(0)
g.seek(0)
print("\nContent of ",file_name1," after swapping:\n",f.read(),sep='')
print("\nContent of ",file_name2," after swapping:\n",g.read(),sep='')
f.close()
g.close()
