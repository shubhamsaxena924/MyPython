#This program will calculate the sum of the numbers present in the file which are isolated by spaces.
ch2='1'
while ch2=='1':
    try:
        file_name=input("Enter the name of the file, to calculate sum of isolated numbers: ")
        f=open(file_name,'r')
        print("\n\nContent in the file ",file_name," :\n",f.read(),sep='')
        f.seek(0)
        sum=0
        for line in f:
            for word in line.split():
                if word.isdigit():
                    sum=sum+int(word)
        print("\n\nSum of all the isolated numbers in the file is: ",sum)
        break
    except:
        print("File Not Found, First create a file.")
        ch=input("\n\nTo create now, Press '1' ")
        if ch=='1':
            exec(open('43_CreateWriteAppendFile.py').read())
        ch2=input("Press '1' to rerun calculation  ")
f.close()
