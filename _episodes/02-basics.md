---
title: "Basics"
teaching: 0
exercises: 0
questions:
- "What are the basic features of Python?"
objectives:
- "Name seven built-in data types in Python and explain their purpose."
- "Name the basic operators on numbers and strings."
- "Explain how and when Python variables are created and typed."
- "Write a `for` loop over a string or list."
- "Write multi-branch conditional statements."
- "Index and slice sequences."
- "Explain what aliasing is and how it occurs."
- "Define a function taking a fixed number of parameters and returning a value."
- "Explain and identify the scope of local variables in functions."
- "Read lines from a text file."
keypoints:
- "Python's basic data types include `None`, Booleans, integers, float, strings, lists, and files."
- "Python's basic operators include the usual numeric operators, string concatenation and multiplication, and the usual Boolean operators."
- "Python variables are created by assignment, and are untyped."
- "`for` loops iterate through the values in a collection."
- "Conditionals are written using `if`, `elif`, and `else`."
- "Sequences (strings and lists) are indexed from 0, and may be sliced with double indices."
- "Negative indices count backward from the end of the sequence."
- "Lists may contain references to other data (including other lists)."
- "Functions are defined using `def`, and may take any number of parameters."
- "Functions return `None` unless `return` is used to explicitly return a value."
- "Variables created inside a function are local to that function."
- "Files are opened with the built-in `open` function, and closed with the `.close` method."
- "Looping over a file object returns one line of the file per iteration."
- "Use the `with` statement to avoid forgetting to close files."
- "Write docstrings for functions so that interactive help will work for them."
---
* Data
  * Basic data types are:
    * Integers
    * Floating-point numbers (floats)
    * Booleans
    * `None`
    * Character strings
      * In Python 3, these are always Unicode
      * There's a primitive `bytes` type for single-byte data
  * Basic arithmetic works as you'd expect
    * 5/2 is 2.5, not 2
    * 5//2 (double slash) is integer division
  * Strings can be concatenated with `+` and multiplied with `*`
  * Strings can *not* be modified in place: they are *immutable*

* Variables and Assignment
  * Python is a *dynamic* language: variables are created whenever something is assigned to a name
  * They don't have types --- they're just sticky notes attached to values
  * Can erase a variable with `del x`

* The `for` loop gives you each item from a collection in turn
  * Items not indices
  * Loop variable created if necessary and persists after the loop
  * Body must be indented
    * Convention is 4 spaces

~~~
for ch in "gold":
    print(3*ch)
~~~
{: .source}

* Conditionals are written using `if`, `elif`, and `else`
  * `if` and `elif` must have conditions
    * Cannot do assignment in those conditions
  * Body indented
  * At most one branch is executed
* Conditions can:
  * Use the usual comparisons
  * Be combined with `and`, `or`, and `not`
  * Use the `in` operator

~~~
for ch in "gold":
    if ch in 'aeiou':
        print(ch, 'is a vowel')
    elif ch <= 'm':
        print(ch, 'is in the first half of the alphabet')
    else:
        print(ch, 'is just an ordinary letter')
~~~
{: .source}

* A list is a mutable sequence of heterogeneous values
  * Mutable: can be modified
  * Sequence: can be indexed
  * Heterogeneous: can hold values of any type
    * But usually store values of a single type
* Index from 0
  * Because [IBM executives were into yacht racing in the 1960s](http://exple.tive.org/blarg/2013/10/22/citation-needed/)
* Negative indices count backward from the end
* Can also *slice* with `[start:end]`
  * Half-open: includes lower index, does *not* include upper
  * So `a[:i]` + `a[i:]` is the whole sequence
* Note that slices can be empty

~~~
print("gold"[0])
print("gold"[3])
print("gold"[4])
print("gold"[-1])
print("gold"[-4])
print("gold"[1:3])
print("gold"[:3])
print("gold"[1:])
~~~
{: .source}

* Lists can contain lists
  * But what we really mean is that lists contain *references* to other lists
  * *Aliasing*

~~~
first = [1, 2]
second = [first, first]
print(second)
first.append(3)
print(second)
~~~
{: .source}

* Define a function with
  * `def`
  * the function's name
  * a parenthesized list of parameters
  * an indented body
* Every function returns something
  * Return value is `None` if nothing else is explicitly returned using `return`

~~~
def closest(values, target):
    result = values[0]
    for v in values[1:]:
        if abs(v - target) < abs(result - target):
            result = v
    return result

print(closest([1, 2, 3], 9))
print(closest([1, 2, 3], -9))
~~~
{: .source}

* Variables `result` and `v` are *local*
  * Only exist while the function is executing
  * Not visible outside

* File I/O modeled on C
  * Built-in function `open(filename, mode)`
    * `mode` is `'r'` (for read), `'w'` (for write), or `'a'` (for append)
  * Returns an object (that can be used in `print` statements)
  * Can also use this object as the subject of a for loop
    * Each iteration gets the next line from the file
  * Then close the file with `file.close()`

~~~
reader = open('data.txt', 'r')
num = 0
for line in reader:
    num = num + 1
reader.close()
print('number of lines', num)
~~~
{: .source}

* Two idioms:
  * The `with` block
  * In-place operators

~~~
with open('data.txt', 'r') as reader:
    num = 0
    for line in reader:
        num += 1
print('number of lines', num)
~~~
{: .source}

* And speaking of idioms:

~~~
def closest(values, target):
    '''Return the closest value to the target in the given list of values.'''

    result = values[0]
    for v in values[1:]:
        if abs(v - target) < abs(result - target):
            result = v
    return result

help(closest)
~~~
{: .source}
