---
title: "File I/O"
teaching: 10
exercises: 5
questions:
- "How can I read data from a file?"
- "How can I write data to a file?"
objectives:
- "Use `open`, `read`, and `readline` to read data from a file."
- "Use a file in `for` loop."
- "Use `write` to save data to a file."
- "Use basic string operations to process text data."
keypoints:
- "Open a file for reading or writing with `open`."
- "Use `read` or `readline` to read directly."
- "Use file in `for` loop to process lines."
- "Use `write` to add data to a file."
---
## Use `open` to open files for reading or writing.

*   Arguments are a path and:
    *   'r' for reading
    *   'w' for writing (immediately erases existing contents)
    *   'a' for appending
*   Result is an object with methods for reading and writing.
    *   `file.read()` reads the entire file.
    *   `file.read(N)` reads up to that many bytes.
*   Close files with `file.close`.

~~~
reader = open('myfile.txt', 'r')
data = reader.read()
reader.close()
print('file contains', len(data), 'bytes')
~~~
{: .python}
~~~
file contains 47189 bytes
~~~
{: .output}

## Usually read text files with `for` loops.

*   Automatically calls `file.readline`.

~~~
reader = open('myfile.txt', 'r')
count = 0
for line in reader:
    count = count + 1
reader.close()
print('file contains', count, 'lines')
~~~
{: .python}
~~~
file contains 261 lines
~~~
{: .output}

## Python preserves end-of-line newlines.

*   By default, converts Windows '\r\n' to Unix '\n'.

## Strip whitespace using string methods.

*   Use `str.strip` to strip leading and trailing whitespace.
    *   `'  abc '.strip()` is `'abc'`.
*   Use `str.rstrip` or `str.lstrip` to strip space from right or left end only.
*   All of these methods return new strings.
    *   Because strings cannot be modified in place.

~~~
reader = open('myfile.txt', 'r')
count = 0
for line in reader:
    line = line.strip()
    if len(line) > 0:
        count = count + 1
reader.close()
print('file contains', count, 'non-blank lines')
~~~
{: .python}
~~~
file contains 225 non-blank lines
~~~
{: .output}

> ## Using `with` to Guarantee a File is Closed
>
> It is good practice to `close` a file after you have opened it.
> You can use the `with` keyword in Python to ensure this:
>
> ~~~
> with open('myfile.txt', 'r') as reader:
>     data = reader.read()
> print('file contains', len(data), 'bytes')
> ~~~
> {: .python}
>
> The `with` statement has two parts:
> the expression to execute (such as opening a file)
> and the variable that stores its result (in this case, `reader`).
> At the end of the `with` block,
> the file that was assigned to `reader` will automatically be closed.
> `with` statements can be used with other kinds of objects
> to achieve similar effects.
{: .callout}

> ## Squeezing a File
>
> 1.  Write a small program that reads lines of text from a file called `input.dat`
>     and writes those lines to a file called `output.dat`.
>
> 2.  Modify your program so that it only copies non-blank lines.
>
> 3.  Modify your program again so that a line is not copied
>     if it is a duplicate of the line above it.
>
> 4.  Compare your implementation to your neighbor's.
>     Did you interpret the third requirement (copying non-duplicated lines)
>     the same way?
{: .challenge}
