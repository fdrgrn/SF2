def  isPalindrome(lst):
    temp = lst
    #temp.reverse()
    return temp == lst

def silly(n):
    for i in range(n):
        result = []
        elem = input("Element: ")
        result.append(elem)
    if isPalindrome(result):
        print('yes')
    else:
        print('no')

silly(2)

