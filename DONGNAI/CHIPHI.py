def uoc(a):
    if a==1:
        return 0
    d=1
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            d+=1
            if a//i!=i:
                d+=1
    return d
f=open('CHIPHI.INP')
f1=open('CHIPHI.OUT','w')
T=int(f.readline())
N,M=list(map(int,f.readline().split()))
a=[[0]*(M+2) for i in range (N+2)]
for i in range(1,N+1):
    a[i]=[0]+list(map(int,f.readline().split()))+[0]
b=[[0]*(M+2) for i in range (N+2)]
for i in range(1,N+1):
    for j in range(1,M+1):
        b[i][j]=uoc(a[i][j])
F=[[0]*(M+2) for i in range (N+2)]
for i in range(1,N+1):
    for j in range(1,M+1):
        F[i][j]=b[i][j]+min(F[i-1][j],F[i][j-1])
print(F[N][M])
        
f.close()
f1.close()
