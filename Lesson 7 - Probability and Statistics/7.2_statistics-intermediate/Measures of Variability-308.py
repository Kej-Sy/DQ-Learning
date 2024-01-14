## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def find_range(array):
    return max(array) - min(array)

range_by_year = {}

for year in houses['Yr Sold'].unique():
    data_by_year = houses[houses['Yr Sold'] == year]
    range_by_year[year] = find_range(data_by_year['SalePrice'])
        
'''Using the measures of variability you got, assess the truth value of the following sentences:'''

'''1. Prices had the greatest variability in 2008. If you consider this sentence true, assign the boolean True to a variable named one, otherwise assign False.'''
one = False

''' 2. Prices variability had a peak in 2007, then the variability started to decrease until 2010 when there was a short increase in variability compared to the previous year (2009). If you consider this sentence true, assign the boolean True to a variable named two, otherwise assign False.'''
two = True

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def average_distance(array):
    mean = sum(array) / len(array)
    distances = []
    for value in array:
        distance = value - mean
        distances.append(distance)
    return sum(distances) / len(distances)

avg_distance = average_distance(C)
print(avg_distance)

'''The average distance was 0. This is because the mean is the balance point of the distribution and, as we've learned, the total distance of the values that are above the mean is the same as the total distance of the values below the mean.'''

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def mean_absolute_deviation(array):
    mean = sum(array) / len(array)
    distances = []
    
    for value in array:
        deviation = abs(value - mean)
        distances.append(deviation)
    
    return sum(distances) / len(distances)

mad = mean_absolute_deviation(C)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def variance(array):
    mean = sum(array) / len(array)
    distances = []
    
    for value in array:
        squared_distance = (value - mean) ** 2
        distances.append(squared_distance)
        
    return sum(distances) / len(distances)

variance_C = variance(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standard_deviation(array):
    mean = sum(array) / len(array)
    distances = []
    
    for value in array:
        squared_distance = (value - mean) ** 2
        distances.append(squared_distance)
        
    return sqrt(sum(distances) / len(distances))

standard_deviation_C = standard_deviation(C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

# Measure first the variability for each year
years = {}

for year in houses['Yr Sold'].unique():
    year_segment = houses[houses['Yr Sold'] == year]
    st_dev = standard_deviation(year_segment['SalePrice'])
    years[year] = st_dev
    
# Get years of max and min variability
greatest_variability = max(years, key = years.get)
lowest_variability = min(years, key = years.get)

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread = 'sample 2'

st_dev1 = standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)
    
plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))

plt.show()

'''Most sample standard deviations are clustered below the population standard deviation.'''

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances) - 1) # implementing Bessel's correction
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

plt.hist(st_devs)
plt.axvline(pop_stdev)  # pop_stdev is pre-saved from the last screen

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std()

numpy_stdev = std(sample['SalePrice'], ddof = 1)

equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample['SalePrice'].var()

numpy_var = var(sample['SalePrice'], ddof = 1)

equal_vars = pandas_var == numpy_var

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

from numpy import var, std

variances = []
st_devs = []

for sample in samples:
    st_devs.append(std(sample, ddof = 1))
    variances.append(var(sample, ddof = 1))
    
mean_std = sum(st_devs) / len(st_devs)
mean_var = sum(variances) / len(variances)

pop_std = std(population, ddof = 0)
pop_var = var(population, ddof = 0)

equal_stdev = mean_std == pop_std
equal_var = mean_var == pop_var
    