#  Starter code for Question 3 of Assignment 2 

import numpy as np
import matplotlib.pyplot as plt

# Import the function you wrote for part 1(e).
from NewtonRaphsonA2 import NewtonRaphson_method


# define the functions you'll need
def f(x):
    return 4.0*x**4 - 8.0*x**3 + 7.0*x**2 - 3.0*x + 1/2 # insert function
def df(x):
    return 16.0*x**3 - 24.0*x**2 + 14.0*x - 3.0 # insert derivative


# Set parameters and initial values for Newton-Raphson iteration.
x0 = 1                                # initial guess value
kmax = 1000                               # maximum number of tolerations
eps_x = 1e-8                           # error tolerance for solution
eps_f = 1e-8                            # error tolerance for solution function value

# Do Newton-Raphson iteration.
solution_NewtRaph, record_NewtRaph, flag_NewtRaph = NewtonRaphson_method(f,df,x0,kmax,eps_x,eps_f)

print("Solution: ", solution_NewtRaph)
print("Record:\n", record_NewtRaph)
print("flag: ", flag_NewtRaph)

# Plot the errors.
#Newton Raphson Method
nx = np.array([])
ny = np.array([])

for k in record_NewtRaph:
    nx = np.append(nx, k[0])
    ny = np.append(ny, k[2])

plt.semilogy(nx,ny)
plt.title("Rate of Convergence for the Newton-Rapshon Method")
plt.xlabel("Number of Iterations (k)")
plt.ylabel("Approximate Error (eps_x)")
plt.show()