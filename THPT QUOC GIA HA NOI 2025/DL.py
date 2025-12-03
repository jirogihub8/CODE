f=open("DL.INP")
f1=open("DL.OUT","w")
s=f.readline()
l=len(s)
pre=[0]*(l+1)
ma={0:0}
mi={}
for i in range(l):
    if s[i]=='V':
        pre[i+1]=pre[i]+1
        
    elif s[i]=='D':
        pre[i+1]=pre[i]-2
del(pre[0])
for i in range(len(pre)):
    if pre[i] not in ma:
        ma[pre[i]]=i
    elif pre[i] in ma:
        if pre[i] not in mi:
            mi[pre[i]]=i
        elif pre[i] in mi:
            if mi[pre[i]]<i:
                mi[pre[i]]=i
result=0
ma[0]=-1
for i in ma:
    if ma[i] in mi:
        t=mi[i]-ma[i]
        result=max(result,t)
f.close()
f1.close()
        
        

        
        
        

    


f.close()
f1.close()