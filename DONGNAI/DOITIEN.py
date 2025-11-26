f=open('DOITIEN.INP')
f1=open('DOITIEN.OUT','w')
a=int(f.readline())
if a<50000:
    f1.write(str(50000-a))
else:
    f1.write(str(a%50000))
f.close()
f1.close()
