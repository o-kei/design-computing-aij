import numpy as np
from scipy import integrate as itgr


pi = lambda x: 4.0 / (1.0 + x**2)
answer = itgr.quad(pi, 0, 1)
print(answer)
