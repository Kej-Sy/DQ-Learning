## 1. Multiple Conditions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if price == 0.0 and genre == "Games":
        free_games_ratings.append(rating)
        
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

## 2. The or Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == "Social Networking" or genre == "Games":
        games_social_ratings.append(rating)
        
avg_games_social = sum(games_social_ratings) / len(games_social_ratings)

## 3. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        non_free_games_social_ratings.append(rating)
        
avg_not_free = sum(non_free_games_social_ratings) / len(non_free_games_social_ratings)

# Not-free apps (average)

## 4. Comparison Operators ##

x = -6
y = 14
z = 8.5

if x > z:
    print("x is greater than z")
if y != z:
    print("y is not equal to z")
if x < z < y:
    print("z is between x and y")

## 5. Comparison Operator Applications ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

cost_more_than_9 = []

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price > 9:
        cost_more_than_9.append(rating)
        
avg_rating = sum(cost_more_than_9) / len(cost_more_than_9)

n_apps_more_9 = len(cost_more_than_9)

n_apps_less_9 = len(apps_data[1:]) - n_apps_more_9

## 6. The else Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append("free")
    else:
        app.append("not free")
        
apps_data[0].append("free_or_not")

print(apps_data[0][:5])

## 7. The elif Clause ##

app_ratings = [['Facebook', 3.5], ['Notion', 4.0], ['Astropad Standard', 4.5], ['NAVIGON Europe', 3.5]]

for row in app_ratings:
    rating = row[1]
    
    if rating < 3.0:
        row.append('below average')
    elif 3.0 <= rating < 4.0:
        row.append("roughly average")
    elif rating >= 4.0:
        row.append("better than average")
        
print(app_ratings)

## 8. Else vs. elif ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0:
        app.append("free")
    elif 0 < price < 20:
        app.append("affordable")
    elif 20<= price < 50:
        app.append("expensive")
    else:
        app.append("very expensive")
        
apps_data[0].append("price_label")

print(apps_data[0])
print(apps_data[1:5])