def binary_search(arr, target):
    low = 0
    high = len(arr)
    
    i = 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Iteration no: {i}")
        print(f"low = {low} ---> mid = {mid} ---> high = {high}\n")
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        i += 1
            
    return -1
    
    
    
arr = list(range(10000))
target = 9901
idx = binary_search(arr, target)
