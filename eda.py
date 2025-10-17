# This script serves to clean and explore the air-quality data for this project.

## Importing relavent packages ---
import numpy as np
import pandas as pd

## Loading in the data (in .gitignore file)
df = pd.read_csv('data/air_quality.csv')

## Convert variables to corresponding types
# df.info() # Checing types
### Objects variables to be converted to numericals
objs = ['so2', 'co', 'o3', 'o3_8hr', 
          'pm10', 'pm2.5', 'no2', 'nox', 'no', 
          'windspeed', 'winddirec', 'co_8hr', 
          'pm2.5_avg', 'pm10_avg', 'so2_avg']
df[objs] = df[objs].apply(pd.to_numeric, errors = 'coerce')
# df.info() # Confirming successful data type changes

### `date` variable to correct type
df['date'] = pd.to_datetime(df['date'], dayfirst = True, format = 'mixed')
df.sort_values(by = 'date', inplace = True, ignore_index = True)
# print(df.head()) # confirm that efforts were successful



print(df.isna().sum()) # Check for number of true NAs (a LOT)

## Convert invalid values to true NA
### This inclued invalids for pollutants and target (aqi)

## Fill in NA values

## Produce summary statistics

## Find most prevalent pollutant

## Find most polluted district

## Create final 4-month forecast of aqi for the remainder of the 2024 year

