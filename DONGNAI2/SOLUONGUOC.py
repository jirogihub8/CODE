def sangnt(a):
    k=[True]*(a+1)
    k[0]=k[1]=False
    for i in range(2,int(a**0.5)+1):
        if k[i]==True:
            for j in range(i*i,a+1,i):
                k[j]=False
    d=[]
    for i in range(2,a+1):
        if k[i]==True:
            d.append(i)
    return d
g=sangnt(10**2)     
f=open("SOLUONGUOC.INP")
f1=open("SOLUONGUOC.OUT","w")
n=int(f.readline())
s=1
for i in f:
    s*=int(i)
i=0
t=0
d=[]
print(s)
while s!=1:
    if s%g[i]==0:
        s//=g[i]
        t+=1
        if s==1:
            d.append(t)
    else:
        i+=1
        d.append(t)
        t=0
result=1
for i in d:
    result*=(i+1)
f1.write(str(result))
f.close()
f1.close()
    
    