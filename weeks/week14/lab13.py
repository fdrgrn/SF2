'''
Implement a custom iterator class to generate 
even numbers in the interval [start, end]
'''
class EvenIter:
    def __init__(self, start = 0, end = 0):
        if start % 2 == 0:
            self.current = start 
        else:
            self.current = start + 1
        self.end = end

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        even_number = self.current
        self.current += 2
        return even_number

# for elem in EvenIter(0, 10):
#     print(elem)

'''
Implement a custom iterable class for the Fibonacci
numbers.  This class constructor should take n, 
representing the first n terms of the Fibonacci 
sequence
'''
class Fibonacci:
    def __init__(self, n):
        self.first = 0
        self.second = 1
        self.count = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        new_fib = self.first + self.second
        self.first, self.second = self.second, new_fib
        return new_fib

for elem in Fibonacci(10):
    print(elem)


'''
Draw the recursion tree for the computation of 
recSum(10)
'''


'''
write a recursive function that determines the
minimum element in a given list of integers. 
'''
class Minimum:
    def __init__(self,lst):
        if not lst:
            raise ValueError
        self.list = lst
        self.min = lst[0]
        self.current = lst[0]

    def __iter__(self):
        return self
    
    def __next__(self):
        

'''
write a recursive function that converts a string of integers
into its integer counterpart
'''

'''
write a recursive function to determine if a given string
is a palindrome
'''

'''
Write a recursive function to count number of vowels in a string
'''

'''
use recursion to determine if a string has more vowels than consonants. 
'''