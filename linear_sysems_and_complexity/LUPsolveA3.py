#  solves Ax=b by via the decomposition PA = LU

import numpy as np
import scipy.linalg as ln

def LUPsolve(A,b):  # inputs n x n numpy array A, and n x 1 numpy array b

    # Performing LU-decomposition with partial pivoting on A and returning all relevant matrices
    P,L,U = ln.lu(A)

    # setting P equal to the transpose of itself since ln.lu() returns a transpose of the permutation matrix
    P = P.T

    # here y = Ux and will be evaluated as part of the system Ly=Pb
    y = ln.solve_triangular(L, P@b, lower=True)

    # using the calculated y above we solve for x in the system Ux = y
    x = ln.solve_triangular(U,y,lower=False)
    
    return x, L, U, P  # outputs solution x, and numpy arrays L, U and P from PA = LU decomposition






