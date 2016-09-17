---
title: "Control Flow"
teaching: 10
exercises: 10
questions:
- "How do I repeat operations?"
- "How do I make decisions?"
- "How do I call built-in functions?"
objectives:
- "Write scripts that use `for` loops to iterate over lists and character strings."
- "Write scripts that use `if`/`elif`/`else` to perform conditional operations."
- "Call built-in functions."
- "Call methods on strings and lists."
- "Use online help to inspect functions' documentation."
- "Use `range` and `for` to iterate over a sequence of numbers."
- "Correctly write programs that use if and else statements and simple Boolean expressions (without logical operators)."
- "Trace the execution of unnested conditionals and conditionals inside loops."
keypoints:
- "Repeat actions for each element in a collection with `for` loops."
- "Use `range` to generate a list of numbers."
- "Use `if`/`elif`/`else` to make choices."
- "Use built-in functions like `len` and `max` to do calculations."
- "Objects like strings and lists have methods that operate on them."
- "Use `if` statements to control whether or not a block of code is executed."
- "Conditionals are often used inside loops."
- "Use `else` to execute a block of code when an `if` condition is *not* true."
- "Use `elif` to specify additional tests."
- "Conditions are tested once, in order."
- "Create a table showing variables' values to trace a program's execution."
---
## A *for loop* executes commands once for each value in a collection.

*   `for` loops give items rather than indices.
    *   Because that's what people usually want.
*   "for each thing in this group, do these operations"

~~~
for number in [2, 3, 5]:
    print(number)
~~~
{: .python}
~~~
2
3
5
~~~
{: output}

## The first line of the `for` loop must end with a colon, and the body must be indented.

*   The colon at the end of the first line signals the start of a block.
*   Python uses indentation rather than `{}` or `begin`/`end` to show *nesting*.
    *   Any consistent indentation is legal, but almost everyone uses four spaces.

~~~
for number in [2, 3, 5]:
print(number)
~~~
{: .python}
~~~
IndentationError: expected an indented block
~~~
{: .error}

*   Indentation is *always* meaningful in Python.

## Use `range` to iterate over a sequence of numbers.

*   The built-in function `range` produces a sequence of numbers.
    *   *Not* a list: the numbers are produced on demand
        to make looping over large ranges more efficient.
*   `range(N)` is the numbers 0..N-1

~~~
print('a range is not a list: range(0, 3)')
for number in range(0,3):
    print(number)
~~~
{: .python}
~~~
a range is not a list: range(0, 3)
0
1
2
~~~
{: .output}

## Use `if` statements to control whether or not a block of code is executed.

*   Structure is similar to a `for` statement.

~~~
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if mass > 3.0:
        print(mass, 'is large')
~~~
{: .python}
~~~
3.54 is large
9.22 is large
~~~
{: .output}

## Use `else` to execute a block of code when an `if` condition is *not* true.

~~~
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if mass > 3.0:
        print(mass, 'is large')
    else:
        print(mass, 'is small')
~~~
{: .python}
~~~
3.54 is large
2.07 is small
9.22 is large
1.86 is small
1.71 is small
~~~
{: .output}

## Use `elif` to specify additional tests.

~~~
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if mass > 9.0:
        print(mass, 'is HUGE')
    elif mass > 3.0:
        print(mass, 'is large')
    else:
        print(mass, 'is small')
~~~
{: .python}
~~~
3.54 is large
2.07 is small
9.22 is HUGE
1.86 is small
1.71 is small
~~~
{: .output}

