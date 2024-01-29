#Collaborators: Arham Naqvi, Kevin Rodriguez, Mansi Patel, Samir Rahman, Fareeha Malik

# Python function for Secant iteration

# you'll need to change the inputs
def SecantIteration(f, a0, a1, kMax, eps_x, eps_f):  
# Input: list the inputs in this comment

    x0 = a0
    x1 = a1                    # you'll need to change this: you now have 2 initial guesses 
    iterations = []    

    conv=False                 # flag for convergence
   
    for k in range(kMax):

        fx0=f(x0)
        fx1=f(x1)                # current function value
        
        # For the secant method, we no longer have an explicit definition for the derivative of our function f
        # for this reason our delta x (the amount by which we change x1 in order to get x2) can only be found using
        # an approximation of the slope of f(x) at x1 which is the slope of the secant line between x0 and x1
        dx = (-1) * ((fx1)*(x1 - x0)) * (fx1-fx0)**(-1)  # update step
        
        # the following error tolerances are for the x1 and x0 values of the previous iteration
        err = abs(dx)          # current error estimate
        res = abs(fx1)         # current residual
       
        # because the err and res values are for the previous iteration, we cannot write k+1 as the iteration number
        # for the err and res values of the current iteration. For example, the error values for the intial guesses
        # are calculated during the first iteration but are for values that existed before any iteration took place and so once
        # we arrive at convergence the total amount of iterations that will have taken place will be k and not k+1  
        print(f'Iteration {k}: x1 = {x1}, x0 = {x0}, err={err:.4e}, res={res:.4e}')        
        
        # appending a tuple containing the iteration number and the eps_x for the current iteration into the iterations list
        iterations.append((k, err))

        if err < eps_x and res < eps_f:       # If converged ...
            print("Converged!")
            conv=True
            break
        
        #  you'll need reassign values for the next iteration here
        x0=x1
        x1=x1+dx
    

    if (conv==False):
        print("No convergence!")
    
    return x1 ,err,res,conv,iterations


