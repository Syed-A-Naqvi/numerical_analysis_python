#  Starter code for Question 1 of Assignment 2 

import numpy as np
import matplotlib.pyplot as plt

# Import the functions you wrote for parts 1(d) and 1(e).
from bisectionA2 import bisection_method
from NewtonRaphsonA2 import NewtonRaphson_method

# define the functions you'll need
def f(x):
    return np.exp(-x)+np.cos(x+1.0)-1.0 # insert function
def df(x):
    return -1.0*np.exp(-x)-np.sin(x+1.0) # insert derivative


# Set parameters and initial values for bisection.
a0=0                                    # lower bound
b0=1                                    # upper bound
k_max = 1000                            # maximum number of iterations
eps_x = 1e-12                           # error tolerance for solution
eps_f = 1e-8                            # error tolerance for solution function value

# Do bisection.
solution_bisection, record_bisection, flag_bisection = bisection_method(f,a0,b0,k_max,eps_x,eps_f)
print("Solution: ", solution_bisection)
print("Record:\n", record_bisection)
print("flag: ", flag_bisection)

# Set parameters and initial values for Newton-Raphson iteration.
x0 = 1.0                                # initial guess value
kmax = 10                               # maximum number of tolerations
eps_x = 1e-12                           # error tolerance for solution
eps_f = 1e-8                            # error tolerance for solution function value

# Do Newton-Raphson iteration.
solution_NewtRaph, record_NewtRaph, flag_NewtRaph = NewtonRaphson_method(f,df,x0,kmax,eps_x,eps_f)
print("Solution: ", solution_NewtRaph)
print("Record:\n", record_NewtRaph)
print("flag: ", flag_NewtRaph)

# Plot the errors.

#Bisection Method
bx = np.array([])
by = np.array([])

for k in record_bisection:
    bx = np.append(bx, k[0])
    by = np.append(by, k[2])

#Newton Raphson Method
nx = np.array([])
ny = np.array([])

for k in record_NewtRaph:
    nx = np.append(nx, k[0])
    ny = np.append(ny, k[2])

# Create a figure with 1 subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plotting the bisection rate convergence
ax.semilogy(bx, by, '-o', label='Bisection Rate of Convergence')

# Plotting the newton raphson rate of convergence
ax.semilogy(nx, ny, '-o', label='Newton-Raphson Rate of Convergence')

# Adding labels and a title
ax.set_xlabel('Number of Iterations (k)')
ax.set_ylabel('Approximate Error (eps_x)')
ax.set_title('Convergence Rates for Differenct Numerical Approximation Methods')
ax.legend()

plt.show() #Displaying the plot