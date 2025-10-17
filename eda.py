# This script serves to clean and explore the air-quality data for this project.

## Importing relavent packages
import numpy as np 
import pandas as pd 

df = pd.read_csv('air_quality.csv')
print(df.head())
