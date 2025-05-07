import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def eulers_method(y, v, c, p, A, mass, arr, acceleration, t):
    v += acceleration * t
    y += v * t
    acceleration = -9.8 + (c * p * A * v**2) / (2 * mass)
    arr = np.append(arr, y)
    return v, y, acceleration, arr

#Constants
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Uncertainties:                          
T/P = 23 degrees, +/- 1 degree            
m = +/- 0.001                           
A = (Big circle inner circle,difference)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
t = 0.02 
y = 1
v = 0
acceleration = -9.8
c = 0.5
p = 1.22
A = 150 / 10000  #Convert cm² to m²
mass = 0.003 #Single mass
arr = np.array([])

#Euler's Method Iteration
while y > 0:
    v, y, acceleration, arr = eulers_method(y, v, c, p, A, mass, arr, acceleration, t)

print(arr)
