import time

def search(collection, value):
    '''
    search for a value in a collection
    '''
    for i in collection:
        found = value in collection
    return found

lst = list(range(1,50000))
start = time.time()
search(lst, 50000)
end = time.time()
print(end - start)