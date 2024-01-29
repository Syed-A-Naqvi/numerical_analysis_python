#  Starter code for Question 1 of Assignment 3 

import numpy as np

# Import the function you wrote for part 1(a) and the secant iteration function.
from CondNumFuncA3 import CondNumFunc
from Secant import secant_method


# Set parameters and initial values for secant iteration.

desired_cond_num = 4

def f(a):
    return CondNumFunc(a) - desired_cond_num

x_previous = 0
x_current = 5
k_max = 100
error_max = 10**(-8)
res_max = 10**(-8)

# Do secant iteration.
solution_secant, record_secant, flag_secant = secant_method( f, x_previous, x_current, k_max, error_max, res_max )


# write out the solution
print(f"The \"a\" value required so that matrix \"A\" has a condition number of {desired_cond_num} is {solution_secant}")