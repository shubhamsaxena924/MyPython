#This program will make a file and add number to it as enter by the user.
print("This program will make a file and add data to it as enter by the user.\n")
file_name=input("Enter the desired name of the file, (with extension: .txt): ")
try:
    f=open(file_name,'r')
    ch=input("File Already Exists. Press '1' to show its content  ")
    if(ch=='1'):
        print("\n\nContent in the file ",file_name," :\n",f.read(),sep='')
    ch2=input("\n\nTo append at the end of the file, press '1' ")
    if(ch2=='1'):
        f=open(file_name,'a+')
        ch='1'
        while(ch=='1'):
            f.write(input("Enter to write line in file: "))
            f.write('\n')
            ch=input("\nPress '1' to enter more lines   ")
        f.seek(0)
        print("\n\nContent in the file ",file_name," :\n",f.read(),sep='')
    else:
        ch2=input("\n\nTo overwrite the content of the file, press '1' ")
        if(ch2=='1'):
            raise error

except:
    f=open(file_name,'w+')
    ch='1'
    while(ch=='1'):
        f.write(input("Enter to write line in file: "))
        f.write('\n')
        ch=input("\nPress '1' to enter more lines   ")
    f.seek(0)
    print("\n\nContent in the file ",file_name," :\n",f.read(),sep='')
f.close()
