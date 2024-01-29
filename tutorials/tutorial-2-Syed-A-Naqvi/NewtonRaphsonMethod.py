#Collaborators: Arham Naqvi, Kevin Rodriguez, Mansi Patel, Samir Rahman, Fareeha Malik

# -*- coding: utf-8 -*-
"""
Script for implementing the Newton-Raphson method 
using function 'NewtonRaphson' defined in NewtonRaphsonIteration.py

"""

import numpy as np
# import function NewtonRaphson defined in file NewtonRaphsonIteration.py:
from NewtonRaphsonIteration import NewtonRaphson
  
# The Python function NewtonRaphson has as inputs: 
#    function handle f, function handle df (derivative of f)
#    initial guess of solution x0, , maximal number of iterations k_max, 
#    tolerance for the error and residual eps_x and eps_f

#  put function definition of f here
def f(x):
    return (x**2 - a)
#  put function definition of df here (derivative of f)
def df(x):
    return (2*x)
#  assign parameter values
a = 5.0
x0 = 3
kmax = 20
eps_x = 1e-10
eps_f = 1e-10
#  call NewtonRaphson
x, error, residual, converged = NewtonRaphson(f,df,x0,kmax,eps_x,eps_f)
#  print out solution
print(f"x = {x}, error = {error}, residual = {residual}, converged = {converged}")


