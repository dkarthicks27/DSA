# First occurance

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    i = 1
    while low <= high:
        mid = (low + high) // 2
        
        print(f"Iteration no: {i}")
        print(f"low = {low} ---> mid = {mid} ---> high = {high}\n")
        
        if arr[mid] == target:
            if mid > 0 and arr[mid - 1] == target:
                high = mid - 1
            else:
                return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        i += 1
            
    return -1
    
    
    
arr = [1, 2, 8, 8, 8, 8, 8, 8, 8, 8]
target = 2
idx = binary_search(arr, target)

print(f"The first occurance of the value {arr[idx]} is at the index position: {idx}")


# Last occurance

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    i = 1
    while low <= high:
        mid = (low + high) // 2
        
        print(f"Iteration no: {i}")
        print(f"low = {low} ---> mid = {mid} ---> high = {high}\n")
        
        if arr[mid] == target:
            if mid < len(arr) - 1 and arr[mid + 1] == target:
                low = mid + 1
            else:
                return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        i += 1
            
    return -1
    
    
    
arr = [1, 2, 8, 8, 8, 8, 8, 8, 8, 8]
target = 2
idx = binary_search(arr, target)

print(f"The first occurance of the value {arr[idx]} is at the index position: {idx}")
