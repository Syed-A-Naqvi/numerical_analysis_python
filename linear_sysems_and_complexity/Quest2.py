#  Starter code for Question 2 of Assignment 3 
#  analysis of linear systems involving Vandermonde matrix
#  i increased the upper bound for the n values to help with the analysis, the plot still includes n values from 15..40


import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as ln
import scipy as sc

#  import function you wrote for solving linear systems
from LUPsolveA3 import LUPsolve

# initialize variables
relativeErrorRecord = []
maxErrorRecord = []
nValues = np.arange(15,41)
conditionNumbers = []
residuals = []

# loop over matrix sizes
for N in nValues:
    
   # call vander to get V
   V = np.vander(np.linspace(-1,1,N+1))
   
   # form the vector c (the right hand side of the equation Vx=c)
   c = V[:,N-1]

   # call LUPsolve to get x
   x_star,L,U,P = LUPsolve(V,c)

   # form the true x for current N
   x_true = np.zeros(N+1)
   x_true[-2] = 1

   # compute the error and record
   true_error = ln.norm(x_true - x_star,sc.inf)/ln.norm(x_true,sc.inf)
   relativeErrorRecord.append(true_error)

   # compute the max relative error and record
   maximal_error = np.linalg.cond(V)*(ln.norm(c - V@x_star,sc.inf)/ln.norm(c,sc.inf))
   maxErrorRecord.append(maximal_error)

   # inlcuding condition numbers and relative residuals on the same plot to help with analysis 
   # residuals.append(ln.norm(c - V@x_star,sc.inf)/ln.norm(c,sc.inf))
   # conditionNumbers.append(np.linalg.cond(V))


# plot error and max relative error versus the matrix size on a logarithmic scale on the y-axis (semilogy) 

# Create a figure with 1 subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plotting relative error
ax.semilogy(nValues, relativeErrorRecord, '-o', label='Relative Error')

# Plotting maximal error
ax.semilogy(nValues, maxErrorRecord, '-o', label='Maximal Relative Error')

# Plotting condition numbers
#ax.semilogy(nValues, conditionNumbers, '-o', label='Condition Numbers')

# Plotting condition numbers
#ax.semilogy(nValues, residuals, '-o', label='Residuals')


# Adding labels and a title
ax.set_xlabel('n value')
ax.set_ylabel('Error')
ax.set_title('Maximal Relative and Relative Errors of Solution Approximations\n for Vandermonde Matrices with Varying n Values')
ax.legend()
plt.show()