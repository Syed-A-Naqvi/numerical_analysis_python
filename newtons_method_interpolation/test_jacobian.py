
import pytest as pt
import numpy as np
from JacobianA4 import Jacobian

def test_jacobian():

    value = np.array([[  16.48246215 ,   6.38636215],
                      [ -80.53063595 , -104.87158814]]) 
    
    x = np.array([np.sqrt(5), 0.31])
    f = Jacobian(x)
    
#    print(np.linalg.norm(f-value,2) <= 1.0e-6)
    
    assert np.linalg.norm(f-value,2) <= 1.0e-6