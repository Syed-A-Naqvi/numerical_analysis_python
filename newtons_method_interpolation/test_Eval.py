
import pytest as pt
import numpy as np
from NewtonPolyEvalA4 import NewtonPolyEval

def test_eval():
 
    xs = np.linspace(0,4,6)
    a = np.array([ 1. , -0.125 , -0.7890625 ,  0.546875 ,  -0.05900065 , -0.10655721])
    x = np.linspace(1,3,6)

    A = np.array([ 0.68103394 , 0.09262329 ,-0.46791626, -0.7122644,  -0.45381958,  0.26136353] )
    
    yy = NewtonPolyEval(a,xs,x)
    
#    print(np.linalg.norm(A-yy,2) <= 1.0e-6)
    
    assert np.linalg.norm(A-yy,2) <= 1.0e-6