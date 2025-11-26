f=open("DAUGIANGUOC.INP")
f1=open("DAUGIANGUOC.OUT","w")
n=int(f.readline())
d1=[]
d2={}
for i in f:
    if i not in d1:
        d1.append(i)
        d2[i]=1
    else:
        d2[i]+=1
d1.sort()
for i in d1:
    if d2[i]==1:
        f1.write(str(i))
        break
f.close()
f1.close()
    