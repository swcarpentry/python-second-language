---
layout: page
title: "Lesson Design"
permalink: /design/
---

## Contents
{:.no_toc}

* Jekyll will replace this line with an auto-generated table of contents.
{:toc}

## Process Used

This lesson was developed using a slimmed-down variant of the "Understanding by Design" process.
The main sections are:

1.  Assumptions about audience, time, etc.

2.  Desired results:
    *   Overall goals
    *   Summative assessments at half-day granularity
    *   What learners will be able to do, what they will know, etc.

3.  Learning plan
    *   Each episode has a heading that summarizes what will be covered,
        then estimates time that will be spent on teaching and on exercises.
    *   The exercises are outlined to make expectations concrete.

## Stage 1 - Assumptions

*   Audience
    *   Graduate students and research software engineers in numerate disciplines from cosmology to economics
    *   Who can write procedural code in a dynamic language such as Perl or MATLAB
        *   Largely self-taught
        *   Variables and assignment, loops, lists or arrays, conditionals, simple functions
        *   May or may not have done object-oriented programming
        *   Familiar with basic Unix shell commands (cd, ls, rm) and concepts (home directory, path)
    *   But have not programmed in Python before (or if they have, they've only dabbled)
*   Constraints
    *   One full day 09:00-16:00
        *   06:30 teaching time
        *   1:00 for lunch
        *   0:30 total for two coffee breaks
    *   Learners use native installs on their own machines
        *   May connect to a cloud resource at their own discretion, but they have to set it up
    *   Assume knowledge of the Unix shell but *not* of version control
    *   Use the Jupyter Notebook
        *   Authentic tool
        *   There isn't really an alternative
        *   And means that even people who have seen a bit of Python before will probably learn something
*   Exercises will mostly *not* be "write this code from scratch"
    *   Want lots of short exercises that can reliably be finished in allotted time
    *   So use MCQs, fill-in-the-blanks, Parsons Problems, "tweak this code", etc.
*   Running Examples
    *   Morning: invasion percolation
    *   Afternoon: data analysis

## Stage 2 - Desired Results

### Essential Questions

How do I...

*   ...express common operations (loops, conditionals, aggregate data structures) in Python?
*   ...break a program into functions?
*   ...write unit tests for Python programs?
*   ...use data structures make programs simpler and more efficient?
*   ...work with matrices?
*   ...analyze tabular data?
*   ...get data from the web?

### Concepts

Learners will know that...

*   ...Python is a dynamic imperative language.
*   ...dictionaries can make programs simpler and more efficient at the same time.
*   ...unit tests are easy to express and run using supporting libraries.
*   ...matrices can be manipulated using MATLAB-style methods.
*   ...tabular data can be manipulated using structures like R's data frames.
*   ...fetching data from the web is not much more complicated than reading from local files.

### Summative Assessment

*   Mid-point: sort files in a directory into groups by size
*   Final: Download and process data set from the web

### Skills

Learners can:

1.  ...run code interactively in the Jupyter Notebook.
2.  ...run code saved in a file from the Unix shell.
3.  ...create, index, and slice lists.
4.  ...create and index dictionaries.
5.  ...call built-in functions.
6.  ...use `help` and online documentation.
7.  ...import code from libraries.
8.  ...read tabular data into data frames.
9.  ...do collective operations on data frames.
10. ...create simple plots of data in data frames.
11. ...interpret common error messages.
12. ...create and run unit tests.
13. ...write functions with default parameter values.
14. ...download data from the web programmatically.

## Stage 3 - Learning Plan

### Basics (09:00)

*   Teaching: 15 min
    *   `int`, `float`, `str`, `bool`, `list`
*   Exercises: 10 min
    *   Immutable strings vs. mutable lists
    *   Subscript games

### Basic Control Flow (09:25)

*   Teaching: 10 min
    *   `for`
    *   `if`/`else`
    *   basic list and string methods
*   Exercises: 10 min
    *   Acronymize

### File I/O (09:45)

*   Teaching: 5 min
    *   `open` and `close`
    *   `for line in file`
*   Exercises: 10 min
    *   Count non-blank lines

### Libraries (10:00)

*   Teaching: 10 min
    *   `import`
    *   dot notation
    *   `math` and `random`
    *   `range`
*   Exercises: 10 min
    *   Calculate average of sequence of random values

### Coffee (10:20)

*   Break: 15 min

### Writing Functions (10:35)

*   Teaching: 10 min
    *   Basic definition
    *   Default values for parameters
    *   Scope rules
*   Exercises: 10 min
    *   Nested function calls
    *   Aliasing of lists

### Defensive Programming (10:55)

*   Teaching: 5 min
    *   The idea of `assert`
*   Exercises: 10 min
    *   Add a few assertions to some functions

### Profiling (11:30)

*   Teaching: 10 min
    *   Sampling vs. instrumenting
*   Exercises: 10 min
    *   Profile two versions of invasion percolation
    *   One uses dictionaries, which haven't yet been introduced...

### Dictionaries (11:10)

*   Teaching: 10 min
    *   Basic operations
    *   Need for immutable keys
    *   Tuples
*   Exercises: 10 min
    *   Sort files in a directory into groups by size

### Summary (11:50): 10 min

### Lunch (12:00)

*   Break: 60 min

### Pandas (13:00)

*   Teaching: 20 min
    *   Data frames
    *   Reading CSV files
    *   Aggregate operations
    *   Indexing
*   Exercises: 15 min
    *   Statistics on GDP

### Plotting (13:35)

*   Teaching: 10 min
    *   Basic line plots
    *   Basic scatter plots
*   Exercises: 10 min
    *   Modify plots
    *   Add extra lines

### Command-Line Programming (13:55)

*   Teaching: 10 min
    *   `sys.argv`
    *   `sys.stdin` and `sys.stdout`
*   Exercises: 15 min
    *   Turn invasion percolation into a command-line application

### Coffee (14:20)

*   Coffee: 15 min

### Testing (14:35)

*   Teaching: 10 min
    *   `py.test`
*   Exercises: 15 min
    *   Add tests to invasion percolation

### Getting Data From the Web (15:00)

*   Teaching: 15 min
    *   The `requests` library
    *   The `json` library
    *   The `csv` library
*   Exercises: 15 min
    *   Pull down another data set

### Next Steps (15:30)

*   Teaching: 20 min
    *   NumPy arrays
    *   The SciPy ecosystem
*   Exercises: 0 min
    *   Because they'll be tired

### Summary (15:50): 10 min
