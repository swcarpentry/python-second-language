---
title: "Plotting"
teaching: 15
exercises: 15
questions:
- "How can I plot my results?"
objectives:
- "Create a time series plot of statistical data."
- "Create a scatter plot of statistical data."
keypoints:
- "Use matplotlib with arrays or data frames to visualize data."
- "Decide what kind of plot to create based on what questions you want to answer."
---
## Plotting in Python

*   [Matplotlib][matplotlib] is the most popular plotting library for Python
*   While Matplotlib is not part of Python's standard libraries, it is  incorporated in [Continuum Anaconda's Python distribution][anaconda].

## Creating and viewing plot in Jupyter notebook

To enable visualization of plots within a Jupyter notebook, a line magic command `%matplotlib inline` must be called at the beginning of the notebook. Next, the *matplotlib* library must first be loaded.

~~~
%matplotlib inline
import matplotlib.pyplot as plt
~~~
{: .python}

To create a plot, the minimum requirement is to provide the data to be visualized as argument to the `plot` function.

~~~
dataValues = [1,2,3,5,7,11]
plt.plot(dataValues)
plt.show()
~~~
{: .python}

By default, a single data sequence is interpreted as the y-values for the plot, and the indices of the series are used as the x-values. The x-values can also be specified by adding an additional data sequence to the `plot` function.

~~~
dataValues = [1,2,3,5,7,11]
dataIndex = [0.2,0.4,0.6,0.8,1,1.2]
plt.plot(dataIndex, dataValues)
plt.show()
~~~
{: .python}

> ## Order of data variables in the `plot` function
>
> What is the shape of the plot when the positions of dataIndex and dataValues are switched in the `plt.plot` function call?
{: .challenge}

A plot can be enhanced by providing additional information about plot title and x and y-axis labels.

~~~
dataValues = [1,2,3,5,7,11]
dataIndex = [0.2,0.4,0.6,0.8,1,1.2]
plt.plot(dataIndex, dataValues)
plt.title('First Plot')
plt.ylabel('data values')
plt.xlabel('data indices')
plt.show()
~~~
{: .python}

## plotting time series data

A time series is a sequence of data points describing a specific attribute over time. Data points of time series are indexed in an ordered manner and often taken at successive equally spaced points in time. Examples include daily stock prices, monthly rainfall measurements, or yearly national GDP.

Time series are often as *csv* files. They can be loaded via the `pandas` library into a DataFrame object.

~~~
import pandas as pd
daily_prices = pd.read_csv("../data/goog.csv")
print (daily_prices)
~~~
{: .python}

In plotting time series data, we want to demonstrate how measured values of a specific attribute changes over time. As time indices are typically recorded as a date string, the most straightforward approach is to plot the measured values against the y-axis and the ordered indices of these values against the x-axis, and to use the time indices as the label for the ticks on x-axis. It is possible to pass the columns of a `DataFrame` directly to `matplotlib`

~~~
plt.plot(daily_prices["Open"])
plt.title('Google stock between 11/01/2016 and 11/22/2016')
plt.ylabel('Opening Price')
plt.xlabel('Date')
plt.xticks(range(0,16), daily_prices["Date"])
plt.show()
~~~
{: .python}

The previous plot is not visually pleasing, as the x-axis ticks are overlaid on
top of one another and not readable. It is possible to rotate the orientation of the x-axis ticks by specifying the `rotation` attribute of `plt.xticks`

~~~
plt.plot(daily_prices["Open"])
plt.title('Google stock between 11/01/2016 and 11/22/2016')
plt.ylabel('Price')
plt.xlabel('Date')
plt.xticks(range(0,16), daily_prices["Date"], rotation='vertical')
plt.show()
~~~
{: .python}

> ## Plotting other pricing metrics
>
> 1. Fill in the blanks so that the plot displays the closing prices of Google stocks.
> 2. Augment the y-axis label so that it clearly displays which pricing metric is being plotted.
> ~~~
> plt.plot(daily_prices[____])
> plt.title('Openning price of Google stock between 11/01/2016 and 11/22/2016')
> plt.ylabel('____')
> plt.xlabel('Date')
> plt.xticks(range(0,16), daily_prices["Date"], rotation='vertical')
> plt.show()
> ~~~
> {: .python}
{: .challenge}

CHANGE GRAPH TYPE TO PLOT SCATTER PLOT

PLOT MULTIPLE SERIES WITH LEGEND BOX

## Exercises

*   Modify plots used in teaching.

[matplotlib]: http://matplotlib.org/
[anaconda]: https://www.continuum.io/downloads
