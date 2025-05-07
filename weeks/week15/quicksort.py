def quickSort(lst):
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    
    pivot = [lst.pop(-1)]
    left_lst = []
    right_lst = []

    for elem in lst:
        if elem < pivot[0]:
            left_lst.append(elem)
        elif elem == pivot[0]:
            pivot.append(elem)
        else:
            right_lst.append(elem)

    print(left_lst)
    print(right_lst)

    sorted_right = quickSort(right_lst)
    sorted_left = quickSort(left_lst)
 
    sorted_lst = sorted_left + pivot + sorted_right
    print(sorted_lst)

    return sorted_lst

lst = [1,4,5,6,2,3,4,7,3] # 1,2,3,4,4,5,6,7,8
quickSort(lst)


