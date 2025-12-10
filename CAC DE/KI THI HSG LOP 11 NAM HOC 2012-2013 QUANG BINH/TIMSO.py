def nt(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

f=open("TIMSO.INP")
f1=open("TIMSO.OUT","w")
P,Q=list(map(int,f.readline().split()))
for i in range(P,Q+1):
    if nt(int(str(i)[::-1])):
        f1.write(str(i)+'\n')
f.close()
f1.close()