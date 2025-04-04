import time
'''
Firgus is behind on assignments, after looking through his backpack he realizes he has n 
items, each of which he records as a string.
He has m upcoming assignments, the i th assignment requests T_i items to complete.
If he has T_i required items. he can complete the assignment, otherwise he flunks.
How many assignments can Firgus complete?

Input:
First line contains two integres N and M seperated by a space
Next n lines contains a single  string (each one is unique)
Next m sections contain a single integer T_i, followed by T_i
line each containing a single string

'''
#def search(items, target_items):
#    return 

start = time.time()
nm_list = input().split()
n = int(nm_list[0])
m = int(nm_list[1])
items = set()

for _ in range(n):
    items.add(input())

needed_items = []

for _ in range(m):
    number_items = int(input("\n"))
    temp_list = set()
    for _ in range(number_items):
        temp_list.add(input())
    needed_items.append(temp_list)

count = 0
for i in range(m):
    #print(f"\nAssignment {i+1} can be completed") if needed_items[i].issubset(items) else print(f"\nAssignment {i+1} can't be completed")
    if needed_items[i].issubset(items):
        count += 1

print(count)