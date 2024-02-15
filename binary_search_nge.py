def binary_search_nge(arr, target):
    low = 0
    high = len(arr) - 1
    
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
    
    print(f"Iteration no: {i}")
    print(f"low = {low} ---> mid = {mid} ---> high = {high}\n")        
    return low
    

arr = [1, 3, 5, 6, 19, 23, 35, 42]
target = 40
idx = binary_search(arr, target)

print(idx, arr[idx])
