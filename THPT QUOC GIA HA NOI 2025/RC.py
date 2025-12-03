def forest_diff_no_get(N, B, C):
    # Bước 1: Ghép lại và sắp xếp theo chiều cao tăng
    trees = sorted([(C[i], B[i]) for i in range(N)])
    
    total_cnt = 0
    total_sum = 0
    cnt_type = {}
    sum_type = {}
    ans = 0
    
    i = 0
    while i < N:
        j = i
        same = []
        # Gom nhóm các cây có cùng chiều cao
        while j < N and trees[j][0] == trees[i][0]:
            same.append(trees[j])
            j += 1
        
        # Bước 2: Tính chênh lệch cho nhóm này
        for c, b in same:
            # nếu cây b có trong cnt_type(hay đã gặp 1 lần)
            # cnt_b=cây b
            if b in cnt_type:
                cnt_b = cnt_type[b]
            else:
                cnt_b = 0
            #nếu cây b có trong sum_type(hay đã gặp 1 lần)
            #sum_type=tổng chiều cao các cây b đã gặp
            if b in sum_type:
                sum_b = sum_type[b]
            else: sum_b = 0
            
            ans += c * (total_cnt - cnt_b) - (total_sum - sum_b)
        
        # Bước 3: Cập nhật sau khi xét nhóm
    
        for c, b in same:
            #nếu như cây b chưa bao giờ xuất hiện thì thêm cây b vào:
            if b not in cnt_type:
                cnt_type[b] = 0 # cnt_type là : số lượng cây b đã gặp
                sum_type[b] = 0 # sum_type là : chiều cao của cây b đã gặp
            cnt_type[b] += 1
            sum_type[b] += c
            total_cnt += 1 # số cây đã gặp       
            total_sum += c # số chiều cao đã gặp
        
        i = j

    return ans
f=open('RC.INP')
f1=open("RC.OUT","w")
N,m=map(int,f.readline().split())
B=list(map(int,f.readline().split()))
C=list(map(int,f.readline().split()))
'''d=[[]for i in range(m+1)]
pre=[0]*(n+1)
for i in range(n):
    d[a[i]].append(i)
for i  in range(1,n+1):
    pre[i]=pre[i-1]+b[i-1]
'''
print(forest_diff_no_get(N, B, C))
f.close()
f1.close()
