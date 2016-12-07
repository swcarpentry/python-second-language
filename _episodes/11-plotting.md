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

## creating scatter plot

Sometimes, a line plot creates an artificial connection among data points that might influence the visual perception. A scatter plot is a type of plot that simply visualizes the individual data point and lets viewers identify the potential connections by themselves. A scatter plot can be created by calling the `scatter` function.

~~~
plt.scatter(range(0,16), daily_prices["Open"])
plt.title('Google stock between 11/01/2016 and 11/22/2016')
plt.ylabel('Price')
plt.xlabel('Date')
plt.xticks(range(0,16), daily_prices["Date"], rotation='vertical')
plt.show()
~~~
{: .python}

As a scatter plot visualize individual data points on a graph, two arguments with equal length are needed to represents the x-coordinates and y-coordinates of the collection of points, respectively.

## plotting multiple datasets

With multiple data sets plotted on the same graph, different visual characteristics are needed for different sets, and legends that associate these visual cues with data sets' identities are also needed.

In the example below, a graph comparing opening and closing prices of Google stock on the same day does provide any meaningful information without the differentiating visual characteristics

~~~
plt.scatter(range(0,16), daily_prices["Open"])
plt.scatter(range(0,16), daily_prices["Close"])
plt.title('Google stock between 11/01/2016 and 11/22/2016')
plt.ylabel('Price')
plt.xlabel('Date')
plt.xticks(range(0,16), daily_prices["Date"], rotation='vertical')
plt.show()
~~~
{: .python}

By specifying the coloring scheme of different data sets, we have a better visual of the data. However, someone without the source code still cannot distinguish between the opening and closing prices (although they can clearly observe two separate data sets)

~~~
plt.scatter(range(0,16), daily_prices["Open"], color="red")
plt.scatter(range(0,16), daily_prices["Close"], color="blue")
plt.title('Google stock between 11/01/2016 and 11/22/2016')
plt.ylabel('Price')
plt.xlabel('Date')
plt.xticks(range(0,16), daily_prices["Date"], rotation='vertical')
plt.show()
~~~
{: .python}

By adding `label` and `legend`, we can now distinguish between the data sets, but the default settings for `legend` and the placement of the legend box are not visually pleasing.

~~~
plt.scatter(range(0,16), daily_prices["Open"], color="red", label="Open")
plt.scatter(range(0,16), daily_prices["Close"], color="blue", label="Close")
plt.title('Google stock between 11/01/2016 and 11/22/2016')
plt.ylabel('Price')
plt.xlabel('Date')
plt.xticks(range(0,16), daily_prices["Date"], rotation='vertical')
plt.legend(loc='upper right')
plt.show()
~~~
{: .python}

Additional modifications to the arguments of the `legend` function call can be made to improve the quality of the plot. More specifically, we move the location of the legend box to the upper left corner of the graph and only use one scatter point in representing the legends.

~~~
plt.scatter(range(0,16), daily_prices["Open"], color="red", label="Open")
plt.scatter(range(0,16), daily_prices["Close"], color="blue", label="Close")
plt.title('Google stock between 11/01/2016 and 11/22/2016')
plt.ylabel('Price')
plt.xlabel('Date')
plt.xticks(range(0,16), daily_prices["Date"], rotation='vertical')
plt.legend(loc='upper left', scatterpoints = 1)
plt.show()
~~~
{: .python}

## Exercises

*   Modify plots used in teaching.

[matplotlib]: http://matplotlib.org/
[anaconda]: https://www.continuum.io/downloads
