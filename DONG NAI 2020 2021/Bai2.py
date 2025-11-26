f=open("Bai2.inp")
f1=open("Bai2.out","w")
n=int(f.readline())
for s in f:
    s=int(s)
    s=str(s)
    while True:
        if len(s)>0:
            if int(s[0])%3==0:
                s=s[1:]
            elif int(s[-1])%3==0:
                s=s[:-1]
            elif (int(s[0])+int(s[-1]))%3==0:
                s=s[1:]
                s=s[:-1]
            else:
                break
        else:
            break
    f1.write(str(len(s))+'\n')
f.close()
f1.close()
        
        
