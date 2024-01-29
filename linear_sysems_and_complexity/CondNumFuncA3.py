# Starter code for Python function for finding 
#   Condition number of specified matrix as
#     a function of the parameter a

import numpy as np


def CondNumFunc( a ):

    # inserting the parameter "a" into the correct position of the Matrix A
    A = np.array([[1,2,4],[3,a,1],[1,-2,3]])

    return np.linalg.cond(A,2) # Condition Number of specified matrix


