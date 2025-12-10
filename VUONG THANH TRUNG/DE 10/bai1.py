def sangnt(x):
    c=[True]*(x+3)
    for i in range(2,int(x**0.5)+1):
        if c[i]:
            for j in range(i*i,x+1,i):
                c[j]=False
    l=[]
    for i in range(2,x+1):
        if c[i]:
            l.append(i)
    return l
x=sangnt(1000)
f=open("bai1.inp")
f1=open("bai1.out","w")
dp=[0]*(10+3)
for i in x:
    print(i)
    for j in range(10,i-1,-1):
        print(dp)
        '''for k in range(1,3):
            if j>=i*k:
                dp[j]=max(dp[j],dp[j-i*k]+k)
                print(j,i*k,i)'''
        if j>=i*1:
            dp[j]=max(dp[j],dp[j-i*1]+1)
        if j>=i*2:
            dp[j]=max(dp[j],dp[j-i*2]+2)

            
        
                
for i in f:
    i=int(i)
    print(dp[i])
