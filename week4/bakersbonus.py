first_line = input("").split()
F = int(first_line[0])
D = int(first_line[1])

day_list = []
for i in range(D):
    temp = []
    temp_input = input("").split()
    for i in range(len(temp_input)):
        temp.append(int(temp_input[i]))
    day_list.append(temp)
print(day_list)

bonus_count = 0
#Daily Sum
for day in day_list:
    print(sum(day))
    if sum(day) % 13 == 0:
        bonus_count += sum(day) % 13
print(bonus_count)


