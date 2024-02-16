def peak_element_ls(arr):
    for i in range(len(arr)):
        if i == 0 and arr[i] >= arr[i + 1]:
            return arr[i]
        elif i == len(arr) - 1 and arr[i] >= arr[i - 1]:
            return arr[i]
        elif arr[i] >= arr[i + 1] and arr[i] >= arr[i - 1]:
            return arr[i]
    


def peak_element_bs(arr):
    low = 0
    high = len(arr) - 1
    
    i = 0
    while low <= high:
        mid = (low + high) // 2
        print(f"Iteration no: {i} Low = {arr[low]} \t high = {arr[high]} \t mid = {arr[mid]}")
        # best case
        if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
            return arr[mid]
        elif arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        i += 1

arr = [6, 13, 7, -5, 4, 3, 19]
# print(peak_element_ls(arr))
print(arr)
print(peak_element_bs(arr))
    
