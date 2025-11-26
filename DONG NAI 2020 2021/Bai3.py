f=open("Bai3.inp")
f1=open("Bai3.out","w")
n=int(f.readline())
xmin=9999999
ymin=9999999
xmax=-9999999
ymax=-9999999
for i in range(n):
    x,y=map(int,f.readline().split())
    xmin=min(xmin,x)
    ymin=min(ymin,y)
    xmax=max(xmax,x)
    ymax=max(ymax,y)
f1.write(str(xmax)+' '+str(ymin)+'\n')
f1.write(str(xmin)+' '+str(ymin)+'\n')
f1.write(str(xmin)+' '+str(ymax)+'\n')
f1.write(str(xmax)+' '+str(ymax))

f.close()
f1.close()
    
