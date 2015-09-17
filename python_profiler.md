## Profiling your code in Python

### Instructional design thoughts:
* Do we need to explain why code might run slowly (example)?
* Is it worth explaining that getting the algorithm right first might be a better approach (example)?
* This lesson will work best if students already modularise their code

### Getting ready
The `line_profiler` module is not installed as part of the base Anaconda Python installation. You will need to use the conda package manager to install this onto your computers.

At the command prompt, enter:

`conda install line_profiler`

If you are using a different Python distribution, the `line_profiler` package can be installed through `pip`:

`pip install line_profiler`

### Learning objectives
* Why do I need to profile my code?
* What impact can I expect on my code?
* How do I use `line_profiler`?
* How do I interpret the results?
* How can I use these results to make my code run faster?

#### Why do I need to profile my code?

No matter how fast your computer is, some programs take too long to run. Eventually you become tired of taking tea breaks to fill the time; or you need to tackle a problem so large, you cannot imagine it finishing at all.

Making a program run more quickly can be daunting: the program might be large; it might have been written by someone else, or in a language you are unfamiliar with.

This is where profiling can help.

It shows what part of a program is occupying most of its execution time, directing you to where you need to focus attention and gain insight on how it might be done better. You can try out different ways of doing the same thing and measure how much faster or slower they are.

Just as importantly, profiling shows you what you do NOT need to execute more quickly. Optimising for speed takes effort to do and easily results in hard to read code that is difficult to understand or change. For that reason, it is important not to optimise code that does not need to be optimised.

_Could we do some simple timing examples here?_

#### What impact can I expect on my code?
* Running a profiler will have an effect on the code- it usually slows it down
* Once I have run the profiler, I get some information that might help me understand where it is spending its time

#### How do I use `line_profiler` ?
After you have installed the `line_profiler` module, to use it you need to add a decorator before each function you want the profiler to measure (_do we need to explain what a decorator is?_ ).

Let's take a simple example, a script to calculate the first `n` prime numbers (this is saved as `primes.py`):

``` python
 def primes(n):
     if n==2:
         return [2]
     elif n<2:
         return []

     s=range(3,n+1,2)
     mroot = n ** 0.5
     half=(n+1)//2-1
     i=0
     m=3

     while m <= mroot:
         if s[i]:
             j=(m*m-3)/2
             s[j]=0
             while j<half:
                 s[j]=0
                 j+=m
         i=i+1
         m=2*i+3
     return [2]+[x for x in s if x]

 primes(100)
 ```

To profile the `primes` function, we need to add the `@profile` decorator before the function:

``` python
@profile
def primes (n):
    ...
```

This tells the profiler to profile this function. If you have multiple functions in your script then add the `@profile` decorator in front of each of them.

Save the file (as `primes.py`)

So before we run the profiler, let's take a look at the code and see where we think it is going to spend it's time.
* On what lines will this script spend most of its time?
* What about cumulatively?

To profile this `primes.py` script we now need to run the profiler and tell it to profile our decorated code.

`kernprof -l -v primes.py`

Here:
`kernprof` is the profiler script
The `-l` argument tells the profiler to recognise the `@profile` decorator and profile your code.
The `-v` argument tells the profiler to display timing information when the script has finished running.

If we do this, we should get an output on screeen that looks something like this:

```
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
```
#### Post-class assessment
1. Please write two programs that each use a different method for calculating pi (this could involve extra research), OR write one program that uses two methods.
2. Profile each method
3. Determine a metric for efficiency
4. Determine which method for pi is the most efficient in your example.

An example python script is given in `profiling_pi.py`
