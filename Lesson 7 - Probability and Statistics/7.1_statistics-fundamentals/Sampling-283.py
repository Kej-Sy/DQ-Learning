"""
Identify which is the case, and assign to the corresponding variable the string 'population' or 'sample'. Here are the questions we need to answer:
1. What's the average salary of the individuals in our company working in IT roles? (Assign either 'population' or 'sample' to the variable question1.)
2. What's the proportion of individuals in the IT department having salaries under $60000? (Assign either 'population' or 'sample' to the variable question2.)
3. What's the minimum salary in the entire company? (Assign either 'population' or 'sample' to the variable question3.)
4. What's the minimum salary in the IT department of our company? (Assign either 'population' or 'sample' to the variable question4.)
5. What's the proportion of salaries under $20000 in the entire company? (Assign either 'population' or 'sample' to the variable question5.)
"""

## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
print(wnba.head())
print(wnba.tail())
print(wnba.shape)

parameter = wnba["Games Played"].max()

sample = wnba["Games Played"].sample(30, random_state=1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

sample_means = []
population_mean = wnba["PTS"].mean()

for i in range(100):    
    sample = wnba["PTS"].sample(10, random_state=i)
    sample_means.append(sample.mean())
    
plt.scatter(range(1,101), sample_means)
plt.axhline(population_mean)

plt.show()

## 7. Stratified Sampling ##

wnba["Points Per Game"] = wnba["PTS"] / wnba["Games Played"]

# Stratifying the data in five strata
stratum_C = wnba[wnba.Pos == "C"]
stratum_F = wnba[wnba.Pos == "F"]
stratum_G = wnba[wnba.Pos == "G"]
stratum_FC = wnba[wnba.Pos == "F/C"]
stratum_GF = wnba[wnba.Pos == "G/F"]

points_per_position = {}

for stratum, position in [(stratum_C, "C"), (stratum_F, "F"), (stratum_FC, "F/C"), (stratum_G, "G"), (stratum_GF, "G/F")]:
    # simple random sampling on each stratum
    sample = stratum["Points Per Game"].sample(10, random_state=0)
    points_per_position[position] = sample.mean()
    
position_most_points = max(points_per_position, key = points_per_position.get)

## 8. Proportional Stratified Sampling ##

stratum_1 = wnba[wnba["Games Played"] <= 12]
stratum_2 = wnba[(wnba["Games Played"] > 12) & (wnba["Games Played"] <= 22)]
stratum_3 = wnba[wnba["Games Played"] > 22]

proportional_sampling_means = []

for i in range(100):
    sample_under_12 = stratum_1["PTS"].sample(1, random_state=i)
    sample_btw_13_22 = stratum_2["PTS"].sample(2, random_state=i)
    sample_over_23 = stratum_3["PTS"].sample(7, random_state=i)
    final_sample = pd.concat([sample_under_12, sample_btw_13_22, sample_over_23])
    proportional_sampling_means.append(final_sample.mean())
    
plt.scatter(range(1,101), proportional_sampling_means)
plt.axhline(wnba["PTS"].mean())

plt.show()

## 10. Cluster Sampling ##

clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)

sample = pd.DataFrame()

for cluster in clusters:
    data_collected = wnba[wnba['Team'] == cluster]
    sample = sample.append(data_collected)
    
mean_height = sample["Height"].mean()
mean_age = sample["Age"].mean()
mean_BMI = sample["BMI"].mean()
mean_total_points = sample["PTS"].mean()

sampling_error_height = wnba["Height"].mean() - mean_height
sampling_error_age = wnba["Age"].mean() - mean_age
sampling_error_BMI = wnba["BMI"].mean() - mean_BMI
sampling_error_points = wnba["PTS"].mean() - mean_total_points