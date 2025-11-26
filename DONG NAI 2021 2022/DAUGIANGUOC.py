f=open("DAUGIANGUOC.INP")
f1=open("DAUGIANGUOC.OUT","w")
n=int(f.readline())
a=f.read().split('\n')
b=set(a)
d=99999999999
for i in b:
    if a.count(i)==1 and int(i)<d:
        d=int(i)
print(d)
