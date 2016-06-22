---
title: "Performance"
teaching: 0
exercises: 0
questions:
- "What other data structures can I use in my programs?"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---

* How fast is our program?
  * Search N^2 cells each time we fill one
  * Fill somewhere between N and N^2 cells, so call it N^1.5
  * So NxN grid requires N^3.5 steps
  * Ouch
  * Speeding up individual steps won't make much of a difference
  * And searching inside an ever-expanding window won't help much either
  * Need an entirely new approach

* Why are we re-searching each time?
  * Fill in a cell adds at most 3 new cells to our list of candidates
  * So store `(v, x, y)` in a list, sorted by `v`
  * Inserting takes N/2 steps on average, so runtime is approximately N^2.5

* But we can do even better
  * List is sorted, so we can use [binary insertion][binary-insert] to insert in the right place in log_2 N steps
  * Runtime becomes N^1.5 log_2 N

| N     | naive |  fast | speedup |
|-------|-------|-------|---------|
|    11 |  4.4K |  126  |     35  |
|   101 | 10.3M |  6.7K |    1.5K |
|  1001 | 31.7G |  315K |    100K |
| 10001 | 100T  | 13.2M |    7.5M |

* *Better algorithms are better than better hardware.*

* What needs to change?
  * Generation and visualization stay the same

~~~
candidates = []                               # now persistent
while not on_edge(last_filled):
    add_candidates(candidates, last_filled)   # add neighbors (avoiding duplication)
    last_filled = select(candidates)          # will modify candidates
    fill_cell(last_filled)
~~~
{: .python}

* FIXME: profile

[binary-insert]: https://docs.python.org/3.5/library/bisect.html
