
f=open("POWER2.INP")
f1=open("POWER2.OUT","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
lt2=[]
t=0
i=1
m=max(a)+10
while t<2*m:
    t=2**i
    i+=1
    lt2.append(t)

past_on={}
l=[]
dem=0
for i in a:
    for j in lt2:
        need=j-i
        if need in past_on and need >0:
            for g in range(past_on[need]):
                l.append((i,need))
                dem+=1
    if i not in past_on:
        past_on[i]=1
    else:past_on[i]+=1

f1.write(str(dem))

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
f.close()
f1.close()

    