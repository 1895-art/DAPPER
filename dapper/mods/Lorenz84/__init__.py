"""A chaotic system of size 3, like Lorenz-63, but with +complex geometry.

Refs:
- E.N. Lorenz, Irregularity: a fundamental property of the atmosphere,
  Tellus A 36 (1984) 98–110.
- E.N. Lorenz, Alook at some details of the growth of initial uncertainties,
  Tellus A 57 (2005) 1–11
"""

import numpy as np

import dapper as dpr
from dapper.tools.math import integrate_TLM

# Constants
a = 0.25
b = 4
F = 8.0
G = 1.23
# G = 1.0


@dpr.ens_compatible
def dxdt(x):
    d = np.zeros_like(x)
    x, y, z = x
    d[0] = - y**2 - z**2 - a*x + a*F
    d[1] = x*y - b*x*z - y + G
    d[2] = b*x*y + x*z - z
    return d


step = dpr.with_rk4(dxdt, autonom=True)

x0 = np.array([1.65,  0.49,  1.21])


def d2x_dtdx(x):
    x, y, z = x
    Mat = np.array(
        [[-a,   -2*y, -2*z],
         [y-b*z, x-1, -b*x],
         [b*y+z, b*x, x-1]])
    return Mat


def dstep_dx(x, t, dt):
    return integrate_TLM(d2x_dtdx(x), dt, method='approx')
