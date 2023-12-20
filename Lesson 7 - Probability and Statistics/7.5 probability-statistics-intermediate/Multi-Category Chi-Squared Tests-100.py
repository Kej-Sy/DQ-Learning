## 2. Calculating Expected Values ##

rows = 32561

males_over50k = 0.241 * 0.67 * rows
males_under50k = 0.759 * 0.67 * rows
females_over50k = 0.241 * 0.33 * rows
females_under50k = 0.759 * 0.33 * rows

## 3. Calculating Chi-squared ##

chisq_gender_income = ((6662 - 5257.6) ** 2 / 5257.6 + 
                       (1179 - 2589.6) ** 2 / 2589.6 +
                       (15128 - 16558.2) ** 2 / 16558.2 +
                       (9592 - 8155.6) ** 2 / 8155.6)

## 4. Finding statistical significance ##

from scipy.stats import chisquare

expected = [5257.6, 2589.6, 16558.2, 8155.6]
observed = [6662, 1179, 15128, 9592]

chisq_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross Tables ##

import pandas as pd

table = pd.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding Expected Values ##

from scipy.stats import chi2_contingency

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(pd.crosstab(income["sex"], [income["race"]]))