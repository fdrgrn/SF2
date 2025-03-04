from math import factorial
def binom(n,k):
    num = factorial(n)
    denom = factorial(n-k)*factorial(k)
    return num // denom

print(binom(3.3))

def PascalTriangle(n):
    lst = []

    for row in range(n):
        sublist = []
        for i in range(row+1):
            sublist.append(binom(row, i))
        lst.append(sublist)
    return lst

def printPascal(matrix):
    for row in matrix:
        for i in range(len(row)):
            print(row[i], end = '')
        print()

printPascal(PascalTriangle(4))