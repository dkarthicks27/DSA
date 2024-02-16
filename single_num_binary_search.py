def single_num(arr):
    low = 0
    high = len(arr) - 1
    
    i = 1
    while low <= high:
        mid = (low + high) // 2
        
        print(f"Iteration no: {i}:\nLow = {low}\tHigh = {high}\tMid = {mid}\n")
        # if the mid element is the single number
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return mid
        
        else:
            if arr[mid] == arr[mid + 1]:
                first_occ_index = mid
            else:
                first_occ_index = mid - 1
            
            if first_occ_index % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1
        
        i += 1
                

arr = [1, 2, 2, 3, 3, 4, 4]
print(arr[single_num(arr)])
