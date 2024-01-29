
#Collaborators: Arham Naqvi, Kevin Rodriguez, Mansi Patel, Samir Rahman, Fareeha Malik


import numpy as np

def bisect(f,a0,b0,k_max,eps_x,eps_f):
    
    conv = False                        # flag for convergence, default is "not converged"
    
    if ( f(a0)*f(b0) > 0):              # check to see whether we can guarantee convergence via IVT condition
        print('Error. f(a0) f(b0) > 0: Starting condition not satisfied.')
        return None, None, conv         # abort and print message if we can't guarantee convergence
    
    a = a0
    b = b0
    iterations = []
    
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

        # printing all relevant information for each iteration, at each iteration
        print(f'iteration {k+1}: c = {c}, a={a}, b={b}, err={max_err:.4e} and res={res:.4e}')

        # appending a tuple containing the iteration number and the eps_x for the current iteration into the iterations list
        iterations.append((k+1,max_err))

        if (max_err < eps_x) and (res < eps_f):     # if both are less than their tolerance, stop iterations
            conv=True                               # set the convergence flag to "converged"
            break

    if (conv==False):                   # print warning if the iterations did not converge
        print(f'No convergence after {k_max} interations')

    return c,max_err,conv,iterations               # return the approximate solution, maximal error, convergence flag,
                                                   # and a list containing the iteration number and the eps_x for that iteration


def f(x):                               # function definition of f(x), where we are solving f(x)=0
    return (x**2)-a                     # here the value for x such that f(x)=0 is actually the value of sqrt(a)






a = 5                                   # we are going to approximate the square root of this parameter

# Using the following conditional statements we will
# determine appropriate bounds for our bisection function
# for approximating the square root of a
 
if(a>1):                                # if a > 1 then 1 < sqrt(a) < a
    a0=1                                # and so our lower bound becomes 1
    b0=a                                # and our upper bound becomes a

else:                                   # if a < 1 then 0 < sqrt(a) < 1
    a0=0                                # and so our lower bound becomes 0
    b0=1                                # and our upper bound becomes 1

k_max = 100                             # maximum number of iterations
eps_x = 1.0e-4                          # tolerance on x
eps_f = 1.0                             # tolerance of function value




xstar,err,conv,iteraetions=bisect(f,a0,b0,k_max,eps_x,eps_f)

if (conv):
    print(f'\n x* = {xstar}')