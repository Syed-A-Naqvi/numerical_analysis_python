import numpy as np

#  Jacobian for Lorenz Equations

def LorenzJacobian(x):         
                                
#  function definition
    
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    J11 = -1
    j12 = 1
    j13 = 0
    J21 = 2-x3
    J22 = -1
    J23 = -x1
    J31 = x2
    J32 = x1
    J33 = -3

    Jac = np.array([[J11, j12, j13], [J21, J22, J23], [J31, J32, J33]])

    return Jac    # the appropriate variable