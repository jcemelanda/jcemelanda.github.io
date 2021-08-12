Title: Python Code Blocks
Date: 2021-08-12 00:00
Category: Python
Tags: start, basics, code block
Slug: python-code-blocks
Authors: Julio Melanda
Summary: Hi, let's talk a bit aboutcode blocks in Python as it's one of the main characteristics of the language.
Lang: en

Hi!

Continuing the Python series, let's talk about code blocks.

For those who missed the first post, here's a link:
[Python Basics](python-basics.html)

In the Python shell, we have two cursors.
```python3
>>>
...
```

The first one we've already seen in the previous post, and it's where you type Python commands in. The second is a code block indicator. There you insert commands that will be inside a code block.

For example, when we do an if, conditional structure that will be explained in more detail in a next post, we can have the following in the shell

```python3
>>> x = 0
>>> if x < 1:
...     print("x is less than 1")
...
x is less than 1
```

Now the explanation =]

In the first line, we say that the variable x contains the value 0;
Next, we compare the value contained in x with 1. When we finish a command with : the interpreter understands that this is a command that did not end at the end of that line, and that it is composed of more commands, so the secondary cursor `.. .`.

So, many programmers used to other languages ​​must ask themselves where the curly braces are to determine the where the block starts and ends.

In Python, blocks are determined by indentation.

The lines that are inside the if, that is what should be executed if the comparison is true, must be indented.

It is generally a convention in Python that we use 4 spaces for indentation.

Returning to the subject, print("x is less than 1") is the command that should be executed if the comparison x < 1 is true. So, this line is indented, and the interpreter knows that it should only execute it if x is less than 1.

When you give an enter at the end of this line, the interpreter shows you the secondary cursor again, because an if can have several commands inside it. As we'll see later, the execution of an entire program can be inside an if.

Thus, only after a second enter does the interpreter execute the command and display the result.

So, to recap:

* Python blocks are defined by indentation
* Indentation must follow a pattern, preferably in all programs
* In the shell, indented blocks are preceded by secondary courses...
* A block indicates a piece of code that is inside another command

In a python script like the parrot we wrote in the previous post, we did the same basically.

```python3
print("Welcome to the parrot app. It will repeat everything you type below")
text = input("=> ")
if text:
    print("The parrot says", text)
else:
    print("You should type something before you hit ENTER")
``` 
