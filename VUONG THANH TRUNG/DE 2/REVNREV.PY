def rev(x,u,v):
    while (u<=v):
        tg=x[u]
        x[u]=x[v]
        x[v]=tg
        u+=1
        v-=1
    return x
def cycle(x,y):
    d=0
    while(True):
        x=rev(x,u,r)
        x=rev(x,l,r)
        d+=1
        if (x==y):
            return d
    
f=open("REVNREV.INP")
f1=open("REVNREV.OUT","w")
n,k=map(int,f.readline().split())
u,v=map(int,f.readline().split())
l,r=map(int,f.readline().split())
a=[0]+[i for i in range(1,n+1)]
b=[0]+[i for i in range(1,n+1)]
d=cycle(a,b)
k=k%d
for i in range(k):
    a=rev(a,u,v)
    a=rev(a,l,r)
for i in range(1,n+1):
    print(a[i])
f.close()
f1.close()