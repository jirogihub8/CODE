'''def uoc(a,b):
    if b==0:
        return a
    return uoc(b,a%b)
print(uoc(2,5))
import math
lcm=2*5//uoc(2,5)
d1=0
d2=0
d3=0
for i in range(1,14 ):
    if i%2==0:
        print(i,end=' ')
        d1=0
print('-')
for i in range(1,14):
    if i%5==0:
        d2+=1
        print(i,end= ' ')
for i in range(1,14):
    if i%2==0 and i%5==0:
        d3+=1
d=100-d1-d2+d3
d4=0
print('-')
for i in range(1,14):
    if i%2== 0 or i%5==0:
        continue
    else:
        print(i,end=' ')
        d4+=1'''
l=0
r=49
while l<=r:
    mid =(l+r)//2
    dem=mid-(mid//2+mid//5-mid//(10))
    if dem>=10:
        r=mid-1
        result=mid
        
    else:
        l=mid+1

    
    
        