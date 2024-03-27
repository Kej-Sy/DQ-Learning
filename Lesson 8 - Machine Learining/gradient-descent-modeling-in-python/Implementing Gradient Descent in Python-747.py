## 1. Loss Function: Mean Squared Error ##

def mean_squared_error(y_true, y_predicted):
    cost = sum((y_true - y_predicted)**2) / len(y_true)
    return cost

## 2. Partial Derivatives ##

import pandas as pd

y = pd.Series(data=[1,2,3,4,5,6,7,8,9])
x = pd.Series(data=[1, 0, 6, 7, 6, 8, 8, 1, 9])
w = 0.7
b = 0.5

y_predicted = w*x + b
n = len(y_predicted)
weight_derivative = -(2/n) * sum(x*(y-y_predicted))
bias_derivative = -(2/n) * sum(y-y_predicted)

## 3. Initializing the Weights ##

def gradient_descent(x, y, iterations = 1000, learning_rate = 0.0001, tolerance = 1e-4, current_weight = 0.1, current_bias = 0.01): 
    
    n = float(len(x))
    
    costs = []
    weights = []
    previous_cost = None
    
    pass

## 4. Iterations ##

def gradient_descent(x, y,
                     iterations = 1000, learning_rate = 0.0001, tolerance = 1e-4,
                     current_weight = 0.1, current_bias = 0.01):
    n = float(len(x))
     
    costs = []
    weights = []
    previous_cost = None
    
    for i in range(iterations):
        
        y_predicted = (current_weight * x) + current_bias
        current_cost = mean_squared_error(y, y_predicted)
        
        if previous_cost and abs(previous_cost-current_cost) < tolerance:
            break
        
        previous_cost = current_cost
        
        costs.append(current_cost)
        weights.append(current_weight)
        
        weight_derivative = -(2/n) * sum(x * (y-y_predicted))
        bias_derivative = -(2/n) * sum(y-y_predicted)
        
        current_weight = current_weight - (learning_rate * weight_derivative)
        current_bias = current_bias - (learning_rate * bias_derivative)
        
    print(f"Iteration {i+1}: Cost {current_cost}")
        
    return current_weight, current_bias