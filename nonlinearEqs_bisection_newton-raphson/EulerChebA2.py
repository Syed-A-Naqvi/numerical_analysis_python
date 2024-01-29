# Starter code for Python function for Euler-Chebyshev iterations

import numpy as np

def EulerCheb_method(f, df, df2, x0, kMax, eps_x, eps_f):
# order of arguments:  function f(x), derivative, 2nd derivative, initial guess, max iterations, tolerance on approximate error, tolerance on residual

#  copy your Newton-Raphson method code and make the appropriate modifications

    x=x0
    conv=False                     # flag for convergence

    for k in range(kMax):
        fx=f(x)                    # current function value
        dx= (-1)*(fx/df(x)) - ( (df2(x)/(2*df(x))) * ((f(x)/df(x))**2) )               # update step
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