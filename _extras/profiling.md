---
layout: episode
title: "Profiling"
teaching: 15
exercises: 15
questions:
- "Why is my program so slow?"
objectives:
- "Use a profiler to determine where a program is spending its time."
- "Explain the difference between sampling and instrumenting profilers."
keypoints:
- "Get it right, then make it fast."
- "Profile a program's execution by instrumenting or sampling."
- "Look at per-call and cumulative runtime to understand what to tune."
---

## We use computers because they're faster than we are.

*   No matter how fast your computer is, some programs take too long to run.
*   Eventually you become tired of taking tea breaks to fill the time,
    or you need to tackle a problem so large, you cannot imagine it finishing at all.
*   But making a program run more quickly can be daunting:
    the program might be large,
    or might have been written by someone else.
*   Modern computing systems are too complex for us to predict performance reliably.
    1.  Paging (i.e., overflowing physical memory).
    2.  Searching instead of looking up directly.
    3.  Putting low-probability if-statements early in a conditional chain.
    4.  Calling procedures or using complex if-statements inside very large data loops.
    5.  Re-creating variables inside loops.
    6.  Reading and writing from disk or the network.
    7.  Using inefficient objects when an array might be better
*   This is where *profiling* can help.
    *   Shows what part of a program is occupying most of its execution time,
        so you know where to focus your effort.
    *   Shows if changes are actually improvements.

## Get it right, then make it fast.

*   No point getting the wrong answer faster or more often.

## Distinguish per-call time, total time, and cumulative time.

*   Per-call time: how long does each execution take (on average)?
*   Total time: how much time is spent in this function/block in total?
    *   I.e., number of calls times time per call.
*   Cumulative time: how much time is spent in this function/block and the ones it calls?
    *   Top-level program should show 100%.

## Profilers necessarily distort execution (a little).

*   *Sampling*: interrupt every few hundred microseconds and see where we are.
*   *Instrumenting*: record entry/exit times for functions, blocks, etc.
*   Both change the execution characteristics of the program.
    *   But so does measuring voltage or temperature...

> ## Installing a Profiler
>
> The `line_profiler` module is not installed as part of the base Anaconda Python installation.
> You will need to use the `conda` package manager to install it:
>
> ~~~
> $ conda install line_profiler
> ~~~
> {: .bash}
>
> If you are using a different Python distribution,
> the `line_profiler` package can be installed through `pip`:
>
> ~~~
> pip install line_profiler
> ~~~
> {: .bash}
{: .challenge}

## Use a decorator to show which parts of the code you want to profile.

*   Add a *decorator* before each function you want the profiler to measure.
    *   Tells Python to modify the function after it's defined.
*   Example: finding prime numbers.

~~~
def primes(n):
    if n==2:
        return [2]
    elif n<2:
        return []

    s=list(range(3,n+1,2))
    mroot = n ** 0.5
    half=(n+1)//2-1
    i=0
    m=3

    while m <= mroot:
        if s[i]:
            j=(m*m-3)//2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

primes(100)
~~~
{: .python}

*   Add the `@profile` decorator before the function definition:

~~~
@profile
def primes(n):
    ...as before...
~~~
{: .python}

> ## Take a Guess
>
> Before going to the next step,
> try to guess where this code is going to spend most of its time.
> Which lines take longest to run individually and cumulatively?
{: .callout}

## Use `kernprof` to run from the command line and collect profile data.

*   `kernprof -l -v primes.py` runs Python with extra options to collect and record data.
*   `kernprof` is the profiler script
*   `-l`: recognise the `@profile` decorator and profile your code.
*   `-v`: display timing information when the script has finished running.

~~~
Wrote profile results to primes.py.lprof
Timer unit: 1e-06 s

