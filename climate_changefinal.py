# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:04:12 2023

@author: MUSTANG
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data(file_path):
    # Read climate change data into Pandas dataframe
    cc = pd.read_csv(file_path, skiprows=3)
    
    return cc

cc = data("climate_change.csv")
cc = cc[cc['Indicator Name'].isin(['Urban population (% of total population)', 'Population, total', 'CO2 emissions (kt)'])]
print(cc)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data(file_path):
    # Read climate change data into Pandas dataframe
    cc = pd.read_csv(file_path, skiprows=3)
    cc_T = cc.transpose()
    cc_T = cc_T.drop(['Country Code', 'Indicator Code', 'Unnamed: 66'], axis=0)
    cc_T.columns = cc_T.iloc[0]
    cc2_T = cc_T.iloc[1:]
    
    return cc, cc2_T

cc, cc2_T = data("climate_change.csv")

cc.head()
cc2_T.head()
print(cc2_T)

cc2_T.T
trans = cc2_T.T[cc2_T.T['Indicator Name'].isin(['Urban population (% of total population)', 'Population, total', 'CO2 emissions (kt)'])]
final = trans.T[['France', 'Italy','Germany', 'Spain', 'United Kingdom']]
final.dropna(inplace = True)
final = final.iloc[15:25,:]

urban_pop = final.iloc[1:,[0,3,6,9,12]]
print(urban_pop)

# Statistical function for urban population
print(urban_pop.describe())

# Mean for urban population
print(urban_pop.mean())

# Median for urban population
print(urban_pop.median())

# Standard deviation for urban population
print(urban_pop.std())

# line plot
plt.figure()

# plot the five countries with labels
urban_pop.plot()

# set labels and show the legend

plt.xlabel("Country Name")
plt.ylabel("Urban Population(millions)")
plt.title('Urban Population of 5 Countries (2005 - 2013)') 
plt.legend(bbox_to_anchor=(1.2,0.5))

plt.show()

total_pop = final.iloc[1:,[1,4,7,10,13]]
print(total_pop)

# Statistical function for total population
print(total_pop.describe())

# Mean for total population
print(total_pop.mean())

# Median for total population
print(total_pop.median())

# Standard deviation for total population
print(total_pop.std())

# Bar plot
plt.figure()

# plot the total population of the five countries with labels
total_pop.T.plot(kind='bar')

plt.title('Total Population of 5 Countries (2005 - 2013)') 
plt.legend(bbox_to_anchor=(1.2,0.5))

plt.show()

CO2 = final.iloc[1:,[2,5,8,11,14]]
CO2
CO2.index = pd.to_numeric(CO2.index)
print(CO2)

# Statistical function for CO2 emissions
print(CO2.describe())

# Mean for CO2 emissions
print(CO2.mean())

# Median for CO2 emissions
print(CO2.median())

# Standard deviation for CO2 emissions
print(CO2.std())

# Scatter plot
plt.figure()

# Scatter plot with Germany and CO2
plt.scatter(urban_pop['Germany'], CO2['Germany'])

# set labels and show the legend

plt.xlabel("CO2")
plt.ylabel('Population(millions)')
plt.title('Scatter plot of Germany with CO2 Emissions (2005 - 2013)')

plt.show()
