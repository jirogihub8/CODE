def check(s):
    xau=s.upper()
    d={}
    for i in xau:
        if i!=' ' and i!='\n':
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
    return d
f=open("TAOXAU.INP")
f1=open("TAOXAU.OUT","w")
s1=f.readline()
s2=f.readline()
a=check(s1)
b=check(s2)
l=len(a)
d=0
for i in b:
    if i in a and b[i]==a[i]:
        d+=1
if l==d:
    f1.write(str(1))
else:
    f1.write(str(0))
f.close()
f1.close()