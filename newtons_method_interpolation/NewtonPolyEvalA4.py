

#  Evaluates polynomial interpolant constructed from Newton polynomial basis 


import numpy as np


def NewtonPolyEval(a,xs,xx):    # input:  a (numpy array containing coefficients of interpolating polynomial
                                #             written in terms of the Newton polynomial basis)
                                #         xs (numpy array containing x values of interpolating nodes)
                                #         xx (numpy array containing x values at which interpolant is to be evaluated)
    
    # code for evaluating interpolant
    
    np1=np.shape(a)[0]
    
    yy=np.full((len(xx),),a[np1-1])
    
    for i in range(len(xx)):
        for j in range(np1-2,-1,-1):
            yy[i] = yy[i]*(xx[i]-xs[j]) + a[j]
           
       
        
    return yy                   # return numpy array containing values for interpolant evaluated xx