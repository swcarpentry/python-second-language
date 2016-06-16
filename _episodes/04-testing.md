---
title: "Testing"
teaching: 0
exercises: 0
questions:
- "How can I tell if my program is (probably) working properly?"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---

* Is our program correct?
  * Have half a dozen functions spanning a hundred lines of code (more or less)
  * If there's a 1% chance of a bug in any one line, the odds of the program as a whole being correct are about 36%
  * Worst case is "plausible but wrong"

* Want to test:
  * *Now* to convince ourselves the program is (probably) correct
  * *Repeatedly* to prevent *regression*
  * To show *others* how it actually works (tests as documentation)

* Use `pytest` library to manage *unit tests*
  * Each cell is a test
  * A *setup* cell is run once before each test
    * A *teardown* cell is run once after each test
  * State is thrown away between tests (so they don't contaminate each other)
  * Use *assertions* inside tests to check conditions

* Each test's result can be:
  * pass: worked as expected
  * fail: something's broken in the application
  * error: something's broken in the test itself

* Example
  * The `closest` function from [an earlier episode]({{ site.root }}/02-basics/)
  * What are some useful tests?

~~~
assert closest([], 0) == None, \
    "Meaningless to ask what's closest to an empty set."

assert closest([1], 0) == 1, \
    "The only value available must be closest, no matter what."

assert closest([0, 1], 0) == 0, \
    "Exact matches."

assert closest([0, 2], 1) == 0, \
    "Keep the first match in case of ties."
~~~
{: .python}

* This has already revealed two ambiguities
  * What does the function return when there are no values?
    * An exception is as plausible as `None`
  * What does the function do when faced with ties?
    * "Return first", "return last", "return any", and "return all" are all plausible

* *Test-driven development*
  * Write the tests, *then* write the code
  * Plant the goalposts, then kick the ball
  * Frees the programmer from cognitive bias (everyone wants their code to be correct)
  * Supporting evidence is actually mixed, but many programmers swear by it

* How to write unit tests for invasion percolation?
  * Given a grid, can test adjacency, density, etc.
  * Visualization is intrinsically hard to test
  * What about finding candidates?
    * Set up a grid and check that the candidates are in the list
    * But order may change based on optimizations
    * Need *deterministic behavior*

* What about end-to-end testing?
  * Given a grid, should see *this* pattern of fills
  * So need an auxiliary routine to compare filling state with an array of 0's and 1's
  * And a way to control what grid is created

* Refactor for test
  * Modify driver to put everything between grid creation and visualization in one function
  * Write an auxiliary function that takes a grid and an expected output and checks equality
  * Test cases are now easy to write

* Now that we can tell our program is correct, we can start to optimize performance
