f=open("SAND.INP")
f1=open("SAND.OUT","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
a.sort()
a=a[::-1]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
dem=0
for i,j in d.items():
    if i==4:
        dem+=j
    elif i==3:
        dem+=j
        if d[1]<=j:
            d[1]=0
        elif d[1]>j:
            d[1]-=j
    elif i==2:
        dem+=(j//2)
        if j%2!=0:
            dem+=1
            if d[1]>=2:
                d[1]-=2
            else:
                d[1]-=0
    elif i==1:
        if d[i]>=1:
            dem+=d[1]//4
            if d[1]%4!=0:
                dem+=1   
f1.write(str(dem))
f.close()
f1.close()