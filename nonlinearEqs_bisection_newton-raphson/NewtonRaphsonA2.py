# Starter code for Python function for Newton-Raphson iterations

# You can use the code you wrote in the tutorials, 
#  but make sure there is an output that contains your iteration history. 
#  (You'll need it for the plots you have to make, and for the grader to mark it).
#  This argument must be a numpy array with one row for each completed iteration and, 
#  on every row, the iteration number, approximation, and the approximate errors, like this:
# [[1, approximation after one update, error after one update, residual after one update], [2, approximation after 2nd update, ...]

#  IMPORTANT: The last row must contain information for the last computed iteration; 
#  i.e., it cannot contain rows of zeros at the end

import numpy as np

def NewtonRaphson_method(f,df,x0, kMax, eps_x, eps_f):
# order of arguments:  function f(x), derivative, initial guess, max iterations, tolerance on approximate error, tolerance on residual

    x=x0
    conv=False                     # flag for convergence

    for k in range(kMax):
        fx=f(x)                    # current function value
        dx=-fx/df(x)               # update step
        err = abs(dx)              # current error estimate
        res = abs(fx)              # current residual


        current_Iter = np.array([k,x,err,res])  # storing a record of information for each iteration
        

        if(k==1):                               # ensuring that the iteration history recording process begins AFTER the first iteration as the        
            iter_Hist = current_Iter            # inital iteration is comprised of error values for the initial guess and not for the first update        
        elif(k>1):                                          
            iter_Hist = np.vstack((iter_Hist,current_Iter))


        if (err < eps_x and res < eps_f):       # convergence test
            print("Converged!")
            conv=True
            break

        x=x+dx # this is the actual iteration step meaning that the calculated errors are for the previous update
    
    if (conv==False):
        print("No convergence!")

    return x, iter_Hist, conv   #  return variables for your approximation, iteration history, and convergence test, in this order
