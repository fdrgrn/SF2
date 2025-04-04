def combine(d1, d2):
    new_dict = {}
    for key in d1:
        if key in d2:
            sum = sum(d1[key]) + sum(d2[key])
            new_dict[key] = sum
        else:
            new_dict[key] = d1[key]

d1 = {1: [2], 4: [5,6]}
d2 = {4: [8]}