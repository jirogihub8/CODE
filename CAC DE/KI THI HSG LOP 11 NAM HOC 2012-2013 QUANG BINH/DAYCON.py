f=open("DAYCON.INP")
f1=open("DAYCON.OUT","w")
N=int(f.readline())
A=list(map(str,f.readline().split()))
M=int(f.readline())
B=list(map(str,f.readline().split()))
a=[0]*(N)
b=[0]*(M)
a1=set()
a2={}
for i in range(N):
    for j in range(M):
        if A[i]==B[j]:
            print(A[i],B[j],i,j)
            a[i]=A[i]
            b[j]=B[j]
f.close()
f1.close()