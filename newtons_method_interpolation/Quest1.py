# script for Question 1 of Assignment #4
#   for solving system of nonlinear equations using Newton's method

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt          # For plotting 

from NewtSysSolve import NewtSysSolve
from NonLinEqnsA4 import NonLinEqns
from JacobianA4 import Jacobian


# Set parameters for Newton iterations
epsf = 1.0e-9
epsx = 1.0e-12
itmx = 15
# Initial guess
x0 = np.ones((2,1))

#  call Newton iteration function NewtSysSolve defined in NewtSysSolve.py
x, err, res, its  = NewtSysSolve(NonLinEqns,Jacobian,x0,epsx,epsf,itmx)


#  print solution
print('\n')
print('The solution is:\n', str(x))
print(f'x1 = {x[0,0]:.8f}, x2 = {x[1,0]:.8f}')


# create a plot showing convergence of the Newton iterations 
#   don't forget to label plot appropriately

plt.figure
plt.semilogy(range(0,its),err[0:its],'-*g')
#plt.semilogy(range(0,its),res[0:its],'-*r')
plt.xlabel('Nr. of iterations')
plt.ylabel('error')
plt.title('Convergence of Newton Iterations for 2x2\n System of Nonlinear Equations')
plt.show()