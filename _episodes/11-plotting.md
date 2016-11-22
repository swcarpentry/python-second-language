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

To enable visualization of plots within a Jupyter notebook, a line magic command *%matplotlib inline* must be called at the beginning of the notebook. Next, the *matplotlib* library must first be loaded.

~~~
%matplotlib inline
import matplotlib.pyplot as plt
~~~
{: .python}









## Exercises

*   Modify plots used in teaching.

[matplotlib]: http://matplotlib.org/
[anaconda]: https://www.continuum.io/downloads
