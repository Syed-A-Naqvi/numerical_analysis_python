# Starter code for Python function for Bisection Method

# As a starting point, you can cut and paste the code in the course codes repository, 
#  but make sure there is an output that contains your iteration history. 
#  (You'll need it for the plots you have to make, and for the grader to mark it).
#  This argument must be a numpy array with one row for each completed iteration and, 
#  on every row, the iteration number, approximation and the approximate error, like this:
# [[0, initial approximation, initial error, initial residual],[1, approximation after one iteration, error after one iteration, residual after one iteration], ...]
#   (you can use the left endpoint of the initial interval as the initial approximation)

#  IMPORTANT: The last row must contain information for the last computed iteration; 
#  i.e., it cannot contain rows of zeros at the end

import numpy as np
import math

def bisection_method(f,a0,b0,k_max,eps_x,eps_f):
    # order of arguments:  function f(x), left endpoint, right endpoint, max iterations, tolerance on approximate error, tolerance on residual):

    conv = False                        # flag for convergence, default is "not converged"
    
    if ( f(a0)*f(b0) > 0):              # check to see whether we can guarantee convergence via IVT condition
        print('Error. f(a0) f(b0) > 0: Starting condition not satisfied.')
        return None, None, conv         # abort and print message if we can't guarantee convergence
    
    a = a0
    b = b0
    
    iter_Hist = np.array([0, a, abs(b-a), abs(f(a))]) # initializing row 0 of the interation history matrix before the occurence of
                                                      # the first iteration 
                                                      # [0, initial approximation, initial error, initial residual]
                                                      # all values are for initial approximation = left endpoint = a0 = a

    for k in range(k_max):              # loop over at most k_max bisection steps
        c = (a + b)/2.0                 # find the current midpoint
        f_mid = f(c)                    # compute the function value at the midpoint
        f_left=f(a)                     # compute the function value at the current left boundary
        if (f_mid*f_left > 0):          # if they have the same sign...
            a=c                         # update the left boundary, otherwise...
        else:
            b=c                         # update the right boundary
        max_err = abs(b-a)              # compute the maximal error and the residual
        res = abs(f_mid)
        
        
        current_Iter = np.array([k+1, c, max_err,res]) # Determining the values for the current iteration

        iter_Hist = np.vstack((iter_Hist,current_Iter)) # Updating the history of iterations with the current iteration information


        if (max_err < eps_x) and (res < eps_f):     # if both are less than their tolerance, stop iterations
            conv=True                               # set the convergence flag to "converged"
            break

    if (conv==False):                   # print warning if the iterations did not converge
        print(f'No convergence after {k_max} interations')

    return c, iter_Hist, conv  #  return variables for your approximation, iteration history, and convergence test, in this order