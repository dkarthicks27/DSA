def flip(b):
    if b == 1:
        return 0
    else:
        return 1


def binary_search(start, end, k, bit):
    mid = (start + end) // 2
    # print(start, end, mid, bit, k)
    if mid == k:
        print(bit)
        return
    
    elif mid < k:
        start = mid + 1
        bit = flip(bit)
        binary_search(start, end, k, bit)
        
    else:
        end = mid - 1
        binary_search(start, end, k, bit)
        
    

n = 2
k = 3

start = 0
end = 2 ** (n + 1) - 2
print(f"len of string: {end + 1}\n\n")

binary_search(start, end, k, 0)
    
    