> ## Compound Relations Using `and`, `or`, and Parentheses
>
> Often, you want some combination of things to be true.  You can combine
> relations within a conditional using `and` and `or`.  Continuing the example
> above, suppose you have
>
> ~~~
> mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
> velocity = [10.00, 20.00, 30.00, 25.00, 20.00]
>
> i = 0
> for i in range(5):
>     if mass[i] > 5 and velocity[i] > 20:
>         print "Fast heavy object.  Duck!"
>     elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
>         print "Normal traffic"
>     elif mass[i] <= 2 and velocity <= 20:
>         print "Slow light object.  Ignore it"
>     else:
>         print "Whoa!  Something is up with the data.  Check it"
> ~~~
> {: .python}
>
> Just like with arithmetic, you can and should use parentheses whenever there
> is possible ambiguity.  A good general rule is to *always* use parentheses
> when mixing `and` and `or` in the same condition.  That is, instead of:
>
> ~~~
> if mass[i] <= 2 or mass[i] >= 5 and velocity[i] > 20:
> ~~~
> {: .python}
>
> write one of these:
>
> ~~~
> if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20:
> if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20):
> ~~~
> {: .python}
>
> so it is perfectly clear to a reader (and to Python) what you really mean.
{: .callout}

> ## Reversing a String
>
> Fill in the blanks in the program below so that it prints "nit"
> (the reverse of the original character string "tin").
>
> ~~~
> original = "tin"
> result = ____
> for char in original:
>     result = ____
> print(result)
> ~~~
> {: .python}
{: .challenge}

> ## Accumulating
>
> Fill in the blanks in each of the programs below
> to produce the indicated result.
>
> ~~~
> # Total length of the strings in the list: ["red", "green", "blue"] => 12
> total = 0
> for word in ["red", "green", "blue"]:
>     ____ = ____ + len(word)
> print(total)
> ~~~
> {: .python}
>
> ~~~
> # List of word lengths: ["red", "green", "blue"] => [3, 5, 4]
> lengths = ____
> for word in ["red", "green", "blue"]:
>     lengths = lengths.____(____)
> print(lengths)
> ~~~
> {: .python}
>
> ~~~
> # Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
> words = ["red", "green", "blue"]
> result = ____
> for ____ in ____:
>     ____
> print(result)
> ~~~~
> {: .python}
>
> ~~~
> # Create acronym: ["red", "green", "blue"] => "RGB"
> # write the whole thing
> ~~~
> {: .python}
{: .challenge}

> ## Cumulative Sum
>
> Reorder and properly indent the lines of code below
> so that they print an array with the cumulative sum of data.
> The result should be `[1, 3, 5, 10]`.
>
> ~~~
> cumulative += [sum]
> for number in data:
> cumulative = []
> sum += number
> print(cumulative)
> data = [1,2,2,5]
> ~~~
> {: .python}
{: .challenge}

> ## Identifying Variable Name Errors
>
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    What type of `NameError` do you think this is?
>    Is it a string with no quotes, a misspelled variable, or a 
>    variable that should have been defined but was not?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
>
> ~~~
> for number in range(10):
>     # use a if the number is a multiple of 3, otherwise use b
>     if (Number % 3) == 0:
>         message = message + a
>     else:
>         message = message + "b"
> print(message)
> ~~~
> {: .source}
{: .challenge}

> ## While Loops
>
> Python also has a `while` loop
> that keeps going as long as some condition is true:
>
> ~~~
> x = 15
> while x > 0:
>   print(x)
>   x = x - 5
> ~~~
> {: .python}
> ~~~
> 15
> 10
> 5
> ~~~
> {: .output}
>
> Use a `while` loop to print every second character in the string 'fluorine'.
> {: .challenge}

> ## Trimming Values
>
> Fill in the blanks so that this program creates a new list
> containing zeroes where the original list's values were negative
> and ones where the origina list's values were positive.
>
> ~~~
> original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
> result = ____
> for value in original:
>     if ____:
>         result.append(0)
>     else:
>         ____
> print(result)
> ~~~
> {: .source}
>
> ~~~
> [0, 1, 1, 1, 0, 1]
> ~~~
> {: .output}
{: .challenge}

> ## Initializing
>
> Modify this program so that it finds the largest and smallest values in the list
> no matter what the range of values originally is.
>
> ~~~
> values = [...some test data...]
> smallest, largest = None, None
> for v in values:
>     if ____:
>         smallest, largest = v, v
>     ____:
>         smallest = min(____, v)
>         largest = max(____, v)
> print(smallest, largest)
> ~~~
> {: .source}
>
> What are the advantages and disadvantages of using this method
> to find the range of the data?
{: .challenge}
