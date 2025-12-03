f=open("HOADEP.INP")
f1=open("HOADEP.OUT",'w')
S=f.readline().strip()
Q=int(f.readline())
l=len(S)
d={}
result=0
check=0
chan=[]
le=[]
tdle={}
halfS1=l//2
halfS2=l//2-2
for i in S:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        if d[i]>l//2:
            check=1
            break
for i in d.values():
    if i%2==0:
        chan+=[i]
    else:
        le+=[i]
        if i==1:
            tdle[0]=1
        else:tdle[i]=i%2
chan.sort()
lchan=len(chan)
lle=len(le)


if check==1:
    f1.write('0')
else:
    for i in f:
        print(i)
f.close()
f1.close()
    