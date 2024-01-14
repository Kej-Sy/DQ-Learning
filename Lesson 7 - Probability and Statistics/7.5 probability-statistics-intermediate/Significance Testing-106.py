## 3. Statistical Significance ##

import numpy as np
import matplotlib.pyplot as plt
'''
Null hypothesis: participants who consumed the weight loss pills lost the same amount of weight as those who didn't take the pill.

Alternative hypothesis: participants who consumed the weight loss pills lost more weight than those who didn't take the pill.
'''

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

## 4. Test Statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

'''
Null hypothesis: ¯xb−¯xa=0

Alternative hypothesis: ¯xb−¯xa>0
'''

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation Test ##

mean_difference = 2.52
print(all_values)

mean_differences = []

for i in range(1000):
    group_a = []
    group_b = []
    
    for weight_loss in all_values:
        
        if np.random.rand() >= 0.5:
            group_a.append(weight_loss)
        else:
            group_b.append(weight_loss)
            
    mean_group_a = np.mean(group_a)
    mean_group_b = np.mean(group_b)
    iteration_mean_difference = mean_group_b - mean_group_a
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)

plt.show()

## 7. Dictionary Representation of a Distribution ##

sampling_distribution = {}

for value in mean_differences:
    
    if sampling_distribution.get(value, False):
        sampling_distribution[value] += 1
    else:
        sampling_distribution[value] = 1

## 8. P Value ##

frequencies = []

for key in sampling_distribution.keys():
    
    if key >= 2.52:
        frequencies.append(sampling_distribution[key])
        
frequencies_sum = np.sum(frequencies)
p_value = frequencies_sum / 1000