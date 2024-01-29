#Collaborators: Arham Naqvi, Kevin Rodriguez, Mansi Patel, Samir Rahman, Fareeha Malik

# -*- coding: utf-8 -*-
"""
Script for implementing the Secant method 
using function 'SecantIterations.py' defined in SecantIteration.py

"""

import numpy as np
# import function SecantIteration defined in file SecantIteration.py:
from SecantIteration import SecantIteration
  
# The Python function SecantIteration has as inputs: 
#    function handle f
#    two initial guesses a0 and a1, maximal number of iterations k_max, 
#    tolerance for the error and residual eps_x and eps_f

#  put function definition of f here
def f(x):
    return (x**2 - a)

#  assign parameter values
a = 5.0

# for our two initial guesses we will use the fact that if a>1 then 1<sqrt(a)<a and if a<1 then 0<sqrt(a)<1
if (a > 1):
    x0 = 1
    x1 = a
else:
    x0 = 0
    x1 = 1

kmax = 50
eps_x = 1e-10
eps_f = 1e-10
#  call NewtonRaphson
x_starr, error, residual, converged = SecantIteration(f,x0,x1,kmax,eps_x,eps_f)
#  print out solution
print(f"x_star = {x_starr}, error = {error}, residual = {residual}, converged = {converged}")
