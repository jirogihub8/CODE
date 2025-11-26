'''def uoc(x):
    d=2
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d+=1
            if x//i!=i:
                d+=1
    return d
f=open("SOLUONGUOC.INP")
f1=open("SOLUONGUOC.OUT","w")
a=int(f.readline())
b=1
for i in f:
    b*=int(i)
print(uoc(b))'''
def uoc(x):
    d=[True]*(x+3)
    d[0]=d[1]=False
    for i in range(2,int(x**0.5)+1):
        if d[i]==True:
            for j in range(i*i,x+1,i):
                d[j]=False
    g=[]
    for i in range(2,x+1):
        if d[i]:
            g.append(i)
    return g
g=uoc(10**3)
f=open("SOLUONGUOC.INP")
f1=open("SOLUONGUOC.OUT","w")
a=int(f.readline())
b=1
d={}
for i in f:
    b*=int(i)
    i=0
while True:
    if b!=1 and b%g[i]==0:
        if g[i] not in d:
            d[g[i]]=1
            b//=g[i]
        else:
            d[g[i]]+=1
            b//=g[i]
    elif b==1:
        break
    else:
        i+=1
re=1
for i in d.values():
    re*=(i+1)
print(re)
   
        
        
        

