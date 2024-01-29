
import pytest as pt
import numpy as np
from NewtonPolyBuildA4 import NewtonPolyBuild

def test_build():
 
    xs = np.linspace(0,4,6)

    A = np.array([[ 1. ,     0. ,     0. ,     0. ,     0. ,     0.    ],
                      [ 1. ,     0.8 ,    0. ,     0. ,     0. ,     0.    ],
                      [ 1. ,     1.6 ,    1.28 ,   0. ,     0. ,     0.    ],
                      [ 1. ,     2.4 ,    3.84 ,   3.072 ,  0. ,     0.    ],
                      [ 1. ,     3.2 ,    7.68 ,  12.288 ,  9.8304 , 0.    ],
                      [ 1. ,     4.  ,   12.8  ,  30.72  , 49.152 , 39.3216]]) 
    
    V = NewtonPolyBuild(xs)
    
 #   print(np.linalg.norm(A-V,2) <= 1.0e-6)
    
    assert np.linalg.norm(A-V,2) <= 1.0e-6