# CSCI / MATH 2072U -- Computational Science 1
# Tutorial 3
# PA=LU decomposition 
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007

import numpy as np

def swap(M,p,q,k=False,no_Zeros=False):               # adding a parameter k specifing the amount of row elements to include in the swap
                                                      # adding a parameter no_zeros which will execute a conditional branch desined to
                                                      # only swap elements beginning at column index k which will avoid swapping zeros in
                                                      # the upper triangular matrix U


    if (k and no_Zeros):                              # swaps rows p and q beginning at column index k of a matrix M

        M_p = np.copy(M[p,k:])                        # creating a copy of elements in row p starting at column index k without linking M_P and M[p]
        M[p,k:] = np.copy(M[q,k:])                    # setting row p equal to a copy of row q from column index k onwards
        M[q,k:] = np.copy(M_p)                        # setting row q equal to a copy of a copy of row p from column index k onwards
    
    elif (k and not no_Zeros):                        # Swap rows p and q up to the kth element of a matrix M

        M_p = np.copy(M[p,:k])                        # creating a copy of the first k elements in row p without linking M_P and M[p]
        M[p,:k] = np.copy(M[q,:k])                    # setting first k elements of row p equal to a copy of the first k elements of row q
        M[q,:k] = np.copy(M_p)                        # setting first k elements of row q equal the copy of a copy of the first k elements of row p

    else:                                             # Swap all elements of rows p and q in matrix M 
        
        M_p = np.copy(M[p])                           # creating a copy of row p without linking M_P and M[p]
        M[p] = np.copy(M[q])                          # setting row p equal to a copy of row q
        M[q] = np.copy(M_p)                           # setting row q equal to a copy of row p

    return M                                          # returning the modified version of matrix M


def LUP(A):

    n = np.shape(A)[0]                                # extract matrix size
    U = np.copy(A)                                    # copy content of A (avoid linking U and A)
    U = U.astype(float)                               # casting the integer elements of U to floating points so that deciaml values are not truncated
    L = np.identity(n)                                # initialize L as the identity
    
    P = np.arange(0,n)                                # creating a permutation matrix P as a column vecor where each element
    P = P.reshape(n,1)                                # stores the index of the corresponding row of an identitiy matrix of size n


    for j in range(0,n-1):

        print(f"\n\n\n***************************_Iteration {j+1}_***************************")

        k = np.argmax(abs(U[j:,j])) + j               # find pivot element

        if (k != j ):                                 # if the pivot is not on the diagonal...
            
            print(f"U before swapping any rows:")
            print(np.round(U,3))
            
            print(f"\nCurrent pivot is the entry at row {j+1}, column {j+1}: {U[j,j]}")
            print(f"New pivot is the entry at row {k+1}, column {j+1}: {U[k,j]}",'\n')
            
            swap(U,j,k,j,True)                        # swap rows of U
            
            print(f"U after swapping rows {k+1} and {j+1} beginning at column {j+1}:")
            print(np.round(U,3),'\n\n')
            
            
            if (j > 0):                               # swap rows of L left of diagonal element
                
                print(f"L before swapping any rows:")
                print(np.round(L,3),'\n')
                swap(L,j,k,j)
                print(f"L after swapping entires in rows {k+1} and {j+1} before column {j+1}:")
                print(np.round(L,3),'\n\n')
                
            swap(P,j,k)                               # swap rows of P

        for i in range(j+1,n):                        # Gauss elimination of rows below pivot
            L[i,j] = (U[i,j]/U[j,j])
            U[i] = U[i] - (L[i,j]) * U[j]
        
        print(f"L after inserting multipliers into column {j+1} below diagonal:")
        print(np.round(L,3),'\n')
        print(f"U after Gaussian Elimination below entry at row {j+1}, column {j+1} (current pivot):")
        print(np.round(U,3))


    print("\nFinal permutation matrix as column vector:")
    print(P,'\n')

    Permutation = np.identity(n)                      # Rebuilding the permutation matrix P from a column vecotor of indecies to
    for i in range(n):                                # a proper nxn perumation matrix
        Permutation[i] = np.identity(n)[P[i,0]]
    P = Permutation                                                  

    print(f"Final permutation matrix as {n}x{n} matrix:")
    print(P,'\n')

    print('\n*****LU decomposition with partial pivoting complete...********\n\n')
    return L,U,P

A = np.array([[1.5,-1.2,0.3],[2.4,-3.3,-1.0],[2.2,2.9,1.3]])               # initializing a 3x3 array of integers

L,U,P = LUP(A)                                        # performing the LU decomposition with partial pivoting

print("Original Matirx:")                             # printing the original matrix A
print(A)

print("Permutation Matrix:")                          # printing the permutation matrix P
print(P)

print("Upper Triangualr Matrix:")                     # printing the upper triangular matrix U
print(np.round(U,3))

print("Lower Triangular Matrix:")                     # printing the lower triangular matrix L
print(np.round(L,3),'\n\n')

print("PA =")                                         # showing that PA is the same as LU meaning the decomposition was a success
print(np.round(P@A,3),"=",np.round(L@U,3),sep='\n')
print("= LU")