## Profiling your code in Python

### Instructional design thoughts:
* Do we need to explain why code might run slowly (example)?
* Is it worth explaining that getting the algorithm right first might be a better approack (example)?
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

#### What impact can I expect on my code?
 * Running a profiler will have an effect on the code- it usually slows it down

 * Once I have run the profiler, I get some information that might help me understand where it is spending its time

  
