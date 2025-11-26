f=open("LEAD.INP")
f1=open("LEAD.OUT","w")
T=int(f.readline())
for i in range(T):
    n=int(f.readline())
    a=list(map(int,f.readline().split()))
    i=0
    x=''
    while i!=n:
        x+=str(max(a[i:]))
        i=a.index(max(a[i:]))+1
        x+=' '
    f1.write(str(x)+'\n')
    
f.close()
f1.close()
                
            
    
f.close()
f1.close()