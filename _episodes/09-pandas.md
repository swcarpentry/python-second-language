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
pd.read_csv("filename")

A quick look at your data frame 
.shape()
.head() 
.tail()
.describe() 

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
