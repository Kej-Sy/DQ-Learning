## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers["Year"] > 1959]

true_avengers['Year'].hist()

## 5. Consolidating Deaths ##

new = true_avengers["Death1"] + true_avengers["Death2"]

def clean_deaths(row):
    num_deaths = 0
    columns = ["Death1", "Death2", "Death3", "Death4", "Death5"]
    
    for column in columns:
        death = row[column]
        if pd.isnull(death) or death == 'NO':
            continue
        else:
            num_deaths += 1
            
    return num_deaths
        
true_avengers["Deaths"] = true_avengers.apply(clean_deaths, axis=1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()

since_joining = 2015 - true_avengers["Year"]

correct_joined_years = true_avengers[true_avengers["Years since joining"] == (2015 - true_avengers["Year"])]
joined_accuracy_count  = len(correct_joined_years)