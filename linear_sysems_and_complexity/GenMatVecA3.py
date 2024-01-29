# function for computing the matrix vector product 
#    where A is a matrix of general form

import numpy as np

def GenMatVec(A,x):

    # Insert code to compute the product y of the general matrix A with vector x.
    
    # zero vector with the same shape as x
    y = np.zeros(x.shape)

    # looping over each row in A
    for j in range(x.size):

        # setting jth element of y equal to the product of the first element of the jth row of A with the first element of x 
        y[j] = A[j,0] * x[0]
    
        # looping over all columns in A after the first
        for k in range(1, x.size):
            
            # updating jth element of y by summing the products of kth element in jth row of A with kth element of x
            y[j] = y[j] + x[k]*A[j,k]


    return y   # y = Ax
