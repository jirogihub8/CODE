import heapq

def minseg_heap(arr):
    distinct = set(arr)         # tập hợp các phần tử phân biệt trong arr
    k = len(distinct)           # số phần tử phân biệt cần có trong đoạn con
    n = len(arr)                # độ dài mảng
    if k == 0:                  # mảng rỗng
        return 0

    last_pos = {}                # lưu vị trí xuất hiện cuối cùng của mỗi phần tử
    heap = []                    # min-heap lưu (index, value)
    ans = n                      # kết quả: khởi tạo bằng độ dài lớn nhất có thể

    # duyệt qua từng phần tử trong arr
    for i, val in enumerate(arr):
        last_pos[val] = i                      # cập nhật vị trí mới nhất của val
        heapq.heappush(heap, (i, val))         # đẩy (chỉ số, giá trị) vào heap

        # chỉ khi đã có đủ tất cả k phần tử phân biệt
        if len(last_pos) == k:
            # loại bỏ các entry trong heap không còn hợp lệ
            # (nghĩa là index không phải là vị trí cuối cùng trong last_pos)
            while heap and last_pos.get(heap[0][1], -1) != heap[0][0]:
                heapq.heappop(heap)

            # sau khi dọn sạch, heap[0] là vị trí nhỏ nhất còn hợp lệ
            min_index = heap[0][0]

            # đoạn con từ min_index đến i chứa đủ k phần tử
            ans = min(ans, i - min_index + 1)

    return ans
    