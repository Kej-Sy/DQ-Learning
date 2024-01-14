## 2. Frequency Distribution Tables ##

freq_distro_pos = wnba['Pos'].value_counts()

freq_distro_height = wnba['Height'].value_counts()

## 3. Sorting Frequency Distribution Tables ##

age_ascending = wnba['Age'].value_counts().sort_index()

age_descending = wnba['Age'].value_counts().sort_index(ascending = False)

#How many players are under 20?
#There are no players under 20.

#How many players are 30 or over?
#There are 38 plaeyrs how are 30 or over.

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below
pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4, 3, 0, 2, 1, 5]]

## 5. Proportions and Percentages ##

proportion_25 = wnba['Age'].value_counts(normalize=True)[25]
percentages = wnba['Age'].value_counts(normalize = True).sort_index() * 100
percentage_30 = percentages[30]
percentage_over_30 = percentages.loc[30:].sum()
percentage_below_23 = percentages.loc[:23].sum()

## 6. Percentiles and Percentile Ranks ##

from scipy.stats import percentileofscore

percentile_rank_half_less = percentileofscore(wnba['Games Played'], 17, kind='weak')

percentage_half_more = 100 - percentileofscore(wnba['Games Played'], 17, kind='weak')

## 7. Finding Percentiles with pandas ##

age_upper_quartile = wnba['Age'].describe().iloc[6]
age_middle_quartile = wnba['Age'].describe().iloc[5]
age_95th_percentile = wnba['Age'].describe(percentiles = [.95])[5]

'''A percentile is a value of a variable, and it corresponds to a certain percentile rank in the distribution of that variable. (If you think this is true, assign True (boolean, not string) to a variable named question1, otherwise assign False.)'''
question1 = True

'''A percentile rank is a numerical value from the distribution of a variable. (Assign True or False to question2.)'''
question2 = False

'''The 25th percentile is the same thing as the lower quartile, and the upper quartile is the same thing as the third quartile. (Assign True or False to question3)'''
question3 = True

## 8. Grouped Frequency Distribution Tables ##

grouped_freq_table = wnba['PTS'].value_counts(bins=10, normalize=True).sort_index(ascending=False) * 100

## 10. Readability for Grouped Frequency Tables ##

intervals = pd.interval_range(start = 0,end = 600, freq = 60)

gr_freq_table_10 = wnba['PTS'].value_counts(bins = intervals).sort_index()