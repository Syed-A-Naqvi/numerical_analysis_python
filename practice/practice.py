import numpy as np
import scipy.interpolate

x = [1,2,3,4]
y = [1.2,0.4,0.3,0.5]

f = scipy.interpolate.CubicSpline(x,y)
f2 = scipy.interpolate.BarycentricInterpolator(x,y)

print(f2(1.5))
print(f(1.5))