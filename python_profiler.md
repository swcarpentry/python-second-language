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
_Could we do some simple timing examples here?_

#### What impact can I expect on my code?
 * Running a profiler will have an effect on the code- it usually slows it down

 * Once I have run the profiler, I get some information that might help me understand where it is spending its time

 #### How do I use `line_profiler` ?
 After you have installed the `line_profiler` module, to use it you need to add a decorator before each function you want the profiler to measure (_do we need to explain what a decorator is?_ ).

 Let's take a simple example, a program to calculate the first `n` prime numbers (this is saved as `primes.py`):

```
 def primes(n):
     if n==2:
         return [2]
     elif n<2:
         return []

     s=range(3,n+1,2)
     mroot = n ** 0.5
     half=(n+1)/2-1
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

 ```
 @profile
 def primes (n):
 ...
 ```
 This tells the profiler to profile this function. If you have multiple functions in your program then add the `@profile` decorator in front of each of them.
