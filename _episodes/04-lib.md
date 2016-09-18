---
title: "Libraries"
teaching: 10
exercises: 10
questions:
- "How can I use Python's standard libraries?"
- "Where do I find documentation on Python's standard libraries?"
objectives:
- "Use `import` to load entire libraries and elements of libraries."
- "Use `import` to load libraries under aliases."
- "Use elements of libraries via dot notation."
- "Use the `math` and `random` libraries."
- "Use the `csv` library to read CSV files."
keypoints:
- "Use `import` to load a library."
- "Use dot notation to get library's contents."
- "The `math` library has common mathematical functions."
- "The `random` library produces pseudo-random numbers."
- "The `csv` library can read CSV files correctly."
---
## Most of the power of a programming language is in its libraries.

*   Python's [standard library][stdlib] is installed with it.
*   Many additional libraries are available from [PyPI][pypi] (the Python Package Index).

## A program must import a library in order to use it.

*   Use `import` to load a library into a program's memory.
*   Then refer to things from the library as `library_name.thing_name`.

~~~
import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))
~~~
{: .python}
~~~
pi is 3.141592653589793
cos(pi) is -1.0
~~~
{: .output}

## Use `help` to find out more about a library's contents.

~~~
help(math)
~~~
{: .python}
~~~
Help on module math:

NAME
    math

MODULE REFERENCE
    http://docs.python.org/3.5/library/math

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)

        Return the arc cosine (measured in radians) of x.
⋮ ⋮ ⋮
~~~
{: .output}

## Import specific items from a library to shorten programs.

*   Use `from...import...` to load only specific items from a library.
*   Then refer to them directly without library name as prefix.

~~~
from math import cos, pi

print('cos(pi) is', cos(pi))
~~~
{: .python}
~~~
cos(pi) is -1.0
~~~
{: .output}

## Create an alias for a library when importing it to shorten programs.

*   Use `import...as...` to give a library a short *alias* while importing it.
*   Then refer to items in the library using that shortened name.

~~~
import math as m

print('cos(pi) is', m.cos(m.pi))
~~~
{: .python}
~~~
cos(pi) is -1.0
~~~
{: .output}

*   Commonly used for libraries that are frequently used or have long names.
    *   E.g., `matplotlib` plotting library is often aliased as `mpl`.
*   But can make programs harder to understand,
    since readers must learn your program's aliases.

> ## Exploring the Math Library
>
> 1. What function from the `math` library can you use to calculate a square root
>    *without* using `sqrt`?
> 2. Since the library contains this function, why does `sqrt` exist?
{: .challenge}

> ## Locating the Right Library
>
> You want to select a random character from a string:
> ~~~
> bases = 'ACTTGCTTGAC'
> ~~~
>
> 1. What [standard library][stdlib] would you most expect to help?
> 2. Which function would you select from that library? Are there alternatives?
{: .challenge}

> ## When Is Help Available?
>
> When a colleague of yours types `help(math)`,
> Python reports an error:
>
> ~~~
> NameError: name 'math' is not defined
> ~~~
> {: .error}
>
> What has your colleague forgotten to do?
{: .challenge}

> ## Importing With Aliases
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Rewrite the program so that it uses `import` *without* `as`.
> 3. Which form do you find easier to read?
>
> ~~~
> import math as m
> angle = ____.degrees(____.pi / 2)
> print(____)
> ~~~
> {: .source}
{: .challenge}

> ## Importing Specific Items
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Do you find this easier to read than preceding versions?
> 3. Why *would't* programmers always use this form of `import`?
>
> ~~~
> ____ math import ____, ____
> angle = degrees(pi / 2)
> print(angle)
> ~~~
> {: .source}
{: .challenge}

> ## Checking Random Numbers
>
> Look up the documentation for the `random` library,
> then write a short program that generates
> a large number of samples from the normal distribution
> with mean 0.0 and standard deviation 1.0
> and see how close the sample average comes to 0.0.
{: .challenge}

> ## Reading Comma-Separated Values
>
> Look up the documentation for the `csv` library
> and use it to read a file containing tabular data
> in comma-separated values (CSV) format.
> Why would you use a library like this
> rather than just reading lines and splitting on the commas?
{: .challenge}

[pypi]: https://pypi.python.org/pypi/
[stdlib]: https://docs.python.org/3/library/
