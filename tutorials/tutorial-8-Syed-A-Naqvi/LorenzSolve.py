# Tutorial 8
#  Use Newton's method to solve Lorenz Equations 


# import necessary modules
import numpy as np
import scipy.linalg 
import matplotlib.pyplot as plt
from LorenzEqnsT8 import LorenzEqns
from LorenzJacobianT8 import LorenzJacobian
from NewtonSystemIteration import NewtonSysSolve


# your code here

#parameters of newton iteration
epsf = 1.0e-9
epsx = 1.0e-12
itmx = 15
# Initial guess
x0 = np.array([2,2,2])
#  call Newton iteration function NewtSysSolve defined in NewtonSystemIteration.py
x, err, res, its = NewtonSysSolve(LorenzEqns,LorenzJacobian,x0,epsx,epsf,itmx)

# print solution
print('\n')
print('The solution is: \n'+str(x))
print(f'That is, we have x1 = {x[0]:.8f}, x2 = {x[1]:.8f}, x3 = {x[2]:.8f}')
print('\n')


# # plot the result
fig, ax = plt.subplots(figsize=(10,6))

# Plotting res error
ax.semilogy(range(its), res[0:its], '-o', label='Residual Error')
# Plotting soution error
ax.semilogy(range(its), err[0:its], '-o', label='Solution Error')


# Adding labels and a title
ax.set_xlabel('Number of Iterations')
ax.set_ylabel('Error')
ax.set_title('Convergence of Lorenz Equations Using Newton Method')
ax.legend()

plt.show()
