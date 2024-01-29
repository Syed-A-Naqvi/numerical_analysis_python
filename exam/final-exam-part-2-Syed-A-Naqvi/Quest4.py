#  Starter code for Question 4 of Final Exam Part 2


#  import functions and modules you will use
import numpy as np
import numpy.linalg as npln


#  insert code for computing Maximal Relative Error 
A = np.array([[1.0,0.0,-1.1],[1.0,0.0,1.8],[1.0,2.0,11.9]])
b = np.array([1.0,1.0,3.0])
xstar = np.array([1.000018,0.999989,0.000024])

#residual
res = npln.norm(b - A@xstar, 2)

#relative residual
rel_res = npln.norm(b - A@xstar, 2)/npln.norm(b, 2)

#maximal relative error
max_rel_err = npln.cond(A) * rel_res


#   write out solution 
print(max_rel_err)


