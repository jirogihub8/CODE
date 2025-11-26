f=open('GIAODICH.INP')
f1=open('GIAODICH.OUT','w')
n=int(f.readline())
a=list(map(int,f.readline().split()))
bestsum=a[0]
nowsum=a[0]
check=0
for i in range(1,n):
    if nowsum<0:
        nowsum=a[i]
        check=i
    else:
        nowsum+=a[i]
    if nowsum>bestsum:
        bestsum=nowsum
        start=check
        end=i
        
print(bestsum)
f.close()
f1.close()