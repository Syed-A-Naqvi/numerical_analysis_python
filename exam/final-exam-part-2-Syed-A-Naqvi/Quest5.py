#  Starter code for Question 5 of Final Exam Part 2



# include necessary code 
import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt          # For plotting 

def NewtSysSolve(f,Df,x0,epsx,epsf,itmx):                      # Newton iteration for systems of nonlinear equations

    conv = False                                               # Set convergence flag
    err=np.ones(itmx)
    res=np.ones(itmx)
    x = x0                                                     # Sets starting point as initial guess x0
    
    for k in range(0,itmx):                                    # Loop over Newton iterates
        
        r_vec = -f(x)                                          # Compute residual vector
        res[k] = scipy.linalg.norm(r_vec,2)                    # Compute residual
        J = Df(x)                                              # Evaluate Jacobian
        
        dx = scipy.linalg.solve(J,r_vec)                        # solve system J dx = -f

        err[k] = scipy.linalg.norm(dx,2)                       # Estimate of error
        
        print(f'Iter. {k}, err = {err[k]:.4e}, res = {res[k]:.4e}' )    # Print error and residual
        
        x = x + dx                                             # Apply update step
        
        if res[k] < epsf and err[k] < epsx:                    # Test for convergence
            conv = True
            its = k+1
            print("Converged, exiting...")
            break


    if conv==False:
        print("No convergece!")
        its=itmx

    return x,err,res,its


def f(x):                                       #  defines the function 
    x1 = x[0]
    x2 = x[1]
    f1 = 4*x1 + x1*x2**2 - 1
    f2 = x2 + x1*x2**2 + x1**2*x2 - 2
    fval = np.array([f1,f2])
    return fval

def Df(x):                                      #  defines the Jacobian
    x1 = x[0]
    x2 = x[1]    
    J11 = 4 + x2**2
    J12 = x1*2*x2
    J21 = x2**2+2*x1*x2
    J22 = 1 + x1*2*x2 + x1**2
    Jac = np.array([[J11,J12],[J21,J22]])
    return Jac


# Parameters of Newton iteration
epsf = 1.0e-9
epsx = 1.0e-8
itmx = 15
# Initial guess
x0 = np.ones((2,1))

#  call Newton iteration function NewtSysSolve defined in NewtonSystemIteration.py
x, err, res, its = NewtSysSolve(f,Df,x0,epsx,epsf,itmx)

# Print out solution 
# (make sure your variables are defined appropriately 
#    so these lines print out your results without error)
print('The solution is ')
print(x)

