---
title: "Pandas - Introduction"
teaching: 35
exercises: 10
questions:
- "How can I manage tabular data in python?"
objectives:
- "Learners will understand how to read csv data into a Pandas DataFrame"
- "Learners will understand how to manipulate and access data in a DataFrame"
- "Learners will understand how to deal with missing and null data by dropping and using backfilling methods"
keypoints:
- "Pandas DataFrames can be used to read and write tabular data in csv format in python"
- "data in DataFrames are accessed using indices (row names) and (columns)"
- "Series and DataFrames can be concatenated using pd.concat"
- "Null data can be dropped or backfilled using DataFrame.dropna and DataFrame.fillna"
---

This module draws heavily from and modifies [Introduction to Pandas][fonnesbeck-pandas] by Chris Fonnesbeck,
which is licensed under the [Creative Commons Attribution 4.0 International License][cc-by].

# Pandas

~~~
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use("ggplot")
import pandas as pd
import numpy as np
from IPython.display import display
~~~
{: .python}

## Data structures


~~~
# Series, indexes
concs = pd.Series([1.1, 2.3, 1.2, 3.5],)
concs.values
concs.index

# Explicit indices
concs = pd.Series([1.1, 2.3, 1.2, 3.5],
                  index = ["CO2", "CH4", "NO2", "O3"])

# Accessing elements of series
concs.CO2 # attribute
concs['CH4'] # key
["O" in formula for formula in concs.index] # looping
concs[0] # positional indexing

# Naming the indices, the values
concs.name = "concentrations (ppb)"
concs.index.name = "compound"

# Numpy-like behavior
concs[0:2]
concs + concs
np.log(concs)
concs[concs > 2]

# Are these the same?  Think about how to ask this.
slice1 = concs["CO2":"NO2"]
slice2 = concs[0:2]
# Inclusive endpoints when slicing using indices

# Construction using dictionaries, Note sorting
concs_dict = {"CO2": 1.1, "CH4": 2.3, 
              "NO2": 1.2, "O3": 3.5}
concs = pd.Series(concs_dict)

# Specifying indices, NaN, alignment of dissimilar series
concs2 = pd.Series(concs_dict, index=["CO2", "CH4", "NO2", "H2O"])
concs2.isnull()
concs + concs2
~~~
{: .python}

~~~
CH4    4.6
CO2    2.2
H2O    NaN
NO2    2.4
O3     NaN
dtype: float64
~~~
{: .output}

~~~
# DataFrames - Tabular data structures
atmo = pd.DataFrame({"conc": [1.1, 2.3, 1.2, 3.5],
                     "weight":[44, 16, 46, 48],
                     "formula":["CO2", "CH4", "NO2", "O3"]})

# Indexes, columns
atmo.index # like row labels
atmo.columns

# accessing columns by key, attribute
atmo.weight
atmo['formula']
# diff from series, where index access via attribute/key

# Accessing rows, why are these two things different?
atmo.ix[0]
atmo.ix[0:1]
# Hint, use the type function

atmo.T
atmo.index = atmo.formula
~~~
{: .python}

## Real data


~~~
co2 = pd.read_csv("../data/atmo_CO2.csv")
co2 = pd.read_csv("../data/atmo_CO2.csv", index_col = "Year")

co2 = co2.drop("StanfordCalifornia", axis = 1)
# or
co2 = co2.dropna(axis = 1, how = "all")

#co2.info()
#co2.describe()

#co2.plot(legend = False)
co2.ix[:, co2.columns != "EPICADome"].plot(legend = False)
~~~
{: .python}


<matplotlib.legend.Legend at 0x12a3c43c8>

![png](../fig/pandas_6_1.png)

## Concatenation

~~~
co2.mean(axis=1)
ch4 = pd.read_csv("../data/atmo_CH4.csv", index_col = "Year")
n2o = pd.read_csv("../data/atmo_N2O.csv", index_col = "Year")

# Concat
summary = pd.concat([chem.mean(axis=1) for chem in [co2, ch4, n2o]], axis=1)
summary.columns = ["CO2", "CH4", "N2O"]
summary.plot()
~~~
{: .python}

<matplotlib.axes._subplots.AxesSubplot at 0x134de4b70>

![png](../fig/pandas_8_1.png)

## Fill in Missing Data

~~~
summary = summary.fillna(method = "bfill")
summary.plot()
~~~
{: .python}

<matplotlib.axes._subplots.AxesSubplot at 0x13b3b21d0>

![png](../fig/pandas_10_1.png)

## Writing to File

~~~
summary.to_csv("atmo_summary.csv")
~~~
{: .python}

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[fonnesbeck-pandas]: https://github.com/fonnesbeck/statistical-analysis-python-tutorial
