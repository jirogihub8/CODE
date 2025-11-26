f=open('SONHA.INP')
f1=open('SONHA.OUT','w')
n=int(f.readline())
s=1
l=1
d=0
while s*10<=n:
    e=s*10-1
    d+=(e-s+1)*l
    l+=1
    s*=10
d+=(n-s+1)*l
d*=80000
f1.write(str(d))
f.close()
f1.close()

