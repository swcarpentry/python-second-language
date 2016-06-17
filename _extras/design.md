---
layout: page
title: "Lesson Design"
permalink: /design/
---

## Process Used

This lesson was designed using the process described in the [Python gapminder lesson][gapminder].

## Stage 0 - Assumptions

*   Audience
    *   Graduate students and research software engineers in numerate disciplines from cosmology to economics
    *   Who can write procedural code in a dynamic language such as Perl or MATLAB
        *   Largely self-taught
        *   Variables and assignment, loops, lists or arrays, conditionals, simple functions
        *   May or may not have done object-oriented programming
        *   Familiar with basic Unix shell commands (cd, ls, rm) and concepts (home directory, path)
    *   But have not programmed in Python before (or if they have, they've only dabbled)
*   Constraints
    *   One full day 09:00-16:00 (05:30 teaching time, 1:00 lunch, 0:30 for two coffee breaks)
    *   Learners use native installs on their own machines
        *   May connect to a cloud resource at their own discretion, but they have to set it up
    *   No dependence on other Carpentry modules
        *   In particular, must not require knowledge of version control
    *   Use the Jupyter Notebook
        *   Authentic tool
        *   There isn't really an alternative
        *   And means that even people who have seen a bit of Python before will probably learn something
*   Examples
    *   Use [ipythonblocks][blocks] and invasion percolation to recapitulate basics (loops, conditionals, functions)
    *   Write unit tests for invasion percolation
    *   Use [turtle graphics][turtle] to illustrate object-oriented programming
        *   Right now, that means running from the command line...
    *   FIXME: how to motivate NumPy?
    *   FIXME: how to motivate Pandas?
    *   Use CSV data from the web to motivate web programming
        *   <http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv>
*   Exercises will mostly *not* be "write this code from scratch"
    *   Want lots of short exercises that can reliably be finished in allotted time
    *   So use MCQs, fill-in-the-blanks, Parsons Problems, "tweak this code", etc.
*   Lesson materials
    *   Notes for instructors and self-study will be written in Markdown
        *   We've tried writing/maintaining lessons as Notebooks...
    *   Learners will be provided with one Notebook per episode containing starting points for exercises

## Stage 1 - Desired Results

### Goals (Summative Assessment)

*   Basics: variables, for loops, conditionals, lists, functions, line I/O
    *   Modify invasion percolation step by step
*   Testing
    *   Unit tests for invasion percolation
*   Dictionaries (and JSON data)
    *   Make invasion percolation more efficient
*   Single-inheritance classes with method overrides
    *   Visualize a simple N-body simulation
*   NumPy
    *   Image manipulation (?)
*   Pandas
    *   Analyze CSV data
*   The `requests` library for fetching data (but not authentication)
    *   FIXME

### Essential Questions

How do I...

*   ...read, analyze, and visualize a tabular data set?
*   ...check and process multiple data sets?
*   ...break a program into functions?
*   ...break a program into classes?
*   ...check that it's working correctly?

### Learners Will Be Able To...

*   Run code saved in a file from the Unix shell
*   Run code interactively in the Jupyter Notebook
*   Create, index, and slice lists
*   Create and index dictionaries
*   Call built-in functions
*   Use `help` and online documentation
*   Import code from libraries
*   Read tabular data into arrays or data frames
*   Do collective operations on arrays and data frames
*   Create simple plots of data in arrays and data frames
*   Interpret common error messages
*   Create unit tests for discrete (integer) problems
*   Write non-recursive functions taking a variable number of named parameters
*   Download data from the web via URLs
*   Create single-inheritance class hierarchies with method overriding

## Stage 2 - Learning Plan

FIXME: break it down into learning chunks

[blocks]: http://ipythonblocks.org/
[gapminder]: https://swcarpentry.github.io/python-novice-gapminder/
[turtle]: https://docs.python.org/3.5/library/turtle.html
