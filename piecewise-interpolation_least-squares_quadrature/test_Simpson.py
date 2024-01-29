
import pytest as pt
import numpy as np
from CompSimpsonA5 import CompSimpson

def test_Simp():
    
    f = lambda x : 2.0/np.sqrt(np.pi) * np.exp(-x**2)
    a = 0.5
    b = 2
    n = 10
     
    
    val = CompSimpson(f,a,b,n)
    
#    print(np.abs(val-0.4748214652) <= 1.0e-8)
    
    assert np.abs(val-0.4748214652) <= 1.0e-8