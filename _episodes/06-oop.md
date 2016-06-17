---
title: "Object-Oriented Programming"
teaching: 0
exercises: 0
questions:
- "How can I make more programs easier to extend?"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---

* We can represent a 2D array as a list of lists
  * Index with `a[i][j]` instead of `a[i, j]`

* How does the performance compare to that of a NumPy array?
  * Could write some synthetic benchmarks
  * But want to experiment with it in the real application...
  * ...*without* rewriting every array access

* Root problem is that our verbs are tied tightly to our nouns
  * Object-oriented programming solves this (and several other problems)

* A *class* defines a new kind of thing
  * Things of that kind have parts (member variables) and behaviors (methods)

* An *object* is a particular concrete thing
  * Every object belongs to a class, which tells us what it has and how it behaves
  * Reality is more complex, but we'll go with this for now...

~~~
class Counter(object):

    def __init__(self):
        self.value = 0

    def get(self):
        return self.value

    def change(self):
        self.value += 1
~~~
{: .python}

* The details
  * `__init__` is called automatically when we're creating a new instance of the class
  * `self` is *this particular object* inside the method
  * Member variables created by assignment (as usual) using dot notation

~~~
left = Counter()
left.change()
left.change()
print('left after two changes:', left.get())

right = Counter()
right.change()
print('right after one changes:', right.get())
~~~
{: .python}

~~~
left after two changes: 2
right after one change: 1
~~~
{: .output}

* Why bother?

~~~
class Wrapper(object):

    def __init__(self, limit):
        self.limit = limit
        self.value = 0

    def get(self):
        return self.value

    def change(self):
        self.value = (self.value + 1) % self.limit

wrapper = Wrapper(3)
for i in range(10):
    print('loop:', i, 'value:', wrapper.get())
    wrapper.change()
~~~
{: .python}

~~~
loop: 0 value: 0
loop: 1 value: 1
loop: 2 value: 2
loop: 3 value: 0
loop: 4 value: 1
loop: 5 value: 2
loop: 6 value: 0
loop: 7 value: 1
loop: 8 value: 2
loop: 9 value: 0
~~~
{: .output}

* OK, but why bother?

~~~
def count_n(stepper, number):
    for n in range(number):
        stepper.change()

counter = Counter()
count_n(stepper, 10)
print('final value of counter is:', counter.get())

wrapper = Wrapper(3)
count_n(wrapper, 10)
print('final value of wrapper is:', counter.get())
~~~
{: .python}

~~~
final value of counter is: 10
final value of wrapper is: 1
~~~
{: .output}

* It's easy to make new code use old code (just call it)
* Object-oriented programming means *old code can use new code*
  * New objects have the same interface as the old ones
  * Calling code only uses that interface
  * *Polymorphism*

~~~
class ListArray(object):

    def __init__(self, N):
        self.array = []
        for i in range(N):
            self.array.append([0] * N)

    def get(self, x, y):
        return self.array[x][y]

    def set(self, x, y, val):
        self.array[x][y] = val


class NumPyArray(object):

    def __init__(self, N):
        self.array = np.zeros((N, N))

    def get(self, x, y):
        return self.array[x, y]

    def set(self, x, y, val):
        self.array[x, y] = val
~~~
{: .python}

* Still have to rewrite the existing code to use `.get` and `.set`
  * But won't have to in future if we change array implementation again

* But wait!
  * We can teach our new array to use square bracket subscripts
  * The expression `a[i]` is implemented by calling `a.__getitem__(i)`
  * And `a[i] = val` is `a.__setitem__(i, val)`

~~~
class ListArray(object):

    def __init__(self, N):
        self.array = []
        for i in range(N):
            self.array.append([0] * N)

    def __getitem__(self, loc):
        x, y = loc[0], loc[1]
        return self.array[x][y]

    def set(self, x, y, val):
        x, y = loc[0], loc[1]
        self.array[x][y] = val
~~~
{: .python}

* Get rid of `NumpyArray`

* Modify main driver to take a string specifying how to create the array
  * And *nothing else changes*
