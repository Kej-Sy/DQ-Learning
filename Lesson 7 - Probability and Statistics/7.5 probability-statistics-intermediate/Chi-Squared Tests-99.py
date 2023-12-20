## 2. Calculating Differences ##

'''
On the last screen, our observed values were 10771 Females, and 21790 Males. Our expected values were 16280.5 Females and 16280.5 Males.

- Compute the proportional difference in number of observed Females vs number of expected Females. Assign the result to female_diff.
- Compute the proportional difference in number of observed Males vs number of expected Males. Assign the result to male_diff.
'''

female_diff = (10771 - 16280.5) / 16280.5
male_diff = (21790 - 16280.5) / 16280.5

## 3. Updating the Formula ##

'''
On the last screen, our observed values were 10771 Females, and 21790 Males. Our expected values were 16280.5 Females and 16280.5 Males.

- Compute the difference in number of observed Females vs number of expected Females using the updated technique. Assign the result to female_diff.
- Compute the difference in number of observed Males vs number of expected Males using the updated technique. Assign the result to male_diff.
- Add male_diff and female_diff together and assign to the variable gender_chisq.
'''

female_diff = (10771 - 16280.5) ** 2 / 16280.5
male_diff = (21790 - 16280.5) ** 2 / 16280.5
gender_chisq = male_diff + female_diff

## 4. Generating a Distribution ##

import numpy as np

chi_squared_values = []

for i in range(1000):
    sequence = np.random.random((32561, ))
    sequence[sequence < 0.5] = 0
    sequence[sequence >= 0.5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    female_diff = (female_count - 16280.5) ** 2 / 16280.5
    male_diff = (male_count - 16280.5) ** 2 / 16280.5
    gender_chisq = male_diff + female_diff
    chi_squared_values.append(gender_chisq)
    
plt.hist(chi_squared_values)

## 6. Smaller Samples ##

'''
For example, our observed values are 107.71 Females, and 217.90 Males. Our expected values are 162.805 Females and 162.805 Males.

- Compute the difference in number of observed Females vs number of expected Females using the new formula. Assign the result to female_diff.
- Compute the difference in number of observed Males vs number of expected Males using the new formula. Assign the result to male_diff.
- Add male_diff and female_diff together and assign to the variable gender_chisq.
'''

female_diff = (107.71 - 162.805) ** 2 / 162.805
male_diff = (217.90 - 162.805) ** 2 / 162.805
gender_chisq = male_diff + female_diff

## 7. Sampling Distribution Equality ##

chi_squared_values = []

for i in range(1000):
    sequence = np.random.random((300, ))
    sequence[sequence < 0.5] = 0
    sequence[sequence >= 0.5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    male_diff = (male_count - 150) ** 2 / 150
    female_diff = (female_count - 150) ** 2 / 150
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)

## 9. Increasing Degrees of Freedom ##

diffs = []

observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i, obs in enumerate(observed):
    exp = expected[i]
    diff = (obs - exp) ** 2 / exp
    diffs.append(diff)
    
race_chisq = sum(diffs)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]
chisquare_value, race_pvalue = chisquare(observed, expected)