## 2. Grouped Bar Plots ##

import matplotlib.pyplot as plt
plt.figure().set_figwidth(8)

import seaborn as sns
sns.set_theme()

sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba, 
              order = ['Rookie', 'Little experience', 'Experienced', 
                      'Very experienced', 'Veteran'],
             hue_order = ['C', 'F', 'F/C', 'G', 'G/F'])
plt.show()

## 3. Challenge: Do Older Players Play Less? ##

'''wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')'''

sns.set_theme()

sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative', data = wnba)
plt.show()

'''
Hypothesis: Let's hypothesize that older players generally play less than this average of 497 minutes, while younger players generally play more.
Analyze the graph and determine whether the data confirms or rejects our hypothesis. If it's a confirmation assign the string 'confirmation' to a variable named result. If it's a rejection, assign the string 'rejection' to the variable result.'''

result = 'rejects'

## 4. Comparing Histograms ##

wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()

plt.show()

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()
plt.show()

print('''We can still observe that most of the old players that belong to the "average or above" category play significantly more than average. With the help of the vertical line, the pattern is very easy to notice. Because the graph looks much cleaner than the one with step-type histograms, we can easily argue that the pattern is much more obvious in the case of kernel density plots.''')

## 7. Strip Plots ##

sns.set_theme()

sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)
plt.show()

print('''The patterns we see are similar to those we saw for heights. This can be easily explained by the fact that there's a strong positive relation between a player's height and her weight: the taller the player, the heavier she is; the shorter the player, the lighter she is.''')

## 8. Box plots ##

sns.set_theme()

sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)
plt.show()

## 9. Outliers ##

sns.set_theme()

iqr = 29 - 22

lower_bound = 22 - iqr * 1.5
upper_bound = 29 + iqr * 1.5

# True values will count as 1 in the summation
outliers_low = sum(wnba['Games Played'] < lower_bound)
outliers_high = sum(wnba['Games Played'] > upper_bound)

sns.boxplot(wnba['Games Played'])
plt.show()