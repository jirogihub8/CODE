lt2=[]
for i in range(1,50):
    lt2.append(2**i)
f=open("POWER2.INP")
f1=open("POWER2.OUT","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
#a^k=x -> loga(x)=k
#2^k=x->log2(x)=k

#kiểm tra phải luỹ thừa 1 số ko
'''x=int(input())
k=round(math.log(x, 2))
if 2**k==x:
    print('1')
else:
    print('0')'''
#kiểm tra phải luỹ thừa của 2 ko
dem=0
d1=list(d.keys())

            
f.close()
f1.close()

    