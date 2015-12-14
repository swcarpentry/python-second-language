## Introduction to the Unix Command Line: Exercises

Obtaining the sample data:

`git clone https://github.com/callaghanmt/shell-training.git`

###Exercise 1

Create the following directory tree in your home directory (~):

    work
    work/input_data/
    work/results/
    work/program/

Create the file `input.txt`with a text editor and put some text in it.

Move the file to `work/input_data` and rename it in the same command to `control01.txt`

Create this directory tree in one line only: `work/experiment/results/report`

Delete the work directory and all of its contents with one single command.


###Exercise 2

Two new commands:

* The `sort` command will sort lines alphabetically
* You can use the `cut` command to split lines of text based on a given character
e.g. `cut -d ',' -f 2` will split lines around the comma and give you the second part

Combine `cat`, `cut`, and `sort` to print out the Latin names from `birds.txt` in alphabetical order

Save the output to a new file


###Exercise 3

List all the animals on the Isle of Man alphabetically and find the 50th item in that list


###Exercise 4

`shell-training/data/` contains 300 data files, each of which should contain 100 values. One of these files is missing some data though...

Use a series of commands connected by pipes to identify the file with missing data

hint `wc -w` will tell you the number of values in a file, `sort -n` will sort numerically


###Exercise 5

* In the `wildcards` directory, create a variable called `files` listing all of the text files.
* Loop through this list and print out the first line from each file.

	
###Exercise 6

What will this command print to the screen?

	[user@host wildcards]$ for filename in *.txt
	> do
	> echo $filename
	> cat $filename > new-file.txt
	> done

What will the contents of `new-file.txt` be and why?


###Exercise 7

Recreate the `a_directory/inside/the_other` tree if you deleted it.

Add `write` permission for users from your group for the full directory tree with one single `chmod` command (look in the man pages for more information).

What happens if you can read but not execute a directory?



###Exercise 8

Create a "Hello world"-like script using a text editor and execute it.

Redirect the output from your script to a file or another program.


###Exercise 9

Write a script which will create as many numbered directories as you want when you run it.


###Exercise 10

Write your own `mid` command which will print a selection of lines from the middle of a file depending on the arguments you pass to it.


