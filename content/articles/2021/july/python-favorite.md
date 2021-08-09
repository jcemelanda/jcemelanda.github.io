Title: Python, my favorite programming language
Date: 2021-07-31 06:00
Category: Opinion
Tags: python, preferences, stack
Slug: python-favorite
Authors: Julio Melanda
Summary: A few ideas and thoughts on why Python is my favorite language
Lang: en

Probably anyone that knows me knows I like Python, it's not really something new, as I have thousands of t-shirts from Python events I've been all over Brazil from 2015 to 2019.

So, I decided to try to put in words why I like it so much and it's so important in my life and my career.

### Simplicity

I think one of the first things that come to someone's mind when they think of Python is how simple it is. Python syntax is so straightforward that many times reading the code feels like reading English.

Take this for example:

```Python3
numbers = [1, 2, 3]

for number in numbers:
    if number > 2:
        print(number)
```

It's just beautiful.

### Rich options of 3rd party libraries

It's common to see jokes that in python you can do whatever you want by just importing a library.

It's surely not as easy, but definitely you have a huge number of libraries that already do or helps you doing almost everything you want to.

Some of the most amazing libraries I have used are:

#### requests

A library that makes it super easy and readable to call URLs using regular HTTP verbs like GET, POST, PUT, PATCH and DELETE. Here are some ecamples of how to call it.

```Python3
requests.get("test.com")
requests.post("test.com", data)
```

#### django

Django is a full featured web framework that allows you to create web applications with an inspiration in the MVC (Model-View-Controller) application architecture, (MVT in Django - Models, Views and templates). It has a great ORM that lets you create and control relational databases and their tables using Python classes for Models. Besides that it allows you to query the data using the model instances in a really simple way. It's really easy and powerful.

Not to mention that Django has an extensible admin interface that uses this same model classes to allow CRUD operations and the management of the data in your application.

A simple example of the ORM use.

```Python3
# Given a model User you can filter the users by a given name like
User.objects.filter(name="Mark")
```

#### pygame

Pygame is a simple SDL game engine. You need to control basically everything, even the flow of the game loop, but that doesn't make it a bad engine, actually that makes you understand in a much deeper level how a game works, the control of printing the images on the screen, the sprites animation and even collision.

Surely, Pygame lets you use some libraries for physics and 3D (OpenGL) for example. I myself wrote a small library to help control the camera and make it follow an object smoothly.

It'd be too long to put pygame code here, but I'll leave a link to a github repo containing a game I wrote.

[Math Shooter](https://github.com/jcemelanda/MathShooter)

### Powerful standard library

You may be asking yourself why should I want to make a language more complex bringing so many functionalities into the standard library if we can have tons of libraries that do those things just a `import` command away from you.

The thing is, managing dependencies can get quite complicated and the standard library have a high degree of optimization as most of it is written in C and works with the Python VM in a lower level than most libraries. That makes it faster in many cases and more efficient.

Some of my favorite libraries in the standard library are `random`, `itertools`, `regex`, `statistics`, `functools` and `pickle`.

### The zen of Python

If you open a python shell and execute `import this` you'll see a poem that kind of summarizes the philosophy behind Python.

<pre>
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
</pre>

Just read it and you'll see how those verses can inspire you to write better code.

### The Python Community

I met the language in 2007 and fell in love with it, but was in 2015, when I went to my first Python conference that I found out Python is not just a technology. It's a community of people that love to share knowledge and that try to make the world a better place. 

I met some of the best developers I ever dreamed of meeting like David Beazley and Luciano Ramalho and after the conference we'd go all together to a bar and talk until very late at night.

I learned so much and I was able to teach and help to. I got involved with PyLadies and DjangoGirls initiatives and I could inspire people and get inspired by them also.

### Finally

Those are just some brief reasons I have Python as my preferred language and I try to apply it everywhere I find it useful.

I hope this can inspire you as much as I got inspired myself all this years.

Happy coding and please tell me what you think in the comments!
