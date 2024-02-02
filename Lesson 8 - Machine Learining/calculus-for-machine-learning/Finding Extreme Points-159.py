## 3. Differentiation ##

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 6, 110)
y = -2*x + 3

plt.plot(x, y)
plt.show()

## 6. Power Rule ##

derivative_one = '5x^4'
derivative_two = '9x^8'

slope_one = 5*(2**4)
slope_two = 9*(0**8)

print(slope_one)
print(slope_two)

## 7. Linearity Of Differentiation ##

derivative_three = '5x^4 - 1'
derivative_four = '3x^2 - 2x'

x=1
slope_three = 5*x**4 - 1

x=2
slope_four =3*x**2 - 2*x

## 8. Practicing Finding Extreme Values ##

derivative = '3x^2 - 2x = x(3x-2)'
#x(3x-2) = 0
#x = 0 v 3x-2 = 0
#x = 2/3 v x = 0

critical_points = [0, 2/3]

#0^3 - 0^2 = 0
#(2/3)^3 - (2/3)^2 = 8/27 - 4/9 = 8/27 - 12/27 = -4/27
x= -4 / 27

rel_min = [2/3]
rel_max = [0]