## 1. Reading CSV files with NumPy ##

import numpy as np

taxi = np.genfromtxt("nyc_taxis.csv", delimiter = ",")
    
taxi_shape = taxi.shape

print(taxi)
print(taxi_shape)

## 2. Reading CSV Files with NumPy Continued ##

taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi_header_removed = taxi[1:]
removed_shape = taxi_header_removed.shape

taxi_header_skipped = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header = 1)
skipped_shape = taxi_header_skipped.shape

print(taxi_header_removed[:5])
print(taxi_header_skipped[:5])
print(removed_shape == skipped_shape)

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == "blue"
c_bool = c >100

print(a_bool)
print(b_bool)
print(c_bool)

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:, 1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:, 12]

tip_bool = tip_amount > 20

top_tips = taxi[tip_bool, 5:14]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

taxi_copy[1066, 5] = 1
taxi_copy[:, 0] = 16
taxi_copy[550:552, 7] = taxi_copy[:, 7].mean()

## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

trip_length = taxi_copy[:, 8]

taxi_copy[trip_length < 60] = 0

## 8. Assignment Using Boolean Arrays Continued ##

# create a new array filled with `0`
zeros = np.zeros([taxi.shape[0], 1])
# append the array to the taxi data to create a new column
taxi_modified = np.concatenate([taxi, zeros], axis=1)
# inspect the last five columns of the first ten rows
print(taxi_modified[:10, -5:])

taxi_modified[taxi_modified[:, 6] == 2, 15] = 1
taxi_modified[taxi_modified[:, 6] == 3, 15] = 1
taxi_modified[taxi_modified[:, 6] == 5, 15] = 1

## 9. Challenge: Which Is the Busiest Airport? ##

jfk = taxi[taxi[:, 5] == 2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:, 5] == 3]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:, 5] == 5]
newark_count = newark.shape[0]

busiest_airport = "laguardia"

## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_distance = taxi[:, 7] # trip distance in miles
trip_length = taxi[:, 8] / 3600 # trip length in hours
trip_mph = trip_distance / trip_length # average trip speed in mph

cleaned_taxi = taxi[trip_mph < 100]

mean_distance = cleaned_taxi[:, 7].mean()

mean_length = cleaned_taxi[:, 8].mean()

mean_total_amount = cleaned_taxi[:, 13].mean()