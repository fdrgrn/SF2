#Insertion sort
def mySort(lst, mode):
    #mode = bool False inverse True straight
    if not lst:
        return lst
    sorted_lst = [lst[1]]
    for i in range(1, len(lst)):
        for j in range(len(sorted_lst)):
            if lst[i] <= sorted_lst[j]:
                sorted_lst = sorted_lst[:j] + [lst[i]] + sorted_lst[j:]
                break
            elif j == len(sorted_lst) - 1:
                sorted_lst = sorted_lst + [lst[i]]
                break
    if not mode:
        sorted_lst = sorted_lst[::-1]
    return sorted_lst

test_list =[1,2,3,7,6,8,0,1]

#result = [[int(i) for i in len(row)] for row in lst_2d]
print(mySort(test_list, True))