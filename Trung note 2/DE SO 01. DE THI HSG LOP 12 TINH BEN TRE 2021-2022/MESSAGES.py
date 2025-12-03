f=open("MESSAGES.INP")
f1=open("MESSAGES.OUT","w")
n,m=list(map(int,f.readline().split()))
c=[[] for i in range(n+1)]
c[0]=[9999 for i in range(m+1)]
for i in range(1,n+1):
    c[i]=[9999]+list(map(int,f.readline().split()))
print(c)
dp=[[99999]*n for i in range(n+1)]
dp[0]=[9999 for i in range(m+1)]
print(dp)
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,j+1):
            dp[i][j]=min(c[i][j],dp[i-1][j],dp[i][j-k]+dp[i][k])
    print(dp)
print(c)
f.close()
f1.close()