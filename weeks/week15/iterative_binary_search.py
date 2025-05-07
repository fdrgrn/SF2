def binarySearch(lst, target):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] < target:
            low = lst[mid] + 1
        elif lst[mid] > target:
            high = lst[mid] - 1
        else:
            return mid
        
    return -1 # Target not in list