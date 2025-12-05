f=open("SAND.INP")
f1=open("SAND.OUT","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))

d={4:0,3:0,2:0,1:0}
for i in a:
    d[i]+=1
dem=0
dem+=d[4]
dem+=d[3]
if d[1]>d[3]:
    d[1]-=d[3]
else:d[1]=0
dem+=d[2]//2
du=d[2]%2
if du==1:
    dem+=1
    if d[1]>=2:
        d[1]-=2
    else:d[1]=0
dem+=d[1]//4
if d[1]%4!=0:
    dem+=1

f1.write(str(dem))
f.close()
f1.close()