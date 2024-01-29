#  Contructs the matrix M for solving for coefficients 
#   of polynomial interpolant using Newton polynomial basis

import numpy as np

def NewtonPolyBuild(xs):     # input numpy array containing x values of interpolating nodes
    
   # code for constructing the matrix M
   
   #finding the value of the dimension n+1 and initialising a square matrix M with n+1 rows and n+1 columns of zeros
   np1 = np.shape(xs)[0]
   M = np.zeros((np1,np1))
   
   for i in range(0,np1):
       M[i,0] = 1
       for j in range(1,i+1):
           M[i,j] = M[i,j-1] * (xs[i] - xs[j-1])
    
   return M          # return numpy array with matrix M 

