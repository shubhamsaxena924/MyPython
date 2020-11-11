f=open("modulefactsum.py",'r')              #Filename is case-insensitive
print(f,"\n\n")                             #Links a file, print info about the file handle.
linecount=0
wordcount=0
charcount=0
for line in f:                              #f is a sequence which can be used to iterate on for each line of the file
    linecount=linecount+1
    wordcount=wordcount+len(line.split())
    charcount=charcount+len(list(line))
    #line.split('')                         #Error: Empty separator
    line=line.rstrip()                      #remove extra newline character as it will also be printed through print function
    print(">>>",line)
print("\n\nLine count using file handle sequence:",linecount)
print("Word count using file handle sequence:",wordcount)
print("Char count using file handle sequence:",charcount)

f.seek(0)                                   #To move the file pointer to the beginning
s=f.read()                                  #Reads whole text after current position in a file as a string
charcount2=0
for i in s:
    charcount2=charcount2+1
wordcount2=0
for i in s.split():
    wordcount2=wordcount2+1
print("\n\nChar count using read():",charcount2)
print("Word count using read():",wordcount2)
f.seek(0)                                   #To move the file pointer to the beginning
s=f.readline()                              #reads one line from current position
f.seek(0)                                   #To move the file pointer to the beginning
s2=f.readlines()                            #reads all the lines and store them as different elements in a list
print("Line count using readlines():",len(s2))
print("Line 1:",s)
f.close()
