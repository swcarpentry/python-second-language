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

Before we load our csv into a data frame, we need to import the [Pandas library](http://pandas.pydata.org/). A common alias for Pandas is `pd` and we will use that for our examples. 

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

It is a good idea to ensure your dataframe loaded correctly. Thankfully, Pandas has a few built in methods to help - [shape](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.shape.html?highlight=shape#pandas.DataFrame.shape), [.head()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html), [.tail()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.tail.html), and [.describe()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html). The shape method will return a tuple that has the number of rows in the first position and the number of columns in the second position. Methods .head() and .tail() return the first 5 rows and the last 5 rows respectively. Finally, .describe() will return a variety of things depending on the data type. For numeric data types, like our example, it includes count, mean, standard deviation, minimum, quartiles, and the maximum. For other object types it will return count, unique, most common, and frequency of the most common. Additionally, timestamps will also include the first and last item. 

~~~
print("The shape of our data frame", temperature_data.shape)
print("\n The head of our data frame \n", temperature_data.head())
print("\n The tail of our data frame \n", temperature_data.tail())
print("\n A quick description of our data frame\n", temperature_data.describe())
~~~
{: .python}
~~~
The shape of our dataframe: (135, 3)

 The head of our dataframe: 
    Year  Annual_Mean  5-year_Mean
0  1880        -0.23          NaN
1  1881        -0.15          NaN
2  1882        -0.18        -0.21
3  1883        -0.21        -0.22
4  1884        -0.29        -0.24

 The tail of our dataframe: 
      Year  Annual_Mean  5-year_Mean
130  2010         0.66         0.57
131  2011         0.55         0.59
132  2012         0.57         0.61
133  2013         0.60          NaN
134  2014         0.67          NaN

 A quick description of our dataframe: 
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

Pandas offers two [different ways](http://pandas.pydata.org/pandas-docs/stable/indexing.html#basics) to access data in a column. These syntactically similar ways can have their respective benefits. However, to help with readability it is generally a good idea to use the same method throughout your code.

Before we start selecting individual columns, let's take a look at our column labels using columns.

~~~
temperature_data.columns
~~~
{: .python}
~~~
Index(['Year', 'Annual_Mean', '5-year_Mean'], dtype='object')
~~~
{: .output}

We can also look at our indexes with something very similar.

~~~
temperature_data.index
~~~
{: .python}
~~~
Int64Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
            ...
            125, 126, 127, 128, 129, 130, 131, 132, 133, 134],
           dtype='int64', length=135)
~~~
{: .output} 

While not particularly useful in this example, there are cases when knowing the indexes can be very valuable.

Now that we know our indexes and columns we can start exploring our data a bit more. Let's take a look at the years in our dataframe.

~~~
temperature_data["Year"]
~~~
{: .python}
~~~
0      1880
1      1881
2      1882
3      1883
4      1884
       ... 
130    2010
131    2011
132    2012
133    2013
134    2014
Name: Year, dtype: int64
~~~
{: .output :}


We can also use the following syntax. 

~~~
temperature_data.Year
~~~
{: .python}
~~~
0      1880
1      1881
2      1882
3      1883
4      1884
       ... 
130    2010
131    2011
132    2012
133    2013
134    2014
Name: Year, dtype: int64
~~~
{: .output :}

While both techniques are valid, for this lesson we are going to use the temperature_data["Year"] syntax. 

## Aggregate operations

There are a number of aggregate operations that can be very useful for doing some quick analysis and verification of your dataset. They are [.count()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.count.html#pandas.DataFrame.count), [.max()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.max.html#pandas.DataFrame.max), [.min()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.min.html#pandas.DataFrame.min), [.std()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.std.html#pandas.DataFrame.std), [.mean()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.mean.html#pandas.DataFrame.mean), and [.sum()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sum.html#pandas.DataFrame.sum). These functions works as one might anticipate.

Let's count the number of values in our year column.

~~~
temperature_data["Year"].count()
~~~
{: .python}
~~~
135
~~~
{: .output}

Let's look for the max and min year.

~~~
print(temperature_data["Year"].max())
print(temperature_data["Year"].min())
~~~
{: .python}
~~~
2014
1880
~~~
{: .output}

Next the standard deviation, mean, and sum.

~~~
print(temperature_data["Annual_Mean"].std())
print(temperature_data["Annual_Mean"].mean())
print(temperature_data["Annual_Mean"].sum())
~~~
{: .python}
~~~
0.300638292778
-0.00955555555556
-1.29
~~~
{: .output} 

While this might not be the most interesting data analysis, these examples do show the methods functionality and use. 

## Indexing 

Pandas supports some nice [indexing and slicing](http://pandas.pydata.org/pandas-docs/stable/indexing.html) features for dataframes that are common to Python generally.

For example if you wanted to look at the first five years of data.

~~~
temperature_data[:5]
~~~
{: .python}
~~~
   Year  Annual_Mean  5-year_Mean
0  1880        -0.23          NaN
1  1881        -0.15          NaN
2  1882        -0.18        -0.21
3  1883        -0.21        -0.22
4  1884        -0.29        -0.24
~~~
{: .output} 

Or the last five years.

~~~
temperature_data[-5:]
~~~
{: .python}
~~~
     Year  Annual_Mean  5-year_Mean
130  2010         0.66         0.57
131  2011         0.55         0.59
132  2012         0.57         0.61
133  2013         0.60          NaN
134  2014         0.67          NaN
~~~
{: .output}

You can even do your own odd mix.

~~~
temperature_data[34:58]
~~~
{: .python} 
~~~
    Year  Annual_Mean  5-year_Mean
34  1914        -0.24        -0.32
35  1915        -0.17        -0.33
36  1916        -0.37        -0.31
37  1917        -0.45        -0.32
38  1918        -0.32        -0.34
39  1919        -0.30        -0.31
40  1920        -0.28        -0.28
41  1921        -0.21        -0.27
42  1922        -0.30        -0.26
43  1923        -0.27        -0.25
44  1924        -0.25        -0.23
45  1925        -0.23        -0.21
46  1926        -0.11        -0.19
47  1927        -0.20        -0.20
48  1928        -0.17        -0.18
49  1929        -0.32        -0.18
50  1930        -0.13        -0.16
51  1931        -0.08        -0.18
52  1932        -0.11        -0.13
53  1933        -0.26        -0.14
54  1934        -0.10        -0.15
55  1935        -0.16        -0.12
56  1936        -0.11        -0.06
57  1937         0.03        -0.04
~~~
{: .output} 

Properly using indexes can help you select data and analysis in a faster, slightly more logical way. Remember the results from our command temperature_data.index? It was a list of numbers from 0-134. It would be nice if our years were actually our index labels. That would help us select data, say from 1882-1892 fairly easily (without having to think about the zero-index location for those years).

To change our index we can use the [.set_index](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index) method. 

~~~
temperature_data_idx = temperature_data.set_index("Year")
~~~
{: .python}

Now let's look at our indexes in our new dataframe, temperature_data_idx.

~~~
temperature_data_idx.index
~~~
{: .python}
~~~
Int64Index([1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889,
            ...
            2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
           dtype='int64', name='Year', length=135)
~~~
{: .output}

A quick note about why we had to create a new dataframe. Many dataframe methods are not done "in place." Which means if you run the method on the dataframe it won't change your original dataframe unless you set it to a new dataframe. We could have set the ```set_index``` option to ```True``` or we could have set the dataframe to itself by using the same ```temperature_data``` but we wanted to take a second to use this as a learning opportunity. 

With our newly indexed dataframe we can access slices of data by the our index labels using [.loc](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html#pandas.DataFrame.loc) and [.ix](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.ix.html#pandas.DataFrame.ix). This is an improvement to having to know the index number (and with [.iloc](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc) we haven't lost our ability to access our data via the index number). This all probably sounding a bit confusing, so let's look at each method and some examples.

.loc is a label-based index selector. Here label-based is probably best understood as a string or text, instead of an index location. That means with our newly indexed dataframe we can quickly access data by year.

~~~
temperature_data_idx.loc[1889:1903]
~~~
{: .python}
~~~
      Annual_Mean  5-year_Mean
Year                          
1889        -0.11        -0.25
1890        -0.34        -0.25
1891        -0.27        -0.28
1892        -0.32        -0.32
1893        -0.36        -0.31
1894        -0.33        -0.29
1895        -0.26        -0.27
1896        -0.19        -0.26
1897        -0.19        -0.23
1898        -0.32        -0.21
1899        -0.21        -0.22
1900        -0.16        -0.24
1901        -0.21        -0.25
1902        -0.31        -0.30
1903        -0.37        -0.33
~~~
{: .output} 

We can also select specific columns. 

~~~
temperature_data_idx.loc[1889:1903, "Annual_Mean"]
~~~
{: .python}
~~~
Year
1889   -0.11
1890   -0.34
1891   -0.27
1892   -0.32
1893   -0.36
1894   -0.33
1895   -0.26
1896   -0.19
1897   -0.19
1898   -0.32
1899   -0.21
1900   -0.16
1901   -0.21
1902   -0.31
1903   -0.37
Name: Annual_Mean, dtype: float64
~~~
{: .output} 

And we can add on our aggregate methods too.

~~~
temperature_data_idx.loc[1889:1903, "Annual_Mean"].std()
~~~
{: .python}
~~~
0.080326713815398632
~~~
{: .output}

We can also use .iloc if we want slice data by index location (zero-based). For example if we wanted to look at the last 10 years in our data set.

~~~
temperature_data_idx.iloc[-10:]
~~~
{: .python}
~~~
      Annual_Mean  5-year_Mean
Year                          
2005         0.65         0.59
2006         0.59         0.57
2007         0.62         0.59
2008         0.49         0.59
2009         0.59         0.58
2010         0.66         0.57
2011         0.55         0.59
2012         0.57         0.61
2013         0.60          NaN
2014         0.67          NaN
~~~
{: .output} 

We can also select columns and add aggregate methods too. However, because we are selecting based on index location we will have to refer to our columns by their zero-indexed location too.

~~~
temperature_data_idx.iloc[-10:, 1].mean()
~~~
{: .python}
~~~
0.58624999999999994
~~~
{: .output} 

Quick question, which column do you think we selected? 

Lastly there is .ix. .ix is mix of .loc and .iloc - that is it first looks for a label-based selector and then checks for an integer location.

~~~
temperature_data_idx.ix[1921:1937]
~~~
{: .python}
~~~
      Annual_Mean  5-year_Mean
Year                          
1921        -0.21        -0.27
1922        -0.30        -0.26
1923        -0.27        -0.25
1924        -0.25        -0.23
1925        -0.23        -0.21
1926        -0.11        -0.19
1927        -0.20        -0.20
1928        -0.17        -0.18
1929        -0.32        -0.18
1930        -0.13        -0.16
1931        -0.08        -0.18
1932        -0.11        -0.13
1933        -0.26        -0.14
1934        -0.10        -0.15
1935        -0.16        -0.12
1936        -0.11        -0.06
1937         0.03        -0.04
~~~
{: .output} 

Now to show .ix index selection ability.

~~~
temperature_data_idx.ix[7:12]
~~~
{: .python}
~~~
Empty DataFrame
Columns: [Annual_Mean, 5-year_Mean]
Index: []
~~~
{: .output}

That's odd, an empty dataframe? In a fun gotcha, when an index is integer based, like our current example, label based access is only supported for .ix because it is difficult for python to know if you're trying to access your data via the label or the integer location. Our empty dataframe is because we don't have any data for years 7 through 12. But, there is a workaround for our situation (using our previous dataframe). Which, reminds us to remember that if we obtain a result or an error that we didn't anticipate it is always best to [read the documentation!](http://pandas.pydata.org/pandas-docs/stable/index.html) : ) 

~~~
temperature_data.ix[0:5]
~~~
{: .python}
~~~
   Year  Annual_Mean  5-year_Mean
0  1880        -0.23          NaN
1  1881        -0.15          NaN
2  1882        -0.18        -0.21
3  1883        -0.21        -0.22
4  1884        -0.29        -0.24
5  1885        -0.27        -0.27
~~~
{: .output}


## Exercises

*   Analyze temperature statistics.
