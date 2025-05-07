def binarySearch(lst, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return binarySearch(lst, mid+1, high, target)
        elif lst[mid] > target:
            return binarySearch(lst, mid, high-1, target)
        
    return -1
        
        