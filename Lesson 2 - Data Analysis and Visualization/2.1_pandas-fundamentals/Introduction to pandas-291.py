## 2. Introduction to the Data ##

import pandas as pd
f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None

f500_type = type(f500)
f500_shape = f500.shape

print(f500_type)
print(f500_shape)

## 3. Introducing DataFrames ##

f500_top_6 = f500.head(6)

f500_bottom_8 = f500.tail(8)

## 4. Introducing DataFrames Continued ##

f500.info()

float64_dtype = 3
int64_dtype = 7
object_dtype = 6

## 5. Selecting a Column from a DataFrame by Label ##

industries = f500["industry"]

industries_type = type(industries)

print(industries)
print(industries_type)

## 7. Selecting Columns from a DataFrame by Label Continued ##

countries = f500["country"]

revenues_years = f500[["revenues", "years_on_global_500_list"]]

ceo_to_sector = f500.loc[:, "ceo" : "sector"]

print(countries)

## 8. Selecting Rows from a DataFrame by Label ##

toyota = f500.loc["Toyota Motor"]

drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola", "Heineken Holding"]]

middle_companies = f500["Tata Motors":"Nationwide"]

print(toyota)

## 10. Value Counts Method ##

countries = f500["country"]

country_counts = countries.value_counts()

print(country_counts)
top_country = "USA"

hq_locations = f500["hq_location"]
hql_counts = hq_locations.value_counts()

print(hql_counts)
top_hq_city = "Beijing"

## 11. Selecting Items from a Series by Label ##

countries = f500["country"]
country_counts = countries.value_counts()

india = country_counts["India"]
print(type(india))

north_america = country_counts[["USA", "Canada", "Mexico"]]
print(type(north_america))

japan_to_spain = country_counts["Japan":"Spain"]
print(type(japan_to_spain))

## 12. Summary Challenge ##

big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"], "rank":"previous_rank"]

bottom_companies = f500.loc["National Grid":"AutoNation", ["rank", "sector", "country"]]

revenue_giants = f500.loc[["Apple", "Industrial & Commercial Bank of China", "China Construction Bank", "Agricultural Bank of China"], "revenues":"profit_change"]