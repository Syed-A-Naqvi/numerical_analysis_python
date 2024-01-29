
import pytest as pt
import numpy as np
from NonLinEqnsA4 import NonLinEqns

def test_eqns():

    value = np.array([ 11.94522602 ,-37.58462299]) 
    
    x = np.array([np.sqrt(5), 0.31])
    f = NonLinEqns(x)
    
#    print(np.linalg.norm(f-value,2) <= 1.0e-6)
    
    assert np.linalg.norm(f-value,2) <= 1.0e-6