## 2. Inconsistent Systems ##

import numpy as np
import matplotlib.pyplot as plt

''''
8x + 4y = 5 -- 4y = -8x + 5 -- y = -2x + 5/4
4x + 2y = 5 -- 2y = -4x + 5 -- y = -2x + 5/2
'''

x = np.linspace(0, 20, 1000)

y1 = -2*x + 5/4
y2 = -2*x + 5/2

plt.plot(x, y1, c='blue')
plt.plot(x, y2, c='blue')
plt.show()

## 4. Possible Solutions For Nonhomogenous Systems ##

def test_solution(x3):
    x1 = 1 - 3*x3
    x2 = 1/2 + x3
    
    if x1 + 3*x3 == 1 and x1 + 2*x2 + x3 == 2:
        return True
    else:
        return False
    
boolean_one = test_solution(3)
boolean_two = test_solution(100)
boolean_three = test_solution(-10000)

## 5. Homogenous Systems ##

def test_homog(x3):
    x1 = 4/3*x3
    x2 = 0
    
    y1 = 6*x1 + 10*x2 + -8*x3
    y2 = -6*x1 - 4*x2 + 8*x3
    y3 = 3*x1 + 1/2*x2 - 4*x3
    
    if y1 == 0 and y2 == 0 and y3 == 0:
        return True
    else:
        return False
    
b_one = test_homog(1)
b_two = test_homog(-10)