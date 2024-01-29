
import pytest as pt
import numpy as np
from CompTrapA5 import CompTrap

def test_trap():
    
    f = lambda x : 2.0/np.sqrt(np.pi) * np.exp(-x**2)
    a = 0.5
    b = 2
    n = 10
     
    
    val = CompTrap(f,a,b,n)
    
#    print(np.abs(val-0.47631878665) <= 1.0e-8)
    
    assert np.abs(val-0.47631878665) <= 1.0e-8