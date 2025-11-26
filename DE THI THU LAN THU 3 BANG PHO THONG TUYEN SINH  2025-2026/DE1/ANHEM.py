def sangnt(x,k):
    c=[True]*(x+5)
    d=0
    for i in range(2,int(x**0.5)+1):
        if c[i]:
            for j in range(i*i,x+1,i):
                c[j]=False
    for j in range(2,x+1):
        if c[j]==True:
            if j+k<=n and c[j+k]:
                d+=1
    return d
f=open("ANHEM.INP")
f1=open("ANHEM.OUT","w")
n,k=map(int,f.readline().split())
f1.write(str(sangnt(n,k)))
f.close()
f1.close()