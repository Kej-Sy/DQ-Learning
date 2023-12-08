## 1. Introduction ##

import pandas as pd

houses = pd.read_table('AmesHousing_1.txt')

scale_land = 'ordinal'

scale_roof = 'nominal'

kitchen_variable = 'discrete'

## 2. The Mode for Ordinal Variables ##

def mode(array):
    dictionary = {}
    for value in array:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1
    return max(dictionary, key=dictionary.get)

mode_function = mode(houses['Land Slope'])

mode_method = houses['Land Slope'].mode()

same = mode_function == mode_method

## 3. The Mode for Nominal Variables ##

# The function we wrote (you can copy-paste yours from the previous screen)
def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return (max(counts, key = counts.get), counts)

mode, value_counts = mode(houses['Roof Style'])

print(houses['Roof Style'].value_counts())

## 4. The Mode for Discrete Variables ##

bedroom_variable = 'discrete'
bedroom_mode = houses['Bedroom AbvGr'].mode()

price_variable = 'continuous'

## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)

mode = 150000
mean = houses['SalePrice'].mean()
median = houses['SalePrice'].median()


'''The mode is lower than the median, and the median is lower than the mean. If you think this is true, assign the boolean True to a variable named sentence_1, otherwise assign False.'''
sentence_1 = True

'''The mean is greater than the median, and the median is greater than the mode. Assign True or False to a variable named sentence_2.'''
sentence_2 = True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

'''In the code editor you can see the mean, mode and median for three distributions. Indicate whether the mean, median, and mode of each distribution suggest a left or a right skew.'''

'''If the values for distribution_1 indicate a right skew, assign the string 'right skew' to a variable named shape_1, otherwise assign 'left skew'.'''
shape_1 = 'right skew'

'''If the values for distribution_2 indicate a right skew, assign the string 'right skew' to a variable named shape_2, otherwise assign 'left skew'.'''
shape_2 = 'right skew'

'''If the values for distribution_3 indicate a right skew, assign the string 'right skew' to a variable named shape_3, otherwise assign 'left skew'.'''
shape_3 = 'left skew'

## 7. Symmetrical Distributions ##

import matplotlib.pyplot as plt

houses['Mo Sold'].plot.kde(xlim = [1, 12])
plt.axvline(houses['Mo Sold'].mode()[0], color = 'Green', label = 'Mode')
plt.axvline(houses['Mo Sold'].median(), color = 'Orange', label = 'Median')
plt.axvline(houses['Mo Sold'].mean(), color = 'Black', label = 'Mean')
plt.legend()

plt.show()