Total time: 0.000245 s
File: primes.py
Function: primes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           @profile
     2                                           def primes(n):
     3         1            8      8.0      3.3      if n==2:
     4                                                   return [2]
     5         1            2      2.0      0.8      elif n<2:
     6                                                   return []
     7
     8         1           11     11.0      4.5      s=range(3,n+1,2)
     9         1           36     36.0     14.7      mroot = n ** 0.5
    10         1            2      2.0      0.8      half=(n+1)/2-1
    11         1            1      1.0      0.4      i=0
    12         1            1      1.0      0.4      m=3
    13
    14         5            8      1.6      3.3      while m <= mroot:
    15         4            4      1.0      1.6          if s[i]:
    16         3            4      1.3      1.6              j=(m*m-3)/2
    17         3            4      1.3      1.6              s[j]=0
    18        31           33      1.1     13.5              while j<half:
    19        28           31      1.1     12.7                  s[j]=0
    20        28           30      1.1     12.2                  j+=m
    21         4            4      1.0      1.6          i=i+1
    22         4            5      1.2      2.0          m=2*i+3
    23        50           61      1.2     24.9      return [2]+[x for x in s if x]
~~~
{: .python}

## Change and test one thing at a time.

*   Many things might improve the performance of the program.
*   E.g., line 9 calculates square root of `n` using built-in exponentiation.
*   This line of code consumes a significant proportion of CPU time.
*   What happens if we use `math.sqrt` instead?

> ## Try It
>
> Replace the square root computation with `math.sqrt`
> and compare the results from the previous profiler run.
{: .challenge}

> ## Calculating Pi
>
> 1.  Write a program that calculates π using some approximation.
> 2.  Profile it.
> 3.  Try to make it faster.
>
> An example python script is given in `profiling_pi.py`.
{: .challenge}

## Profiling within IPython
> ## Loading line_profiler
> `line_profiler` has to be loaded into the IPython/Jupyter notebook by running:
>
> ~~~
> `%load_ext line_profiler`
> ~~~
> {: .source}
{: .prereq}


There are multiple ways to profile code within the IPython terminal depending how detailed you want to be
These magic commands also work in Jupyter Notebooks

* `%time` - time how long a statement takes to run
~~~
%time primes(100)
~~~
{: .python}
~~~
CPU times: user 21 µs, sys: 6 µs, total: 27 µs
Wall time: 23.8 µs
~~~
{: .output}

* `%timeit` - average time how long a cell takes to run over multiple runs
~~~
%timeit primes(100)
~~~
{: .python}
~~~
100000 loops, best of 3: 8.11 µs per loop
~~~
{: .output}
*  `%prun`  - time each function in a script
~~~
%prun primes(100)
~~~
{: .python}
~~~
        4 function calls in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <ipython-input-26-4a302b84e1ce>:1(primes)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
~~~
{: .output}
*  `%lprun` - time each line in a function to run
~~~
%lprun -f primes primes(100)
~~~
{: .python}
* `%lprun -f func1 -f func2 ....... <statement>` to profile multiple functions
~~~
Timer unit: 1e-06 s

Total time: 0.000122 s
File: <ipython-input-26-4a302b84e1ce>
Function: primes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def primes(n):
     2         1            2      2.0      1.6      if n==2:
     3                                                   return [2]
     4         1            1      1.0      0.8      elif n<2:
     5                                                   return []
     6                                           
     7         1            4      4.0      3.3      s=range(3,n+1,2)
     8         1            2      2.0      1.6      mroot = n ** 0.5
     9         1            1      1.0      0.8      half=(n+1)//2-1
    10         1            0      0.0      0.0      i=0
    11         1            0      0.0      0.0      m=3
    12                                           
    13         5            4      0.8      3.3      while m <= mroot:
    14         4            2      0.5      1.6          if s[i]:
    15         3            3      1.0      2.5              j=(m*m-3)/2
    16         3            4      1.3      3.3              s[j]=0
    17        31           20      0.6     16.4              while j<half:
    18        28           23      0.8     18.9                  s[j]=0
    19        28           19      0.7     15.6                  j+=m
    20         4            1      0.2      0.8          i=i+1
    21         4            2      0.5      1.6          m=2*i+3
    22        50           34      0.7     27.9      return [2]+[x for x in s if x]
~~~
{: .output}


* Check the documentation by running the command with an `?` at the end for additional options
~~~
%lprun?
~~~
{: .python}
