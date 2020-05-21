# Pandas Dataframes
# Pandas is a high-level data manipulation tool developed by Wes McKinney.
# It is built on the Numpy package and its key data structure is called the DataFrame.
# DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.
# There are several ways to create a DataFrame. One way way is to use a dictionary.
# Ex:-----
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
# -----

# As you can see with the new brics DataFrame, Pandas has assigned a key for each country
# as the numerical values 0 through 4. If you would like to have different index values, say,
# the two letter country code, you can do that easily as well.

print("\n")
# -----
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)
# -----
# Another way to create a DataFrame is by importing a csv file using Pandas.
# Now, the csv cars.csv is stored and can be imported using pd.read_csv:
# (note: since following the online tutorial, do not have access to cars.csv, so output simulated below)
"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
"""
# outputs
"""
<script.py> output:
      Unnamed: 0  cars_per_cap        country drives_right
    0         US           809  United States         True
    1        AUS           731      Australia        False
    2        JAP           588          Japan        False
    3         IN            18          India        False
    4         RU           200         Russia         True
    5        MOR            70        Morocco         True
    6         EG            45          Egypt         True
"""

# Indexing DataFrames
# There are several ways to index a Pandas DataFrame.
# One of the easiest ways to do this is by using square bracket notation.

# In the example below, you can use square brackets to select one column of the cars DataFrame.
# You can either use a single bracket or a double bracket.
# The single bracket with output a Pandas Series, while a double bracket will output a Pandas DataFrame.
# Ex:
"""
# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])
"""
# Output:
"""
<script.py> output:
    US     809
    AUS    731
    JAP    588
    IN      18
    RU     200
    MOR     70
    EG      45
    Name: cars_per_cap, dtype: int64
         cars_per_cap
    US            809
    AUS           731
    JAP           588
    IN             18
    RU            200
    MOR            70
    EG             45
         cars_per_cap        country
    US            809  United States
    AUS           731      Australia
    JAP           588          Japan
    IN             18          India
    RU            200         Russia
    MOR            70        Morocco
    EG             45          Egypt
"""
# Square brackets can also be used to access observations (rows) from a DataFrame. For example:
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 4 observations
print(cars[0:4])

# Print out fifth and sixth observation
print(cars[4:6])
"""
# Output:
"""
<script.py> output:
         cars_per_cap        country drives_right
    US            809  United States         True
    AUS           731      Australia        False
    JAP           588          Japan        False
    IN             18          India        False
         cars_per_cap  country drives_right
    RU            200   Russia         True
    MOR            70  Morocco         True
"""

#You can also use loc and iloc to perform just about any data selection operation.
# loc is label-based, which means that you have to specify rows and columns based on their
# row and column labels.
# iloc is integer index based, so you have to specify rows and columns by their integer index
# like in the previous exercise.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
"""
# Output:
"""
<script.py> output:
    cars_per_cap      588
    country         Japan
    drives_right    False
    Name: JAP, dtype: object
         cars_per_cap    country drives_right
    AUS           731  Australia        False
    EG             45      Egypt         True
"""
