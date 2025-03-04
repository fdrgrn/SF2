#def combine2(d1, d2):
'''
    return a dicitonary ehre each key is a key that is a key in the values of d1 and d2
    The values associated with every key in the new dictionary is the sum of all integers
    associated with that key in d1 and d2
'''

d1 = {'a': {3: [2], 4: [5, 6]}, 'b': [2, 7, 9], 4: [5,6]}
d2 = {'a': {3: [8, 12]}, 'b': {7: [7, 33]}}
result = {}
letter = {}

def combine(d1, d2):
    for key in d1:
        if key in d2:
            for x in d1[key]:
                if x in d2[key]:
                    lst1 = d1[key][x]
                    lst2 = d2[key][x]
                    result[x] = sum(lst1) + sum(lst2)
    return result

print(combine(d1, d2))
