---
title: "Programming Style"
teaching: 5
exercises: 10
questions:
- "How can I make programs more robust?"
- "How can I make programs easier to understand?"
objectives:
- "Add `assert` statements to programs to check pre-conditions, post-conditions, and invariants."
keypoints:
- "Fail early, often, and meaningfully."
- "Use `assert` to check that programs are working correctly."
- "Give `assert` statements meaningful error messages to help users."
---
## Follow standard Python style in your code.

*   [PEP8](https://www.python.org/dev/peps/pep-0008) is a style guide for Python.
*   The [PEP8 application and Python library](https://pypi.python.org/pypi/pep8)
    checks code for compliance.

## Use assertions to check for internal errors.

*   `assert condition, 'message'` halts with an error message if the condition isn't true.
    *   Pre-condition: must be true in order for this function to run.
    *   Post-condition: guaranteed true at the end of this function.
    *   Invariant: guaranteed true at this point in the program (typically in a loop).
*   Proportions vary widely, but 10-20% of production code is there to check the other 80-90%.
    *   "Fail early, fail often, fail loudly."

~~~
def bounds(values):
    assert len(values) > 0, 'Cannot get bounds of empty list.'
    low = min(values)
    high = max(values)
    assert low <= high, 'Low bound should not be greater than high bound'
    return low, high
~~~
{: .python}

## Use docstrings to provide online help.

*   If the first thing in a function is a character string
    that is not assigned to a variable,
    Python attaches it to the function as the online help.

~~~
def average(values):
    "Return average of values, or None if no values are supplied."

    if len(values) == 0:
        return None
    return sum(values) / average(values)

help(average)
~~~
{: .python}
~~~
Help on function average in module __main__:

average(values)
    Return average of values, or None if no values are supplied.
~~~
{: .output}

> ## Multiline Strings
>
> Often use *multiline strings* for documentation.
> These start and end with three quote characters (either single or double)
> and end with three matching characters.
>
> ~~~
> """This string spans multiple lines.
>
> Blank lines are allowed. For documentation, typically a first line
> summarizes the functionality, and a blank line separates that summary
> from the remainder. The ending three quote characters, in the case of a
> long documentation string, are typically on their own line.
> """
> ~~~
> {: .python}
{: .callout}

> ## Document This
>
> Turn the comment on the following function into a docstring
> and check that `help` displays it properly.
>
> ~~~
> def middle(a, b, c):
>     # Return the middle value of three.
>     # Assumes the values can actually be compared.
>     values = [a, b, c]
>     values.sort()
>     return values[1]
> ~~~
> {: .source}
{: .challenge}

> ## Clean Up This Code
>
> 1. Read this short program and try to predict what it does.
> 2. Run it: how accurate was your prediction?
> 3. Refactor the program to make it more readable.
>    Add assertions as you go to make sure you're not breaking things,
>    and run it after each change to test it.
> 4. Compare your rewrite with your neighbor's.
>    What did you do the same?
>    What did you do differently, and why?
>
> ~~~
> n = 10
> s = 'et cetera'
> print(s)
> i = 0
> while i < n:
>     # print('at', j)
>     new = ''
>     for j in range(len(s)):
>         left = j-1
>         right = (j+1)%len(s)
>         if s[left]==s[right]: new += '-'
>         else: new += '*'
>     s=''.join(new)
>     print(s)
>     i += 1
> ~~~
> {: .source}
{: .challenge}
