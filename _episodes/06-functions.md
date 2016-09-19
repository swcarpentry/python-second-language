---
title: "Writing Functions"
teaching: 10
exercises: 10
questions:
- "How can I make code more readable?"
- "How can I make code reusable?"
objectives:
- "Write a function taking a fixed number of parameters and having a single point of return."
- "Write functions whose parameters have default values."
- "Write functions with multiple points of return."
- "Write functions that return multiple values."
- "Extract functions from longer programs."
- "Trace the execution of nested non-recursive function calls."
- "Correctly identify the scope of variables."
keypoints:
- "Use `def` to define a new function."
- "Give parameters default values to make use easier and intent clearer."
- "Use `*args` to handle variable-length parameter lists."
- "Use `return` at any point to return values."
- "Turn repeated or deeply-nested pieces of code into functions."
- "Functions temporarily store values on a call stack."
---
## Break programs down into functions.

*   Readability: human beings can only keep a few items in working memory at a time.
    *   *Encapsulate* complexity so that we can treat it as a single "thing".
*   Reuse: write one time, use many times.
*   Testing: components with well-defined boundaries are easier to test.

## Define a function using `def` with a name, parameters, and a block of code.

*   Function name must obey the same rules as variable names.
*   Put *parameters* in parentheses.
    *   Empty parentheses if the function doesn't take any inputs.
*   Then a colon and an indented block of code.

~~~
def print_greeting():
    print('Hello!')
~~~
{: .python}

## Arguments in call are matched to parameters in definition.

~~~
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)
~~~
{: .python}
~~~
1871/3/19
~~~
{: .output}

## Functions may return a result to their caller using `return`.

*   May occur anywhere in the function.
*   But functions are easier to understand if `return` occurs:
    *   At the start to handle special cases.
    *   At the very end, with a final result.
*   Functions without explicit `return` produce `None`.

~~~
def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)
~~~
{: .python}

~~~
a = average([1, 3, 4])
print('average of actual values:', a)
~~~
{: .python}
~~~
2.6666666666666665
~~~
{: .output}

~~~
print('average of empty list:', average([]))
~~~
{: .python}
~~~
None
~~~
{: .output}

~~~
result = print_date(1871, 3, 19)
print('result of call is:', result)
~~~
{: .python}
~~~
1871/3/19
result of call is: None
~~~
{: .output}

## Can specify default values for parameters.

*   All parameters with defaults must come *after* all parameters without.
    *   Argument-to-parameter matching would be ambiguous otherwise.
*   Makes common cases simpler, and signals intent.

~~~
def sum(values, scale=1.0):
    result = 0.0
    for v in values:
        result += v * scale
    return result

print('sum with default:', sum([1, 2, 3]))
print('sum with factor:', sum([1, 2, 3], 0.5))
~~~
~~~
sum with default: 6.0
sum with factor: 3.0
~~~
{: .output}

## Can pass parameters by name.

*   Helpful when functions have lots of options.

~~~
print('out of order:', sum(scale=0.25, values=[1, 2, 3]))
~~~
{: .python}
~~~
out of order: 1.5
~~~
{: .output}

## Functions can take a variable number of arguments.

*   Prefix at most one parameter's name with `*`.
    *   By convention, everyone calls the parameters `args`.
*   All "extra" parameters are put in a list-like structure assigned to that parameter.
    *   We'll explain what "list-like" means in more detail later.

~~~
def total(scale, *args):
    result = 0.0
    for a in args:
        result += a * scale
    return result

print('with one value:', total(0.5, 1))
print('with two values:', total(0.5, 1, 3))
~~~
{: .python}
~~~
with one value: 0.5
with two values: 2.0
~~~
{: .output}

## Functions can return multiple values.

*   This is just a special case of many-to-many assignment.

~~~
red, green, blue = 10, 50, 180

def order(a, b):
    if a < b:
        return a, b
    else:
        return b, a

low, high = order(10, 5)
print('order(10, 5):', low, high)
~~~
{: .python}
~~~
order(10, 5): 5 10
~~~
{: .output}

> ## Encapsulation
>
> Fill in the blanks to create a function that takes a single filename as an argument,
> loads the data in the file named by the argument,
> and returns the minimum value in that data.
>
> ~~~
> import pandas
>
> def min_in_data(____):
>     data = ____
>     return ____
> ~~~
> {: .source}
{: .challenge}

> ## Find the First
>
> Fill in the blanks to create a function that takes a list of numbers as an argument
> and returns the first negative value in the list.
> What does your function do if the list is empty?
>
> ~~~
> def first_negative(values):
>     for v in ____:
>         if ____:
>             return ____
> ~~~
> {: .python}
{: .challenge}

> ## Running Sum
>
> Write a function that calculates the running sum of any number of input arguments,
> returning the result as a list.
> For example:
>
> * `running(1, 2)` => `[1, 3]`
> * `running(-5, 2, 7)` => `[-5, -3, 4]`
>
> What should `running()` return, and why?
{: .challenge}

> ## Extracting Functions
>
> People often create functions
> by extracting pieces of code from scripts they've written.
> Re-write the short program below to have one or more functions
> so that no single piece of code is more than ten lines long.
> Do you find the result easier to understand?
>
> ~~~
> # Report the number of lines in each chapter in a text file.
> # A chapter heading has '##' in the first two columns.
> # Blank lines are *not* counted in totals.
>
> reader = open('thesis.txt', 'r')
> current_title = None
> current_count = None
> for line in reader:
>     line = line.strip()
>     if not line:
>         pass
>     elif line.startswith('##'):
>         if current_title is None:
>             current_title = line
> 	    current_count = 0
>         else:
>             print(current_title, current_count)
>             current_title = line
>             current_count = 0
>     else:
>         current_count = current_count + 1
>
> if current_title is not None:
>     print(current_title, current_count)
> ~~~
> {: .python}
{: .challenge}
