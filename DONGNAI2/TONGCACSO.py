f=open("TONGCACSO.INP")
f1=open("TONGCACSO.OUT","w")
a=f.readline()
s=0
for i in a:
    s+=int(i)
f1.write(str(s))
f.close()
f1.close()