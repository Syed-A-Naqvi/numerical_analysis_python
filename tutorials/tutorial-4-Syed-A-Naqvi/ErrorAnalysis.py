import numpy as np
import numpy.linalg as npln
import scipy.linalg as sciln
import matplotlib.pyplot as plt

def matrixBuilder(size):                                            # Building a square matrix of the passed size
    
    A = np.zeros((size,size),float)

    for i in range(1, size+1):
        for j in range(1, size+1):
            A[i-1][j-1] = ((-1)**(i+j)) / (i + 2*j)                 # This is the mathematical formula by which the square matrix is
                                                                    # is constructed
    return A


iterations = np.zeros((9,5),object)                                 # This nd array will record the iteration history


for N in range(2,11):                                               # We are going to construct 8 NxN matrices for N = 2..10 and determine
                                                                    # the relative errors and relative residuals for each 

    A = matrixBuilder(N)                                            # Building a matrix A using the matrix builder function above


    c_true = A[:,0]                                                 # Setting c_true (in the equation Ax=c) as the first column of A 


    cond_A = npln.cond(A,2)                                         # Determining the condition number of matrix A using the 2-norm


    x_star = sciln.solve(A,c_true)                                  # Finding the approximate solution to the system Ax=c using built-in
                                                                    # LUP-decomposition scipy.linalg.solve algorithm


    c_approx = A@x_star                                             # Approximating c using our approximate solution x_star                 


    x_exact = np.identity(N,float)[:,0]                             # Due to the selection of the resultant vector c as being the first
                                                                    # column of matrix A, it MUST be the case that the exact soluion to the
                                                                    # system Ax=c is the first column of the appropriate identitiy matrix (e1)


    rel_res = ( sciln.norm((c_true - c_approx), 2)                  # Here we calculate the relative residual for the current matrix A using
                /sciln.norm(c_true,2) )                             # ||c_true - c_approx|| / ||c_true||


    max_rel_error = cond_A*rel_res                                  # Calculating the upper bound for the relative error using the condition
                                                                    # number of matrix A and the relative residual of matrix A 


    rel_error = ( sciln.norm((x_exact-x_star),2)                    # Using the known exact solution and our approximation to determine the
                  /sciln.norm(x_exact) )                            # relative error for each matrix


    iterations[N-2] = np.array([N, cond_A, rel_res, rel_error,      # Adding current iteration to record
                       max_rel_error],object)


# defining relevant axis
sizes = iterations[:,0]
rel_errors = iterations[:,3]
max_rel_errors = iterations[:,4]
rel_reses = iterations[:,2]

# Create a figure with 1 subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plotting relative error
ax.semilogy(sizes, rel_errors, '-o', label='Relative Error')

# Plotting maximal error
ax.semilogy(sizes, max_rel_errors, '-o', label='Maximal Relative Error')

# Plotting relative residuals
ax.semilogy(sizes, rel_reses, '-o', label='Relative Residuals')



# Adding labels and a title
ax.set_xlabel('Size of NxN Matrix')
ax.set_ylabel('Error')
ax.set_title('Relative Error, Maximal Relative Error and Relative Residuals with Increasing Matrix Sizes')
ax.legend()

plt.show()

