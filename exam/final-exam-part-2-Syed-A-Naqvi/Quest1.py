#  Starter code for Question 1 of Final Exam Part 2

# include necessary code

import numpy as np
import matplotlib.pyplot as plt

def NewtRaph(f,fprime,x0,k_max,eps_x,eps_f):
    
    conv = False                        # flag for convergence, default is "not converged"
    
    x = x0
    
    iteration_history = []              # to hold a list
    
    for k in range(k_max):              # loop over at most k_max Newton steps
        res = f(x)                      # compute the residual
        delta_x = - res/fprime(x)       # comput the Newton-Raphson update
        x = x + delta_x
           # compute the approximate error 
        err = abs(delta_x)
        iteration_history.append([k+1, x, err, res])
        
        print(f'iteration {k+1}, x* = {x:.8f}, approx error={err:.4e} and res={res:.4e}')  # Since k starts at 0, I added 1 to k to make the first iteration 1

        if (err < eps_x) and (abs(res) < eps_f):     # if both are less than their tolerance, stop iterations
            conv=True                                  # set the convergence flag to "converged"
            break

    if (conv==False):                       # print warning if the iterations did not converge
        print(f'No convergence after {k_max} interations')

    it_hist = np.array(iteration_history)  # plot will need this to be an array not a list

    return x,it_hist,conv                   # return the approximate solution, maximal error and convergence flag


def f(x):                               # function definition of f(x), where we are solving f(x)=0
    return  np.exp(x)*((9*x**2)-(12*x)+4)

def fprime(x):                          # function definition of f(x), where we are solving f(x)=0
    return ((9*x**2)+(6*x)-8)*np.exp(x)


x0 = 1.0;\
k_max=1000                              # maximum number of iterations
eps_x = 1.0e-8                          # tolerance on x
eps_f = 1.0                             # tolerance of function value

x,it_hist,conv=NewtRaph(f,fprime,x0,k_max,eps_x,eps_f)
err=np.array(it_hist[:,2])
num_its=it_hist[-1][0]

# Print out solution 
# (make sure your variables are defined appropriately 
#    so these lines print out your results without error)

#  x is solution, err[num_its-1] is approximate error on last iteration
#    and num_its is the number of iterations required


print(x, err[-1], num_its)


# make the plot
    
xx = it_hist[:,0]
yy = it_hist[:,2]
#plt.plot(xx,np.log(yy))
plt.semilogy(xx,yy)
plt.title("Newton-Raphson Convergence Rate")
plt.xlabel('iteration (k)')
plt.ylabel('approx error')

plt.show()