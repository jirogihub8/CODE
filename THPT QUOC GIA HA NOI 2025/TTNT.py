f=open("TTNT.INP")
f1=open("TTNT.OUT","w")
starton,startoff,T=list(map(int,f.read().split('\n')))
'''s=0
for i in range(1,10):
    if i%2==0:
        s+=startoff
        print(s-startoff+1,':',s,'offline')
    else:
        s+=starton
        print(s-starton+1,':',s,'on')
bcnhay=starton+startoff
bc=T//(starton+startoff)
if T/bcnhay==bc:
    bc-=1
start1on=1
start1off=start1on+starton
start2off=starton+startoff
d=1
nowoff2=start2off+(bcnhay*(bc))
nowoff1=start1off+(bcnhay*(bc))
nowon2=starton+(bcnhay*(bc))
nowon1=start1on+(bcnhay*(bc))
if nowon1<=T<=nowon2:
    f1.write('1')
elif nowoff1<=T<=nowoff2:
    f1.write('0')
f.close()
f1.close()
'''
x=int(input())
s=int(input())
t=int(input())
if (t-1)%(s+x)<=x:
    print('1')
else:
    print('0')