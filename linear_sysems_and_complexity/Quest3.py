
#  Starter code for Question 3 of Assignment 3 
# matrix-vector multiplication analysis

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt   #  for plotting
import time                       #  module for timing computations

from GenMatVecA3 import GenMatVec              # import function for general matrix-vector product
from LowTriangMatVecA3 import LowTriangMatVec  # import function for matrix-vector product with unit lower triangular matrix

wtimes_Low = []        #  initialize list for storing computation times for lower triangular matrix
wtimes_Gen = []        #  initialize list for storing computation times for lower triangular matrix
wtimes_BuiltIn = []    #  initialize list for storing computation times for built-in Python function
nValues = []           #  initialize list for storing n values

for k in range(7,15):     # Loop over matrix sizes
    print(k)                              
    n = 2**k
    nValues.append(n)
    A = np.random.rand(n*n).reshape((n,n))  # Set up random general matrix and right hand side
    P,L,U = scipy.linalg.lu(A)              # use LU decomp to get a unit lower triangular matrix L
    x = np.random.rand(n)                   # Set up random vector

    
    #  compute products and measure computation time for general matrix A and record result
    tb = time.time()
    GenMatVec(A,x)
    ta = time.time()
    tt=ta-tb
    wtimes_Gen.append(tt)

    #  compute products and measure computation time for unit lower triangular matrix L and record result
    tb = time.time()
    LowTriangMatVec(L,x)
    ta = time.time()
    tt=ta-tb
    wtimes_Low.append(tt)

    #  compute products and measure computation time using built-in Python function and record result
    tb = time.time()
    A@x
    ta = time.time()
    tt=ta-tb
    wtimes_BuiltIn.append(tt)

    #  end k for loop


#  print out computation times and plot results

# printing out computation times for builtin algorithm
print(wtimes_BuiltIn)

# Create a figure with 1 subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plotting relative error
ax.loglog(nValues, wtimes_Low, '-o', label='Complexity of LowTriangMatVec() Algorithm')

# Plotting maximal error
ax.loglog(nValues, wtimes_Gen, '-o', label='Complexity of GenMatVec() Algorithm')

# Adding labels and a title
ax.set_xlabel('n values')
ax.set_ylabel('Computation Time (ms)')
ax.set_title('Computation Time Comparison of LowTriangMatVec() Algorithm vs GenMatVec() Algorithm\n')
ax.legend()
plt.show()
