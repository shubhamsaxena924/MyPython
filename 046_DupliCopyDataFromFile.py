#This program will copy the content of a file in another file.
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
    file_name1=input('Enter the name of the file to copy from: ')
    f=open(file_name1,'r')
except:
    f=create(file_name1)

file_name2=input('Enter the name of the file to copy to: ')
try:
    g=open(file_name2,'x')
except:
    print("FILE ALREADY EXISTS. Do You Want To Overwrite Or Append?")
    ch=input("Press 'w' to overwrite OR\nPress 'a' to append OR\nPress any other key to exit   ")
    if ch=='w' or ch=='a':
        g=open(file_name2,ch+'')
    else:
        f.close()
        #g.close()                  Error: As g is not defined
        exit()
f.seek(0)
c=f.read()
g.write(c)
f.seek(0)
g=open(file_name2,'r')
g.seek(0)
print("\n\nContent in the file",file_name1,"is: \n",f.read())
print("\n\nContent in the file",file_name2,"is: \n",g.read())
f.close()
g.close()
