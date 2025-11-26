f=open("EXC.INP")
f1=open("EXC.OUT","w")
n,k=list(map(int,f.readline().split()))
a=list(map(int,f.readline().split()))
d=[]
s=k*(k+1)//2
for i in a:
    if i not in d and i<=k:
        d+=[i]
        s-=i
        
        

f1.write(str(s))
f.close()
f1.close()