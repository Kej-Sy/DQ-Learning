## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()

mean_original = houses['SalePrice'].mean()

difference = mean_original - mean_new

## 2. Different Weights ##

sum_per_year = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']

all_sums_together = sum(sum_per_year)

total_n_houses = sum(houses_per_year['Houses Sold'])

weighted_mean = all_sums_together / total_n_houses

mean_original = houses['SalePrice'].mean()

difference = mean_original - weighted_mean

## 3. The Weighted Mean ##

import numpy as np

def weighted_mean(distribution, weights):
    weighted_sum = []
    for mean, weight in zip(distribution, weights):
        weighted_sum.append(mean * weight)
        
    return sum(weighted_sum) / sum(weights)

weighted_mean_function = weighted_mean(houses_per_year['Mean Price'], 
                                       houses_per_year['Houses Sold'])

weighted_mean_numpy = np.average(houses_per_year['Mean Price'], 
                                 weights = houses_per_year['Houses Sold'])

equal = weighted_mean_function == weighted_mean_numpy

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

rooms = houses['TotRms AbvGrd'].copy()
rooms_sorted = rooms.replace({'10 or more': 10}).astype(int).sort_values()

median = rooms_sorted.median()
lenght = len(rooms_sorted)

# Another way
# Find the median
middle_indices = [int((len(rooms_sorted) / 2) - 1),
                  int((len(rooms_sorted) / 2))
                 ] # len - 1 and len because Series use 0-indexing 
middle_values = rooms_sorted.iloc[middle_indices] 
median1 = middle_values.mean()

## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt

houses['Lot Area'].plot.box()
plt.show()

houses['SalePrice'].plot.box()
plt.show()

lotarea_mean = houses['Lot Area'].mean()
lotarea_median = houses['Lot Area'].median()

lotarea_difference = lotarea_mean - lotarea_median

saleprice_mean = houses['SalePrice'].mean()
salepice_median = houses['SalePrice'].median()

saleprice_difference = saleprice_mean - salepice_median

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()

houses['Overall Cond'].plot.hist()

plt.show()

more_representative = 'mean' 

'''
The mean seems more representative and more informative because it captures the fact that there are more houses rated above 5 than rated under 5. Because of this, the mean is slightly shifted above 5. 
'''