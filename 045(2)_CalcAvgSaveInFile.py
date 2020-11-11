try:
    f=open('created.txt','r')
except:
    print("File Not Found!")
    exit()
namels=f.readline().split()
lines=f.readlines()
sum=[]
avg=[]
col=len(namels)
for i in range(col):
    sum.append(0)
for scores in lines:
    scorels=scores.split()
    for i in range(col):
        sum[i]=sum[i]+int(scorels[i])
for i in range(col):
    avg.append(sum[i]/len(namels))
    print("Average of",namels[i],":",avg[i])

g=open('filehandlingfile.py','a+')
for i in range(col):
    g.writelines(["Average of ",namels[i]," : ",str(avg[i]),"\n"])
g.seek(0)
print("\n\nContent of the file FileHandlingFile.py after appending is: \n",g.read(),sep='')
f.close()
g.close()
