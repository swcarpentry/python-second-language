---
title: "Dictionaries"
teaching: 15
exercises: 15
questions:
- "How can I store and manipulate non-rectangular data?"
objectives:
- "Write programs that use sets to store unique values."
- "Write programs that use dictionaries to store key/value pairs."
- "Identify values that can and cannot be used as dictionary keys."
keypoints:
- "Use sets to store unique unordered values."
- "Use dictionaries to store extra information with those values."
---

## Use a set to store unique values.

*   Create with `{...}`
    *   But must use `set()` to create an empty set.

~~~
primes = {2, 3, 5, 7}
print('is 3 prime?', 3 in primes)
print('is 9 prime?', 9 in primes)
~~~
{: .python}
~~~
is 3 prime? True
is 9 prime? False
~~~
{: .output}

*   Intersection,  union, etc.

~~~
odds = {3, 5, 7, 9}
print('intersection', odds & primes)
print('union', odds | primes)
~~~
{: .python}
~~~
intersection {3, 5, 7}
union {3, 5, 7, 9, 11}
~~~
{: .output}

## Sets are mutable.

*   But only store *unique* values.

~~~
primes.add(11)
print('primes becomes', primes)
primes.discard(7)
print('after removal', primes)
primes.add(11)
print('after adding 11 again', primes)
~~~
{: .python}
~~~
primes becomes {11, 2, 3, 5, 7}
after removal {11, 2, 3, 5}
after adding 11 again {11, 2, 3, 5}
~~~
{: .output}

## Sets are unordered.

*   Values are stored by *hashing*.
    *   Which is intentionally as random as possible.

~~~
names = {'Darwin', 'Newton', 'Turing'}
for n in names:
    print(n)
~~~
{: .python}
~~~
Newton
Darwin
Turing
~~~
{: .output}

## Use a dictionary to store key/value pairs.

*   Equivalently, to store extra information with elements of a set.

~~~
birthdays = {'Newton' : 1602, 'Darwin' : 1809}
print(birthdays['Newton'])
birthdays['Turing'] = 1612 # oops
birthdays['Turing'] = 1912 # that's better
print(birthdays)
~~~
{: .python}
~~~
1602
{'Darwin': 1809, 'Newton': 1602, 'Turing': 1912}
~~~
{: .output}

*   Just an accident that keys are alphabetical in this case.
    *   Like sets, dictionaries store keys by hashing, which is as random as possible.

## Set values and dictionary keys must be immutable.

*   Changing them after insertion would leave data in the wrong place.
*   Use a *tuple* for multi-valued keys.

~~~
people = {('Isaac', 'Newton'): 1602, ('Charles', 'Darwin'): 1809}
~~~
{: .python}

## Example: create a histogram.

~~~
numbers = [1, 0, 1, 2, 0, 0, 1, 2, 1, 3, 1, 0, 2]
count = {}
for n in numbers:
    if n not in count:
        count[n] = 1
    else:
        count[n] = count[n] + 1
print(count)
~~~
{: .python}
~~~
{0: 4, 1: 5, 2: 3, 3: 1}
~~~
{: .output}

## Keys are often strings.

~~~
elements = {'H' : 1, 'He' : 2, 'Li' : 3, 'Be' : 4, 'B' : 5}
print('atomic number of lithium:', elements['Li'])
~~~
{: .python}
~~~
atomic number of lithium: 3
~~~
{: .output}

> ## How Heavy Is This Molecule?
>
> Write a function that takes two parameters:
> a dictionary mapping atomic symbols to atomic weights,
> and a list of (atom, count) pairs for a molecule,
> and returns that molecule's molecular weight.
>
> ~~~
> weights = {'H' : 1.0079, 'C' : 12.0107, 'N' : 14.0067,
>            'O' : 15.9994, 'P' : 30.9738, 'S' : 32.065}
>
> methane = [('C', 1), ('H', 4)]
> print('methane', mol_weight(weights, methane))
>
> aminothiazole = [('C', 3), ('H', 4), ('N', 2), ('S', 1)]
> print('aminothiazole', mol_weight(weights, aminothiazole))
> ~~~
> {: .python}
> ~~~
> methane 16.0423
> aminothiazole 100.1421
> ~~~
> {: .output}
>
> How did you test your function?
{: .challenge}
