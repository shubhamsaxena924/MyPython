#Read scores of USA and IND separated by space and find sum for each of the column
ch2='1'
while ch2=='1':
    try:
        file_name=input("Enter the name of the file, to calculate sum of isolated numbers: ")
        f=open(file_name,'r')
        print("\n\nContent in the file ",file_name," :\n",f.read(),sep='')
        f.seek(0)
        names=f.readline()                               #To skip first line USA IND and so on
        namels=[]
        score_sum=[]
        for name in names.split():
            namels.append(name)
            score_sum.append(0)
        lines=f.readlines()
        for scores in lines:
            scorels=scores.split()
            for i in range(len(scorels)):
                score_sum[i]=score_sum[i]+int(scorels[i])
        for i in range(len(scorels)):
            print("Sum of",namels[i],"scores: ",score_sum[i])
        break
    except:
        print("File Not Found, First create a file.")
        ch=input("\n\nTo create now, Press '1' ")
        if ch=='1':
            exec(open('43_CreateWriteAppendFile.py').read())
        ch2=input("Press '1' to rerun calculation  ")
f.close()
