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

## What is a data frame? 


## Loading tabular data with pandas
temperature_data = pd.read_csv("filename")

## Spend a few minutes reviewing your data 
It is normally a good idea to ensure your data frame loaded correctly. Thankfully, Pandas has a few built in methods to help - shape, .head(), .tail(), and .describe(). The shape method will return a tuple that has the number of rows in the first position and the number of columns in the second position. In our example our data frame has 135 rows and 3 columns. Methods .head() and .tail() return the first 5 rows and the last 5 rows respectively. Finally, .describe() will return a variety of things depending on the data type. For numeric data types, like our example, it includes count, mean, standard deviation, minimum, quartiles, and the maximum. For object types it will return count, unique, most common, and frequency of the most common. Additionally, timestamps will also include the first and last item. 

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

temperature_data[""] or temperature_data.""


## Aggregate operations 
.sum() 
.mean()
.std()
.min()
.max()
.count()


## indexing 
.set_index()
.loc()
.iloc()
.ix()

## Exercises

*   Analyze temperature statistics.
