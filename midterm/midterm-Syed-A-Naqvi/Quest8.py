#  Starter code for Question 8 of Midterm Test


#  import functions and modules you will use
import numpy as np
import matplotlib.pyplot as plt
import math

#  insert code for finding the approximate solution 
#    to the nonlinear equation using the Newton-Raphson Method
def NewtRaph(f,fprime,x0,k_max,eps_x):
    
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

        if (err < eps_x):                              # if both are less than their tolerance, stop iterations
            conv=True                                  # set the convergence flag to "converged"
            break

    if (conv==False):                       # print warning if the iterations did not converge
        print(f'No convergence after {k_max} interations')

    it_hist = np.array(iteration_history)  # plot will need this to be an array not a list

    return x,it_hist,conv                   # return the approximate solution, maximal error and convergence flag


def f(x):                               # function definition of f(x), where we are solving f(x)=0
    return  np.exp(x)+math.sin(x)+2*x-2

def fprime(x):                          # function definition of f(x), where we are solving f(x)=0
    return math.cos(x) + np.exp(x) + 2 


x0 = 1.0;                               # initial guess
k_max=1000                              # maximum number of iterations
eps_x = 1.0e-10                         # tolerance on x

xstar,it_hist,conv=NewtRaph(f,fprime,x0,k_max,eps_x)

#   write out solution 
if (conv==True):
    print(f'\n x* = {xstar}')
    print('number of iterations required for convergence = ',it_hist[-1,0] )

################################-------------------------PLOT-----------------------##########################################
# number of iterations
xx = it_hist[:,0]
# max error per iteration
yy = it_hist[:,2]

# Create a figure with 1 subplots
fig, ax = plt.subplots(figsize=(7,5))

# Plotting the Newton-Rapshon rate of convergence
ax.semilogy(xx, yy, '-o')


# Adding labels and a title
ax.set_xlabel('Number of Iterations (k)')
ax.set_ylabel('Approximate Error (eps_x)')
ax.set_title('Convergence Rate for Newton-Rapshon Method')

plt.show()