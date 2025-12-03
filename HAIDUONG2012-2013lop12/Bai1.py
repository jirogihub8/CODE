f1=open('Bai1.inp')
f2=open('Bai1.out','w')
n=int(f1.readline())
m=10**9
a=1
b=n//a
while a<=b:
    if n%a==0:
        b=n//a
    else:
        b=n//a+1
    if m>2*(a+b):
        m=2*(a+b)
    a+=1
print(m)