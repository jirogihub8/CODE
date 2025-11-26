with open("TONGCACSO.INP","r") as f:
    t=list(map(int,f.readline()))
with open("TONGCACSO.OUT","w") as f:
    print(sum(t))
    