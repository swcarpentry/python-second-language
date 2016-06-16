---
title: "Invasion Percolation"
teaching: 0
exercises: 0
questions:
- "How can I build larger programs in Python?"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---

* Invasion percolation
  * NxN grid of integer cells
  * Fill in center
  * Fill lowest-value neighbor on boundary of filled region
    * Break ties randomly
    * So have to record candidates and then select
  * Continue until filled region hits boundary
  * How does density of filling depend on range of values?

* Start with a main driver
  * Takes grid size N and random range R as parameters
    * Eventually wrap this in something that reads them from the command line
  * Create grid
  * Select and fill until on edge
  * Visualize
  * Calculate density

* How to represent grid?
  * NumPy array is just what we need
  * And comes with random filling

* How to initialize?
  * Fill center cell with marker value -1
    * Could keep a separate Boolean array of filled markers
  * Insist that N be odd so that "center" is unambiguous

* How to fill?

~~~
while not on_edge(last_filled):
    candidates = find_candidates()
    last_filled = select(candidates)
    fill_cell(last_filled)
~~~
{: .python}

* How to fill a cell?
  * Easy: assign -1
  * Use a function because we might want to do other things later (e.g., logging)

* How to select which cell to fill?
  * Easy: randomly select an item from the list of candidates
  * Which means we've decided to use a list of candidates
  * Which contains (x, y) coordinates

* How to find candidates?

~~~
candidates = []
least = None
for location in array:
  if is_adjacent(location):
    value = array[location]
    if (least is None) or (value < least):
      least = value
      candidates = [location]
    elif value == least:
      candidates.append(location)
return candidates
~~~
{: .python}

* How to visualize?
  * Create ipythonblocks grid the same size as the array
  * Color each cell to show filled/unfilled status
  * Optional: color unfilled cells to show value

* How to calculate density?
  * Count number of filled cells and divide by N^2
  * Can do this:
    * With a double loop
    * Using array methods
    * Incrementally

* Now have skeleton of program
  * Go ahead and implement with partner
  * **Ask us** whenever you don't know how to do something you want to do
  * On-demand teaching: you are all bringing different background knowledge, so you'll all have different questions
