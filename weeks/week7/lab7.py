'''
Question1:

Given a dictionary of keys that are strings and/or integers, 
values are lists, write a snippet of code that returns the total number
of elements of all lists that have keys as strings.  
'''

def string_keys_count(d):
    count = 0
    for key in d.keys():
        print(type(key))
        if str(type(key)) == "<class 'str'>":
            count += 1
    return count


'''
Question2:

Write a function wordTally that takes an integer argument 
n and reads n words from the user.  Note that the user
may enter the same word multiple times.  
Your function should tally up how many times each word
occurs that the user has entered and store it in a dictionary
where the keys are the words and the values are the number
of times each word occurs.  
Return this dictionary. 

You may only create one collection: one dictionary
'''
def wordTally(n):
    d = {}
    for i in range(n):
        word = input(f"Enter word {i+1}: ")
        d[word] = d.get(word, 0) + 1
    print(d)
    return d

'''
Quesiton3: 

write a function called invertDictionary that takes a 
dictionary d as an argument.  This function inverts the
provided dictionary.  That is, the keys become the values
(as lists) and the values become the keys. 

Note that d may have repetitive values, in which case in 
the inverted dictionary only one of these values
will be used as a key. For such a key, in the inverted
dictionary the value is a list of all such possible
keys from d

For example: 
d = {3: 5, 4: 5, 6: 1}
d_inverted = {5: [3, 4], 1: [6]}
'''

def invertDictionary(d):
    d_inverted = {}
    for key in d:
        d_inverted[d[key]] = [item for item in d if d[item] == d[key]]
    return d_inverted

'''
Question 4:

Given a sequence of m words and an integer k, find the
k-th most common words.  A word w is the k-th most 
common if exactly k-1 distinct words occur more
frequently than w. 
'''

def kth_common(l, k):
    d = {}
    for key in l:
        d[key] = d.get(key, 0) + 1

    d_inverted = {}
    for key in d:
        d_inverted[d[key]] = [item for item in d if d[item] == d[key]]

    key_list = list(d.keys())
    words_magnitudes = key_list.sort(reverse = True)
    set_magnitudes = list(set(words_magnitudes))

    word = words_magnitudes[k-1]
    if words_magnitudes.index(word) == set_magnitudes.index(word):
        return d_inverted[word]
    return None

list = ['cat','cat','cat','cat','fox','fox','fox','hi','hi','bye','bye','river','brook','stream']
print(kth_common(list, 1))