f=open("NHIENLIEU.INP")
f1=open("NHIENLIEU.OUT","w")
N=int(f.readline())
a=list(map(int,f.readline().split()))
vt={0:[N+1]}
m=[]
R=[0]*(N+1)
stalk=[]
for i in range(N-1,-1,-1):
    '''vt_min=bisect.bisect_left(m,a[i])'''
    ''' tìm vị trí sẽ làm mất giá a[i]'''
    while stalk and stalk[-1] >= a[i]:
        stalk.pop()
    if stalk:
        vt_min=vt_min=vt[stalk[-1]][0]
    else:
        vt_min=N
    stalk.append(a[i])
    
    if a[i] not in vt:
        vt[a[i]]=[i+1]
    else:
        vt[a[i]].insert(0,i+1)
    R[i+1]=vt_min
        
    print('min của :',a[i],'là',a[vt_min-1])
    if vt_min==N:
        print('khoảng cách từ a[i] đến vị trí của min là:',N-i)
        print("từ",i+1,'đến',N)
    else:
        print('khoảng cách từ a[i] đến vị trí của min là:',vt_min-i-1)
        print("từ",i+1,'đến',vt_min)
print("-----------------------------------------------------------")
q=int(f.readline())
for i in f:
    L1,R1,x=map(int,i.split())
    L0=L1
    R0=R[L1]
    check=a[L1-1]
    result=0
    checkN=0
    ''' tìm vị trí xuất hiện đầu tiên và cuối cùng của giá x trong đoạn l:r'''
    while check !=x and L0<=R1 and checkN!=1:
        L0=R0
        R0=R[L0]
        
        check=a[L0-1]
        if R0==N:
            checkN=1
    '''xử lí vị trí xuất hiện đầu tiên và cuối cùng của giá x trong đoạn l:r'''
    '''láy số lượng'''
    if check==x:
        if R0==N and R0<=R1:
            result=N-L0+1
        elif R0>R1:
            result=R1-L0+1
        elif R0<R1:
            result=R0-L0
        elif R0==R1:
            
            result=R1-L0
    if result==0:
        print("Từ ",L1,"đến ",R1,"thì ",x,"không tồn tại")
    else:
        if R0==N and R0<=R1:
            R0+=1
        
        print("Từ ",L1,"đến ",R1,"thì ",x,"trong từ vị trí ",L0,"đến vị trí ",R0-1,)
        print("số lượng ",x,"là ",result)
    
    
    
    
