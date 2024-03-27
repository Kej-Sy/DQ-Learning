## 1. Introduction to Gradient Descent: Finding the Bottom ##

def array_minimum(array):
    minimum = array[0]
    for num in array[1:]:
        if num < minimum:
            minimum = num
    return minimum

## 2. Finding the Bottom ##

def step_by_step_minimum(array):
    length = len(array)
    for index in range(length-1):
        if array[index] < array[index+1]:
            return index, array[index]
    return length - 1, array[length - 1]

## 3. Random Starting Point ##

def step_by_step_minimum(array):
    length = len(array)
    for index in range(length - 1):
        if array[index] < array[index+1]:
            return index, array[index]
    return length - 1, array[length - 1]

def step_by_step_random(array, index):
    fetch_minimum = lambda x: step_by_step_minimum(x)[1]
    length = len(array)
    if index == 0:
        return fetch_minimum(array)
    elif index == length - 1:
        return fetch_minimum(array[::-1])
    elif array[index-1] < array[index+1]:
        return fetch_minimum(array[:index+1][::-1])
    return fetch_minimum(array[index:])

## 6. Univariate Gradient Descent Algorithm ##

def derivative(x):
    return 2*(x-1)

def update(x, alpha):
    return x - alpha * derivative(x)

def gradient_descent(x_0, alpha, iter_):
    values = [x_0]
    x= x_0
    for n in range(iter_):
        x = update(x, alpha)
        values.append(x)
    return values

'''
For either of the mathematical functions: x^2 and (x-1)^2, what happens when the learning rate is 1? Assign the right option to lr.
1. The values are always 1
2. The values alternate between two numbers
3. The values quickly converge to the minimum
4. The values are always the same
'''
lr = 2

## 7. Stopping Criteria ##

def f(x):
    return pow(x-1, 2)

def derivative(x):
    return 2*(x - 1)

def update(x, alpha):
    return x - alpha*derivative(x)

def gradient_descent(x_0, alpha, tolerance, max_iter):
    x = x_0
    
    for n in range(max_iter):
        previous_image = f(x)
        x = update(x, alpha)
        current_image = f(x)
        
        if abs(previous_image - current_image) < tolerance:
            break
        
    return x, f(x)