f=open("DF.INP")
f1=open("DF.OUT","w")
x=1
y=1
z=0
for i in range(1,10**5+2):
    f.write(str(z))
    z=x+y
    x=y
    y=z
f.close()
f1.close()