# CSCI / MATH 2072U -- Computational Science 1
# Date: 22/01/2022
# Tutorial 1
# CRN: 73778
# Collaborators: Arham Naqvi, Kevin Romero Rodriguez, Mansi Patel, Samir Rahman, Fareeha Malik
#
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007


# Computes iterates of a function / rule:  phi 
# (is also the implementation of the iterative approximation of 
# the square root of a, which we'll see later in class).

# In: x, initial point; a, parameter; k_max, max number of iterations
# Out: x, kth iterate (which we'll see is actually an approximation of sqrt(a) )
import math


#Time Complexity = O(1) + O(1) + O(1) + O(1) + O(1) + O(n) + O(1)
#Time Complexity = O(n)
def iteration(x, a, k_max, eps_x):  # This funciton will compute iterates of the function phi
                                    # k_max is the maximum allowed iterations
									# eps_x is the error threshold

    print()
    print(f"With an x0 of {x} and an \"a\" value of {a}, we are going to determine")
    print(f"if the function phi(x)=(1/2)*(x+(a/x)) converges to sqrt(5) below an error threshold of")
    print(f"{eps_x}(epsilon_x) within a maximum of {k_max} iterations.")
    print()

    for k in range(k_max):
        x_previous = x              #This line keeps track of the previous iterate
        x = phi(x,a)                #This assignment sets x equal to the next iterate in the sequence
        print (f"Iterate x({k+1}) = {x}") #O(1) 
        
        if( abs(x-x_previous) < eps_x ): #O(1) This lines determines if the current iteration
										 #is below the error tolerance passed as eps_x
            print()
            print(f'It has taken {k+1} iterations to converege below a tolerance of {eps_x}(epsilon_x)')
            return x, k+1 #O(1)
    
    print()
    print(f"After {k_max} iterations we did not converge below a tolerance of {eps_x}.")

#O(1)
# Rule phi that produces iterates 
def phi(x, a):
	return (1/2)*(x+(a/x)) #O(1)  # Decide what, if anything, needs to be returned


# Execution part of code
print("Iteration of a rule, phi") #O(1)
x_starr, iters = iteration(-1,5,20, 1.0e-4) #O(n)
		
print ("Solution is ", x_starr) #O(1)

#Total Time Complexity = O(n)
