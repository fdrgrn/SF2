'''
bisect arguments:
lst wo work with
num to insert into list
[start,end] interval of the lst to consider

bisect(lst, num, start, end)
returns index qhere num can be inserted so lst will stay sorted
if num is already in lst, returns rightmost index where num can be inserted

bisect_left(lst, num, start, end)
returns the index where num can be inserted so lst will stau orted
if num is already in lst, return the leftmost index where it can be inserted

bisect_right(lst,num,start,end)
same as bisect
'''

import bisect
lst = [1,2,3,4,5,7,7,7,8,10,11]
num = 7
print(bisect,bisect(lst, num))