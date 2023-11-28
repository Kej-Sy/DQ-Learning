## 2. Bar Plots ##

import matplotlib.pyplot as plt

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()
plt.show()

## 3. Horizontal Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title='Number of players in WNBA by level of experience')
plt.show()

## 4. Pie Charts ##

wnba['Exp_ordinal'].value_counts().plot.pie()
plt.show()

## 5. Customizing a Pie Chart ##

wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6, 6), autopct = '%.2f%%', title = "Percentage of players in WNBA by level of experience")
plt.ylabel('')
plt.show()

## 6. Histograms ##

wnba['PTS'].plot.hist()
plt.show()

## 7. The Statistics Behind Histograms ##

from numpy import arange

print(wnba['Games Played'].describe())

wnba['Games Played'].plot.hist()
plt.show()

## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range= (1, 32), bins = 8, title = "The distribution of players by games played")
plt.xlabel("Games played")
plt.show()

## 10. Skewed Distributions ##

wnba['AST'].plot.hist()
wnba['FT%'].plot.hist()
plt.show()

assists_distro = 'right skewed'
ft_percent_distro = 'left skewed'

## 11. Symmetrical Distributions ##

wnba['Age'].plot.hist()
plt.show()
wnba['Height'].plot.hist()
plt.show()
wnba['MIN'].plot.hist()
plt.show()

normal_distribution = 'Height'