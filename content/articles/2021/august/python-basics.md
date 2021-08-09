Title: Python Basics
Date: 2021-08-10 00:00
Category: Python
Tags: start, basics
Slug: python-basics
Authors: Julio Melanda
Summary: Hello, this is a quick introduction to Python programing language.
Lang: en

Hello!

I think it could be a good thing to start with a set of posts teaching the very basics of Python.

I won't teach you to install it because it's quite straightforward and if will be a different process for each operating system. So, just click here to find out how to [install python to your system](https://wiki.python.org/moin/BeginnersGuide/Download).

After having it installed, you're going to need a nice code editor to use while learning. I recommend [VSCode](https://code.visualstudio.com/download). If you're already used to another code/text editor, feel free to use it instead.

Open the terminal in your editor and run `python`. That should be enough to get you to the interactive shell of python if the binaries are correctly installed/referenced in the system.

You should see something that looks like this

```python3
Python 3.9.6 (default, Jul 16 2021, 00:00:00) 
[GCC 11.1.1 20210531 (Red Hat 11.1.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Note that the `>>>` are the cursor where you can enter new commands.

## Hello World

As every noteworthy beginner's guide we should start with the most loved and well known `Hello World` example.

In your python shell type

```python3
print("Hello World")
```

And hit enter. In the python shell it should look like this:

```python3
>>> print("Hello World")
Hello World
```

So, from now on, when the code is expected to be typed in the `Python Shell` we'll use the cursors to help you identifying it, as in the example above.

## Getting Input

The same way you can print data to the screen, you can ask for data from the user. Usually this data would be stored in a variable, which in python is dynamically created, so, no declaration needed.

Let's make a small scrip that asks for your age and prints it back to the screen.

```python3
>>> age = input("Type your age here => ")
Type your age here => 
```

Here you can type your age and hit `enter`, that will be read as a text, and then you can print it to the console.

```python3
>>> age = input("Type your age here => ")
Type your age here => 34
>>> print("Your age is", age)
Your age is 34
```

## Running a Python Script

Now that we know how to get data from the user and print it in the screen we can already create a simple script based in our small code.

In your editor, create a new file called `parrot.py`. We'll first greet the user with a `print` statement.

```python3
print("Welcome to parrot app. It will repeat whatever you type below")
```

Now we'll get the input into a variable that we'll call `text`.

```python3
text = input("=> ")
```

Finally we print the text back to the screen.

```python3
print("The parrot says", text)
```

This is the full content you should have in your file

```python3
print("Welcome to parrot app. It will repeat whatever you type below")
text = input("=> ")
print("The parrot says", text)
```

Now, in the terminal, exit the `python shell` with `exit(0)` or `CTRL+D`. In the regular terminal now you should run 

```shellscript
python parrot.py
```

This should ask for some text, and after you type and hit enter it should print it back to you. Something like this

```shellscript
$ python parrot.py
Welcome to parrot app. It will repeat whatever you type below
=> Hello World!
The parrot says Hello World!
```

And those were your first steps into Python. I hope you enjoyed this small tutorial and soon I'll continue with this series teaching more python basics.

Please let me know in the comments what you think and what else you would like to see in this blog :D

See ya!