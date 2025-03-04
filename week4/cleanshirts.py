firstline_inputs = input("").split()
secondline_inputs = input("").split()

int_firstline = []
for j in range(len(firstline_inputs)):
    int_firstline.append(int(firstline_inputs[j]))

N = int_firstline[0]
MaxShirts = N
M = int_firstline[1]
D = int_firstline[2]

date_list = []
for i in range(len(secondline_inputs)):
    date_list.append(int(secondline_inputs[i]))

count_laundry = 0
for i in range(1, D):
    N -= 1
    if i in date_list:
        date_list.pop(date_list.index(i))
        N += 1
        MaxShirts += 1
    if N == 0:
        N = MaxShirts
        count_laundry += 1
print(count_laundry)
