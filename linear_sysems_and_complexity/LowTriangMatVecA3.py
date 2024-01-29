# function for computing the matrix vector product 
#    where L is a unit lower triangular matrix

import numpy as np

def LowTriangMatVec(L,x):

    # Insert code to compute the product y of the lower triangular matrix L with vector x.
    
    # zero vector with the same shape as x
    y = np.zeros(x.shape)

    # looping over each 1 along main diagonal
    for i in range(x.size):

        # updating the ith element of y by adding the corresponding element of x
        y[i] = y[i] + x[i]
    
        # looping over all entries in L below a pivot 1
        for j in range(i+1, x.size):
            
            # updating all elements of y by adding the corresponding element in x times the corresponding element
            # in L for the current column i
            y[j] = y[j] + x[i]*L[j,i]

    return y   # y = Lx
