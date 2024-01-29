import numpy as np

#  function for Lorenz Equations

def LorenzEqns(x):                                 

#  function definition

    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    f1 = x2-x1
    f2 = 2*x1-x2-x1*x3
    f3 = x1*x2-3*x3

    f = np.array([f1,f2,f3])
        
    return f # the appropriate variable
