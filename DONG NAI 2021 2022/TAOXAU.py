f=open("TAOXAU.INP")
f1=open("TAOXAU.OUT","w")
a=f.read().split('\n')
d=0
a[0]=a[0].lower()
a[0]=a[0].replace(' ','')
a[1]=a[1].lower()
for i in a[0]:
    if a[0].count(i)<=a[1].count(i):
        d+=1
if d==len(list(a[0])):
    print("1")
else:print("0")
