village_number = int(input("How many villages: "))
point_list = []

for i in range(village_number):
    point_list.append(int(input(f"Village {i+1}: ")))

point_list.sort()
smallest = []
for j in range(1, len(point_list) - 1):
    difference =  abs((point_list[j] - abs(point_list[j] - point_list[j-1])/2  - (point_list[j]+ abs(point_list[j+1] - point_list[j])/2 )) )
    smallest.append(difference)
print(min(smallest))
