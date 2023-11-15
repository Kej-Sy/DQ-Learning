## 2. Connecting to the database ##

import sqlite3
conn = sqlite3.connect('world_population.db')
conn.close()

## 3. Executing Queries ##

import pandas as pd
import sqlite3

conn = sqlite3.connect("world_population.db")

query = "SELECT CountryName, Population FROM population WHERE Year = '2020' LIMIT 10;"
results = pd.read_sql_query(query, conn)

print(results)

conn.close()

## 4. Your Task ##

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('world_population.db')

# Write code below
# Write a SELECT query
query = '''
        SELECT CountryName, Year, Population
          FROM population
         WHERE CountryName = 'Poland'
'''

# Execute the query
results = pd.read_sql_query(query, conn)

# Printing results
print(results.head(10))

# Close the database connection
conn.close()

## 5. Creating a Data Visualization ##

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('world_population.db')

# Execute a SELECT query
query = """
    SELECT Year, Population 
      FROM population 
     WHERE CountryName ='Poland'
    """

# Retrieve the results of the query as a pandas dataframe
data = pd.read_sql_query(query, conn)

# Create a bar chart of the top 10 countries by population
plt.bar(data['Year'], data['Population'])
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population of Poland by Year')

# Show the plot
plt.show()

# Close the database connection
conn.close()

## 6. Putting It All Together ##

# Importing librries
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('world_population.db')

# Execute a SELECT query
query = """
        SELECT region, subregion, sum(PopChange) as TotalPopChange
          FROM population p
          JOIN country_mapping c ON p.CountryCode = c.CountryCode
         WHERE Year between 2010 and 2020
         GROUP BY region, subregion
         ORDER BY TotalPopChange DESC
         LIMIT 10;
    """

# Retrieve the results of the query as a pandas dataframe
data = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Create a bar chart of the top 10 countries by population
plt.barh(data['SubRegion'], data['TotalPopChange'])
plt.xlabel('Population Change')
plt.ylabel('Subregion')
plt.title('Top 10 Subregions by Population Change from 2010 to 2020')

# Show the plot
plt.show()