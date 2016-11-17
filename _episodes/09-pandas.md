---
title: "Pandas"
teaching: 20
exercises: 20
questions:
- "How can I do statistical analysis of tabular data?"
objectives:
- "Load tabular data with Pandas to create a data frame."
- "Do statistical analysis on data stored in a data frame."
keypoints:
- "Use Pandas data frames to store tabular data for statistical analysis."
- "Data frame operations make (most) loops unnecessary."
---

## What is a dataframe? 

A dataframe is conceptually similar to a spreadsheet. It is two dimensional with columns and rows. Columns have labels, similar to the first row of a spreadsheet, for accessing content and similarly rows are indexed by number. Dataframes can be very powerful and are great for data exploration and analysis. 

## Loading tabular data with pandas

Before we load our csv into a data frame, we need to import the Pandas library. A common alias for Pandas is `pd` and we will use that for our examples. 

~~~
import pandas as pd
~~~
{: .python}

To load your csv into a Pandas data frame, you can use the .read_csv() method. [.read_csv](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) has a lot of potential parameters but for example we will simply pass .read_csv() the file name, which is located in the same folder as our Jupyter Notebook. 

~~~
temperature_data = pd.read_csv("temperature.csv") 
~~~
{: .python}

## Spend a few minutes reviewing your data 

It is a good idea to ensure your data frame loaded correctly. Thankfully, Pandas has a few built in methods to help - shape, .head(), .tail(), and .describe(). The shape method will return a tuple that has the number of rows in the first position and the number of columns in the second position. In our example our data frame has 135 rows and 3 columns. Methods .head() and .tail() return the first 5 rows and the last 5 rows respectively. Finally, .describe() will return a variety of things depending on the data type. For numeric data types, like our example, it includes count, mean, standard deviation, minimum, quartiles, and the maximum. For object types it will return count, unique, most common, and frequency of the most common. Additionally, timestamps will also include the first and last item. 

~~~
print("The shape of our data frame", temperature_data.shape)
print("\n The head of our data frame \n", temperature_data.head())
print("\n The tail of our data frame \n", temperature_data.tail())
print("\n A quick description of our data frame\n", temperature_data.describe())
~~~
{: .python}
~~~
The shape of our data frame: (135, 3)

 The head of our data frame: 
    Year  Annual_Mean  5-year_Mean
0  1880        -0.23          NaN
1  1881        -0.15          NaN
2  1882        -0.18        -0.21
3  1883        -0.21        -0.22
4  1884        -0.29        -0.24

 The tail of our data frame: 
      Year  Annual_Mean  5-year_Mean
130  2010         0.66         0.57
131  2011         0.55         0.59
132  2012         0.57         0.61
133  2013         0.60          NaN
134  2014         0.67          NaN

 A quick description of our data frame:
               Year  Annual_Mean  5-year_Mean
count   135.000000   135.000000   131.000000
mean   1947.000000    -0.009556    -0.015649
std      39.115214     0.300638     0.284251
min    1880.000000    -0.480000    -0.450000
25%    1913.500000    -0.235000    -0.250000
50%    1947.000000    -0.070000    -0.050000
75%    1980.500000     0.135000     0.145000
max    2014.000000     0.670000     0.610000
~~~
{: .output}

## Referencing Columns  

Pandas offers two different ways to access data in a column. These syntactically similar ways can have their respective benefits. However, to help with readability it is generally a good idea to use the same method throughout your code.

Before we start selecting individual columns, let's take a look at our column labels. 

~~~
temperature_data.columns
~~~
{: .python}
~~~

We can also look at our indexes with something very similar

~~~
temperature_data.index
~~~
{: .python}

While not particularly useful in this example, there are cases when knowing the indexes can be very valuable.

Now that we know our indexes and columns we can start exploring our data a bit more. Let's take a look at the years in our dataframe.

~~~
temperature_data["Year"]
~~~
{: .python}

We can also use this syntax

~~~
temperature_data.Year
~~~
{: .python}

While both techniques are valid, for this lesson I'm going to use the temperature_data["Year"] syntax. 

## Aggregate operations

There are a number of aggregate operations that can be very useful for doing some quick analysis and verification of your dataset. They are .count(), .max(), .min(), .std(), .mean(), and .sum(). These functions works as one might anticipate.

~~~
# Let's count the number of values in our year column
temperature_data["Year"].count()
~~~
{: .python}

~~~
# The max and min year 
print(temperature_data["Year"].max())
print(temperature_data["Year"].min())
~~~
{: .python}

~~~
# The standard deviation, mean, and sum
print(temperature_data["Annual_Mean"].std())
print(temperature_data["Annual_Mean"].mean())
print(temperature_data["Annual_Mean"].sum())
~~~
{: .python}

While this might not be the most interesting data analysis, these examples do show the methods functionality and use. 

## Indexing 

Pandas supports some nice slicing features for dataframes that are common to Python generally.

For example if you wanted to look at the first five years of data

~~~
temperature_data[:5]
~~~
{: .python}

Or the last five years

~~~
temperature_data[-5:]
~~~
{: .python}

or some mix

~~~
temperature_data[34:58]
~~~
{: .python} 


Properly using indexes can help you select data and analysis in a faster, slightly more logical way. Remember the results from our command temperature_data.index? It was a list of numbers from 0-134. It would be nice if our years were actually our index labels? That would help us select data, say from 1882-1892 fairly easily (without having to think about the zero-index location for those years).

To change our index we can use the .set_index method. 

~~~
temperature_data_idx = temperature_data.set_index("Year")
~~~
{: .python}

With our newly indexed dataframe we can access slices of data by the our index labels using .loc and .ix. This is an improvement to having to know the index number (and with .iloc we haven't lost our ability to access our data via the index number). This all probably sounding a bit confusing, so let's look at each method and some examples.

.loc is a label-based index selector. Here label-based is probably best understood as a string or text, instead of an index location. That means with our newly indexed dataframe we can quickly access data by year.

~~~
temperature_data_idx.loc[1889:1921]
~~~
{: .python}

We can also select specific columns if we are interested 

~~~
temperature_data_idx.loc[1889:1921, "Annual_Mean"]
~~~
{: .python}

And we can add on our aggregate methods too.

~~~
temperature_data_idx.loc[1889:1921, "Annual_Mean"].std()
~~~
{: .python} 

We can also use .iloc if we want slice data by index location (zero-based). For example if we wanted to look at the last 10 years in our data set.

~~~
temperature_data_idx.iloc[-10:]
~~~
{: .python}

Again we can select columns and add aggregate methods too. However, because we are selecting based on index location we will have to refer to our columns by their zero-indexed location.

~~~
temperature_data_idx.iloc[-10:, 1].mean()
~~~
{: .python}

Lastly there is .ix. .ix is mix of .loc and .iloc - that is it first looks for a label-based selector and then checks for an integer location.

~~~
temperature_data_idx.ix[1921:1937]
~~~
{: .python}

However, in a fun gotcha, when an index is integer based, like our current example, label based access is only supported for .ix because it is difficult for python to know if you're trying to access your data via the label or the integer location. But, there is a workaround for our situation (using our previous dataframe for our example). 

~~~
temperature_data.ix[0:5]
~~~
{: .python}


## Exercises

*   Analyze temperature statistics.
