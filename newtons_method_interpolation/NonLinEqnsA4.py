#  This file contains a function that evaluates the (vector-valued) function f(x)
#    (used to define the system of nonlinear equations f(x) = 0 )  

import numpy as np

def NonLinEqns(x):     # input numpy array containing elements of the vector x                                       

   # assigining variables
   x1 = x[0]
   x2 = x[1]

   #  code that evaluates f(x)
   f1 = x1*(x2*x2) + (x1*x1)*x2 + x1*x1*x1 - 1
   f2 = (x1*x1*x1)*(x2*x2) - 2*(x1*x1*x1*x1*x1)*(x2) - (x1*x1) + 1

   fval = np.array([f1, f2]) 

   # return numpy array containing elements of (vector-valued) f(x)
   return fval