# Head First Python
Study note for Head First Python

### Chapter 1 : Getting Started Quickly (P1)
    Everything is an Object in Python
    from 'module.py' import 'submodule/class'
    dir(module) to list attributes / methods in the module
    help(module.method) to display detail about module.method
    print() : end='|', sep=','

### Chapter 2 : Working with Ordered Data (P47)
    list[1,2,3]

### Chapter 3 : Working with Structured Data (P95)
    dict {key:value,key:value} : Key / Value
    set {value, value, value} : No Duplicate
    tuple (value, value, value) : READ ONLY

### Chapter 4 : Functions and Modules (P145)
    BIF : Build-in Function
    PEP : Python Enhancement Protocol
    Pass by reference, Pass by value
    pytest / pep8 testing framework
    use setuptool to deploy custom module to site-package

### Chapter 5 : Getting Real - build web app (P195)
    Use flask (web app framework)
    pip install flask
    __name__ => pronoun 'dunder name'

### Chapter 6 : Where to Put Your Data - storing and manipulating data(P243)
    Working with file
    with statement : context management protocol
    open('file', 'mode')

### Chapter 7 : Putting Python's DB-API to use - using a database (P281)
    Use MySQL or MariaDB
    Install MySQL for Python driver

### Chapter 8 : Abstracting Behavior and State - a little of class (P309)
#### Naming Convention
    function name : lower case => country_from_by()
    class name : CamelCase => CountryFromBy()

    class CountryFromBy():
        statement

    self keyword = this keyword in other language
    always to self.val to refer the variable in the class

### Chapter 9 : Hooking into Python's with Statement - the context management protocol (P335)
    elaborate context management protocol (with statement)
    use context management protocol to simply the process of setup and close database.

### Chapter 10 : Wrapp Functions - function decorator (P363)
    Decorator : add code to an existing function without modify any of the existing function's code.
    use session.

### Chapter 11 : What to Do When Things Go Wrong - Exception handling (P413)
    2 big web attacks : SQL injection (SQLi) and Cross-site scripting (XSS)
    Create custom error message.  see DBcm.py

### Chapter 11 1/3 : A Little Bit of Threading - Dealing with Waiting (P461)
    Ch11Thread.py

    from threading import Thread
    t = Thread(target=func_name, args(arg1, arg2))
    t.start()

### Chapter 12 : Advanced Iteration - Looping like Crazy (P477)
    string.strip() : remove begin/end whitespace

#### Comprehension
    replace for loop 
    1.  faster
    2.  can place in for loop cannot place
#####    Normal loop
    dests = []
    for dest in flights.values():
        dests.append(dest.title())
#####    Comprehension
    dest2 = [dest.title() for dest in flights.values()]

    listcomp = ['value' 'for loop' 'if filter' ]
    listcomp, dictcomp, setcomp but no tuplecomp

#### Generator
    Use () as generator instead of []
    Performance is better.
    return result once available and one by one.
    use yield instead of return in generator function.

### A : Installing - Installing Python (P521)

### B : Pythonanywhere - Deploying Your Webapp (P529)

### C : Top Ten Things We Didn't Cover - There's Always More to Learn (P539)
2.  Virtual Programming Enviroments
3.  More on Object Orientation
5.  Getting Things Sorted
6.  More from the Standard Library
    collections.
        OrderedDict, Counter, ChainMap
    itertools
    functools
7.  Running Your Code Concurrently
        multiprocessing, asyncio, concurrent.futures
        New Keywords: async and await
8.  GUIs with Tkinter (and Fun with Turtle)
9.  Automated testing
        doctest, unittest
10. Debug, Debug, Debug
        Python's debugger : pdb

### D : Top Ten Projects Not Covered - Even More Tools, Libraries, and Modules (P551)
3.  Jupyter Notebook : The web-based IDE
4.  Doing Data Science
        Best place for data science is the PyData : pydata.org
        bokeh: A set of technologies for publishing interactive graphics on web pages.
        matplotlib/seaborn:  A comprehensive set of graphing modules (which integrates with ipython and jupyter notebook)
        numpy: Store and manipulate multidimensional data(Matrices).
        scipy: A set of scientific modules optimized for numerical data analysis, which complements and expands upon what's provided by numpy.
        pandas: provides optimized analysis data structures and tools (built on top of numpy and matplotlib).  pandas is another killer Python application.
        scikit-learn: A set of machine learning alogrithms and technologies implemented in Python.
5.  Web Development Technologies
        Flask, Django

6.  Working with Web Data
        requests, Beautiful Soup, Scrapy

7.  More Data Sources
        sqlalchemy: the database toolkit for Python
        www.sqlalchemy.org

8.  Programming Tools
        Pylint, Python's code analysis tool:

9.  Kivy
    A Python library for develop multitouch interfaces.

10. Python Cookbook : OReilly

### E : Getting Involved - The Python Community (P563)