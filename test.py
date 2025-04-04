grade_d = {'a': [1,2,3], 'b': [4,5,6], 'c':[7,2,9]}

list1 = [max([value[i] for value in list(grade_d.values())]) for i in range(3)]
print(list1)

list2 = [sum([value[i] for value in list(grade_d.values())])/2 for i in range(3)]
print(list2)

list3 = [(person, sum(grade_d[person])/3) for person in grade_d]
print(list3)