# Life Expectancy and GDP Project

# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Inspect dataset

data = pd.read_csv('all_data.csv')
print(data.head())
print(data.GDP.describe())

# Plot univariate histograms and boxplots to gain a sense of distribution

# GDP Spread
sns.boxplot(data=data, x='GDP', hue='Country', palette='bright')
plt.title('GDP Range over 15 years by Country')
plt.savefig('gdp_spread_by_country.png')
plt.show()
plt.clf()


# Life expectancy spread

sns.boxplot(data=data, x='Life expectancy at birth (years)', hue='Country', palette='bright')
plt.title('Life Expectancy Range over 15 years by Country')
plt.savefig('life_expectancy_spread_by_country.png')
plt.show()
plt.clf()


# Look at country data changing over time

# GDP over time

sns.lineplot(data=data, x='Year', y='GDP', hue='Country')
plt.title('GDP Over Time by Country')
plt.savefig('gdp_over_time.png')
plt.show()
plt.clf()


# Life expectancy over time
sns.lineplot(data=data, x='Year', y='Life expectancy at birth (years)', hue='Country')
plt.title('Life Expectancy over Time by Country')
plt.savefig('life_expectancy_over_time.png')
plt.show()
plt.clf()


# Plot a multivariate visualization
countries = ['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe']
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
plt.figure(figsize=(10, 8))

for i in range(len(countries)):
    country = countries[i]
    color = colors[i]
    plt.subplot(3, 2, i+1)
    sns.scatterplot(data=data[data.Country == country], x='GDP', y='Life expectancy at birth (years)', color=color)
    if country == 'United States of America':
        plt.title('USA')
    else:
        plt.title(country)
plt.subplots_adjust(wspace=0.45, hspace=0.6)
plt.savefig('gdp_vs_life_expectancy_per_year_by_country.png')
plt.show()
plt.clf()
