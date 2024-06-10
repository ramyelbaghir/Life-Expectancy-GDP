# Life Expectancy and GDP Data Analysis

## Introduction

As part of a larger curriculum on data science, ![alt text](D:\Computer Science\Visual Studio Scripts\Life-Expectancy-and-GDP-Starter\Life-Expectancy-and-GDP-Starter\all_data.csv "this small dataset") on GDP and life expectency at birth from the World Health Organization provides an opportunity to use visualizations to clarify trends and important variables in otherwise dense or inaccessible data.

## Exploration of Data

Investigated GDP and Life Expectancy Spread

![alt text](D:\Computer Science\Visual Studio Scripts\Life-Expectancy-and-GDP-Starter\Life-Expectancy-and-GDP-Starter\gdp_spread_by_country.png "GDP Spread by Country")
![alt text](D:\Computer Science\Visual Studio Scripts\Life-Expectancy-and-GDP-Starter\Life-Expectancy-and-GDP-Starter\life_expectancy_spread_by_country.png "Life Expectancy Spread by Country")

Then examined GDP and Life Expectancy over time by country

![alt text](D:\Computer Science\Visual Studio Scripts\Life-Expectancy-and-GDP-Starter\Life-Expectancy-and-GDP-Starter\gdp_over_time.png "GDP Over Time")
![alt text](D:\Computer Science\Visual Studio Scripts\Life-Expectancy-and-GDP-Starter\Life-Expectancy-and-GDP-Starter\life_expectancy_over_time.png "Life Expectancy Over Time")

## Patterns unveiled

GDP and Life Expectancy seem to be positively correlated -- as one variable increases, the other predictably increases alongside it. This correlation persists despite orders of magnitude of difference in different GDP values per country (e.g., Zimbabwe vs China.)

![alt text](D:\Computer Science\Visual Studio Scripts\Life-Expectancy-and-GDP-Starter\Life-Expectancy-and-GDP-Starter\gdp_vs_life_expectancy_per_year_by_country.png "GDP vs Life Expectancy by Country")

However, this positive correlation seems to have diminishing returns. After a certain GDP, the life expectancy for a particular country will only marginally increase by a couple of years, as seen by the United States' ever-growing GDP corresponding stagnant life-expectancy. Conversely, increases in GDP for a country like Zimbabwe (whose GDP quadrupled over the timespan in the dataset) will lead to a much larger increase in life expectancy. This is seen further by comparing the range of the Life-Expectancy axes for each country in the above visualization.

## Conclusion

This correlation reinforces the importance of economic growth as a contributor to life expectancy, as having a larger GDP theoretically affords a country's citizens more safety, robust healthcare and healthy lifestyles. However, when GDP reaches a point of diminishing returns as seen with countries like the United States and China, it cannot be reasonably said that this growth is in service of increasing life expectancy. Realistically, further GDP growth beyond this threshold leads to other political benefits in the interests of those nations. Those other political benefits may indeed be critical to a country's public health or economic well-being. But this data reveals that after a certain point, life expectancy at birth is decidedly not a significant benefit of continued GDP growth.