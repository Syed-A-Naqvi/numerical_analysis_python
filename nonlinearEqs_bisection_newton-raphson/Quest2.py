#  Starter code for Question 2 of Assignment 2 

import numpy as np
import matplotlib.pyplot as plt

# Import the functions you wrote for parts 2(a) and 1(e).
from EulerChebA2 import EulerCheb_method
from NewtonRaphsonA2 import NewtonRaphson_method

# define the functions you'll need
def f(x):
    return np.exp(-x)+np.cos(x+1.0)-1.0 # insert function
def df(x):
    return -1.0*np.exp(-x)-np.sin(x+1.0) # insert derivative
def df2(x):
    return np.exp(-x)-np.cos(x+1.0) # insert 2nd derivative

# Set parameters and initial values for Halley iteration.
x0 = 1.0                                # initial guess value
kmax = 10                               # maximum number of tolerations
eps_x = 1e-14                           # error tolerance for solution
eps_f = 1e-8                            # error tolerance for solution function value

# Do Euler-Chebyshev iteration.
solution_EulerCheb, record_EulerCheb, flag_EulerCheb = EulerCheb_method(f,df,df2,x0,kmax,eps_x,eps_f)
print("Solution: ", solution_EulerCheb)
print("Record:\n", record_EulerCheb)
print("flag: ", flag_EulerCheb)

# Set parameters and initial values for Newton-Raphson iteration.
x0 = 1.0                                # initial guess value
kmax = 10                               # maximum number of tolerations
eps_x = 1e-14                           # error tolerance for solution
eps_f = 1e-8                            # error tolerance for solution function value

# Do Newton-Raphson iteration.
solution_NewtRaph, record_NewtRaph, flag_NewtRaph = NewtonRaphson_method(f,df,x0,kmax,eps_x,eps_f)
print("Solution: ", solution_NewtRaph)
print("Record:\n", record_NewtRaph)
print("flag: ", flag_NewtRaph)


# Plotting the errors.

#Euler-Chebyshev Method
ex = np.array([])
ey = np.array([])

for k in record_EulerCheb:
    ex = np.append(ex, k[0])
    ey = np.append(ey, k[2])

#Newton Raphson Method
nx = np.array([])
ny = np.array([])

for k in record_NewtRaph:
    nx = np.append(nx, k[0])
    ny = np.append(ny, k[2])

# Create a figure with 1 subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plotting the bisection rate convergence
ax.semilogy(ex, ey, '-o', label='Euler-Chebyshev Rate of Convergence')

# Plotting the newton raphson rate of convergence
ax.semilogy(nx, ny, '-o', label='Newton-Raphson Rate of Convergence')

# Adding labels and a title
ax.set_xlabel('Number of Iterations (k)')
ax.set_ylabel('Approximate Error (eps_x)')
ax.set_title('Convergence Rates for Differenct Numerical Approximation Methods')
ax.legend()

plt.show() #Displaying the plot