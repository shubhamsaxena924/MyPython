#Two types of files:-
    ##1 Text File:- Consists of chas; Human-readable; Used to store textual data.
    ##2 Binary File:- Written in binary(machine) language, 0-1 ; can be used to store images, videos, audios, zip files etc.

#open():  opens a file specified in specified mode.(By default read mode)       Syntax:  var_name=open("filename.txt",[mode])   ;where var_name is file handle, which is used to operate on that particular file.

##Seven modes to open a file:-
    #1  r = read mode           #2 w = write mode           #3  a = append mode         #4 r+ = r & w mode          #5 w+ = w and r mode            #6 a+ = a & r mode          #7 x = exclusive mode for w
#   (Err if no file)      (No err,Overwrite if exist)      (No err,Append at end)        (Err if no file)       (No Err, Overwrite if exist)      (No err, Append at end)     (Err if file exists for security)

#   tell()=returns current position of the file pointer                         seek(x,0) or seek(x): move file pointer x positions ahead from beginning
#                                                                               seek(x,1): move file pointer x posiiton ahead from current position
#                                                                               seek(x,2): move file pointer x position backward from end of the file
##In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file are allowed (the exception being seeking to the very file end with seek(0, 2)).
### NOTE: When we open a file in read mode, then the file handle can be used as a ordered sequence in which each element is a line of the file.
f=open("filehandlingfile.py",'r')           #Filename is case-insensitive
print(f,"\n\n")                             #Links a file, print info about the file handle.
for line in f:                              #f is a sequence which can be used to iterate on for each line of the file
    line=line.rstrip()                      #remove extra newline character as it will also be printed through print function
    print(">>>",line)

f.seek(0)                                   #To move the file pointer to the beginning
s=f.read()                                  #Reads whole text after current position in a file as a string
print("\n\n\nUsing read():",s)
f.seek(0)                                   #To move the file pointer to the beginning
s=f.readline()                              #reads one line from current position
f.seek(0)                                   #To move the file pointer to the beginning
s2=f.readlines()                            #reads all the lines and store them as different elements in a list
print("\n\nUsing readlines():",s2)
print("\n\nLine 1 Using readline:",s)



### NOTE: Write and append
f=open("filehandlingfile.py",'a+')          #append and read
p=f.tell()                                  #last position initially
f.write("Shubham")                          #Write shubham at the end
print("Current position:",f.seek(0),"\n\n") #pointer at starting for reading purpose
print("After appending:\n ",f.read(),sep='')
f.seek(p)                                   #file pointer at initial last position
f.writelines(["Aadarsh\n","Priya\n","Bharti\n","Anand\n"])                      #but it still appends at the end ;  you need to specify where you want new line, other wise it will be printed in same line
print(f.seek(0),"\n\n\n")                   #pointer at starting for reading purpose
print("After appending:\n ",f.read(),sep='')



### NOTE: Exclusive mode
#f=open("modulefactsum1.py",'x')            #Error: FileExistsError
f.close()
