# relearning-python
After 3 years of experience in python revisioning core fundamentals of Python



## Internal Working ( 13th February 2025 )

#### Copy, Reference Coutn, Slice

## Numbers in Depth

## String in Python

## List in Python

#### List Slicing
```bash
    >>> nums = [1, 2, 3, 4]
    >>> nums = [0, 1, 2, 3, 4]
    >>> nums[1:1]
    []
    >>> nums[1:1] = [7, 8]
    >>> nums[:]
    [0, 7, 8, 1, 2, 3, 4]
    >>> nums[1:3]
    [7, 8]
    >>> nums[1:3] = []  # Inserting void at index 1, 2
    >>> nums[:]
    [0, 1, 2, 3, 4]
```

#### Insert, remove, pop in List
```bash
    >>> arr=[1,2,3,404]
    >>> arr.remove(404)
    >>> arr
    [1, 2, 3]
    >>> arr.insert(1,600)
    >>> arr
    [1, 600, 2, 3]
    >>> arr.pop()
    3
    >>> arr
    [1, 600, 2]
```

#### List comprehension
List Comprehension is a concise and efficient way to create list in Python using some expression.
```bash
    >>> [ x*x for x in range(1,6) ] 
    [1, 4, 9, 16, 25]
```

## Dictionary in Python

```bash
    >>> chai={"masala":"spicy", "ginger":"zesty", "green":"mild"}
    >>> chai
    {'masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}
    >>> chai["masala"]
    'spicy'
    >>> chai.get("ginger2")
    >>> chai["ginger2"]
    Traceback (most recent call last):
    File "<python-input-5>", line 1, in <module>
        chai["ginger2"]
        ~~~~^^^^^^^^^^^
    KeyError: 'ginger2'
    >>> chai["green"]="Fresh"
    >>> chai
    {'masala': 'spicy', 'ginger': 'zesty', 'green': 'Fresh'}
```
#### x in dict [ TC: O(1) ]     x in dict.values() [ TC: O(n)]

#### Pop in dict
```bash
    >>> chai.pop("ginger")
    'zesty'
    >>> chai
    {'masala': 'spicy', 'green': 'Fresh'}
```

#### Pop last entry of dict & delete operation
```bash
    >>> chai["new"] = "Black Tea"
    >>> chai
    {'masala': 'spicy', 'green': 'Fresh', 'new': 'Black Tea'}
    >>> chai.popitem()
    ('new', 'Black Tea')
    >>> chai
    {'masala': 'spicy', 'green': 'Fresh'}
    >>> del chai["green"]
    >>> chai
    {'masala': 'spicy'}
```
#### Mutable
```bash
    >>> hmap={
    ... "chai":chai,
    ... "name":"Tamal Mallick"
    ... }
    >>> hmap
    {'chai': {'masala': 'spicy'}, 'name': 'Tamal Mallick'}
    >>> chai
    {'masala': 'spicy'}
    >>> chai["green"]="mild"
    >>> chai
    {'masala': 'spicy', 'green': 'mild'}
    >>> hmap
    {'chai': {'masala': 'spicy', 'green': 'mild'}, 'name': 'Tamal Mallick'}
```
#### Dictionary Comprehension
```bash
    >>> square={x:x*x for x in range(1,5)}
    >>> square
    {1: 1, 2: 4, 3: 9, 4: 16}
    >>> square.clear()
    >>> square
    {}
```
#### Creating new dict
```bash
    >>> keys=["green","red","masala"]
    >>> default_value= "tea"
    >>> new_dict= dict.fromkeys(keys, default_value)
    >>> new_dict
    {'green': 'tea', 'red': 'tea', 'masala': 'tea'}
    >>> new_dict= dict.fromkeys(keys, keys)
    >>> new_dict
    {'green': ['green', 'red', 'masala'], 'red': ['green', 'red', 'masala'], 'masala': ['green', 'red', 'masala']}
```

## Tuple in Python

#### Immutable but supports all other operations like list()
```bash
    >>> t=(1,2,3,1,2,3,1,1)
    >>> t.count(1)
    4
```
# Lesson 1:
### Optimization at level Python < C < OS < CPU
Optimization happens at multiple levels:

Python < C < OS < CPU

    - Python: Interpreted, high-level, more overhead.

    - C: Lower-level, compiled, optimized memory handling.

    - OS: Manages processes, scheduling, memory paging.

    - CPU: Hardware-level optimizations, caching, parallel execution.

Each layer adds efficiency, with CPU-level optimizations being the fastest! 🚀

## Behaind the scene of Loops in Python

#### Iterator and Iterable
    - Calling iter(arr) returns an iterator object for the iterable ( x= iter([1,2,3,4]) & got x= <list_iterator object at 0x00000250EB95DCF0> ).

    - Iterator Object's memory reference stays the same between iterations.

    - Calling x.__next__() returns the current value and then __next__() moves to the next item ( returns 1 and moves to next element 2).

    - What changes: The internal position of the iterator (x.__next__() moves to the next item like from 1 to 2).

    - What does not change: The memory reference of the iterator object ,even after x.__next__() is called. (Remains x= <list_iterator object at 0x00000250EB95DCF0>).

    - StopIteration: When the iterator is exhausted, x.__next__() raises the StopIteration exception to signal the end of iteration and the for loop stops.
```bash
    >>> arr=[1,2,3,4]
    >>> x=iter(arr)
    >>> x
    <list_iterator object at 0x00000250EB95DCF0>
    >>> x.__next__()
    1
    >>> x
    <list_iterator object at 0x00000250EB95DCF0>
    >>> x.__next__()
    2
    >>> x.__next__()
    3
    >>> x.__next__()
    4
    >>> x.__next__()
    Traceback (most recent call last):
    File "<python-input-17>", line 1, in <module>
        x.__next__()
        ~~~~~~~~~~^^
    StopIteration
    >>>
```
#### Reference of file is by default it's Iterable Object
#### Reference of List/ Dictionary is not it's Iterable Object by default 
```bash
    >>> f= open('chai.py')
    >>> f is iter(f)
    True                    # Reference of Iterable of file object
    >>> f.__iter__() is iter(f)
    True                    
    >>> arr=[1,2,3]
    >>> iter(arr) is arr
    False                   # Reference of actual list object
    >>> next(arr)
    TypeError: 'list' object is not an iterator
    >>> z= iter(arr)        # Creating the Iterable of list object
    >>> z is iter(arr)
    True
    >>> next(z)
    1
```

# Function in Python

#### Topics
- Basic Function Syntax
- Functionwith multiple Parameters
- Polymorphism in Function : 2 *3= 6, "a"*3= "aaa"
- Default Parameter value
- Lambda function
- Function with *args : Takes n number of arguments as tuple
```python
def sum_all(*args):
    print(args, type(args))

    # map(... ) returns a lazy iterator that does not execute immediately
    list(map(lambda x: print(f"Cube of {x} is {x**3}"), args))
    # So, list(map(...)) is used to force execution by iterating over it.

    return f"Sum = {sum(args)}"

print(sum_all(1,2,4))
```
OUTPUT:
```bash
(1, 2, 4) <class 'tuple'>
Cube of 1 is 1
Cube of 2 is 8
Cube of 4 is 64
Sum = 7
```

- Function with **kwargs : Takes n number of keyword arguments as a dictionary.
```python
def print_kwargs(**kwargs):
    print(kwargs, type(kwargs))
    for key , value in kwargs.items():
        print(key," : ",value)

print_kwargs(power="Laddu", name="Chota Bhem", enemy="Kaliya")
```
OUTPUT:
```bash
{'power': 'Laddu', 'name': 'Chota Bhem', 'enemy': 'Kaliya'} <class 'dict'>
power  :  Laddu
name  :  Chota Bhem
enemy  :  Kaliya
```

- Generator  Function with yield : Returns values on demand using yield, without storing them all in memory.
```python
def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

print(type(even_generator(8)))

for num in even_generator(8):print(num, "\tGenerated")
```
OUTPUT:
```bash
<class 'generator'>
2 	Generated
4 	Generated
6 	Generated
8 	Generated
```

- Recursive Function : Recursion is a technique where a function calls itself to solve a problem by breaking it into smaller subproblems until a base case is reached.
```python
def factorial(n):
    print(f"Input : {n}")
    if n<2:
        return 1
    return n* factorial(n-1)
    
factorial(4)
```
OUTPUT:
```bash
Input : 5
Input : 4
Input : 3
Input : 2
Input : 1

120
```

### Highlights

#### Parameter vs. Argument in Python Functions

| Feature          | Parameter  | Argument  |
|-----------------|------------|-----------|
| **Definition**   | A variable in a function definition that acts as a placeholder for values. | The actual value passed to the function when it is called. |
| **Where It Appears** | In the function definition (inside parentheses). | In the function call (inside parentheses). |
| **Example**     | `def greet(name):` (`name` is a parameter) | `greet("Alice")` (`"Alice"` is an argument) |
| **Role**        | Acts as a placeholder that receives a value. | Supplies an actual value to the function. 

So in short, Parameters are variables in a function defination that act as placeholders for arguments passed during function call.

#### Generators vs Regular Functions

| Feature         | Generators (`yield`) | Regular Functions (`return`) |
|---------------|--------------------|--------------------------|
| **Memory Usage** | ✅ Memory-efficient (stores only the current value) | ❌ Uses more memory (stores all values at once) |
| **Execution** | ✅ **Lazy execution** (produces values one by one) | ❌ **Eager execution** (computes everything immediately) |
| **State Retention** | ✅ **Remembers where it left off** (resumes from `yield`) | ❌ **Does not retain state** (starts fresh each call) |
| **Return Type** | ✅ Returns a **generator object** (an iterator) | ❌ Returns a **final computed value** |
| **Use Case** | ✅ Ideal for **large datasets, streaming, infinite sequences** | ❌ Best for **small computations and immediate results** |
| **Performance** | ✅ Efficient for iterating over large collections | ❌ Slower for large data (high memory usage) |

### When to Use Generators?
- ✅ Processing **large files** (reading line by line)
- ✅ Streaming **real-time data** (logs, APIs)
- ✅ Generating **infinite sequences** (Fibonacci, primes)

So in short, A generator is a special function that returns an iterator and yields values one at a time, storing only the current state in memory for efficient execution.


# Scopes , Global and Closure in Python
Python uses the LEGB rule (Local, Enclosing, Global, Built-in) to resolve variable names

### Scope
Scope is the area where a variable can be accessed or used in our code.

``` python
user= "Ram"

def fun():
    user = "Tamal"
    def new():
        user="mallickboy"
    new()
    print(user)

fun()
print(user)
```
OUTPUT:
```bash
Tamal
Ram
```

### `global` keyword
global tells Python to use and update the global variable's pointer instead of making a new local one.
```python
user= "Ram"

def fun():
    global user  # Refers to the global 'user' variable
    user = "Tamal"
    def new():
        user="mallickboy"   # Local to 'new', does NOT affect the global 'user'
    new()
    print(user)

fun()
print(user)
```
OUTPUT
```bash
Tamal
Tamal
```

#### `global` can create a variable in the global namespace (module-level memory scope) of Python.

```python
def myfun():
    global x
    x = 100  # No global x existed before, now created
myfun()
print(x)
```
OUTPUT:
```bash
100
```

#### `global` directly refers to global variable's reference
`globl` keword tell to refer variable reference of global memory scope , it doesn't perform that LEGB rule. So parent may have different same variable with different reference and values

```python
var= "I am from Global Scope"
def myfun():
    var="I am from local of myfun Scope"  # Has different reference than the global `var` 
    def nested():
        global var  # Refers to the global `var`, not the local one
        var="I am from local of myfun.nested Scope"
    print(var)  # (1) Before nested() call → local `var` of `myfun`
    nested()    # This updates the global `var`
    print(var)  # (2) After nested() call → still local `var` of `myfun`
myfun()
print(var)      # (3) Global `var`, which was updated in nested()
```
OUTPUT:
```bash
I am from local of myfun Scope
I am from local of myfun Scope
I am from local of myfun.nested Scope
```

### Clousure
Closure is when an inner function remembers and uses (depends on and has access to ) variables from its outer function even after the outer function has finished.

#### ✅ Clousure: bagpack has values 
```python
def f1():
    x= 88           # x is local to f1
    def f2():
        print(x)    # f2 uses x from the enclosing f1
    return f2
myf=f1()            # myf is now f2, with x=88 stored inside its closure
print("Nested function : ")
myf()
print("Got clousure: ",myf.__closure__[0].cell_contents if myf.__closure__ else myf.__closure__)
```
OUTPUT:
```bash
Nested function : 
88
Got clousure:  88
```

#### ❌ Not Clousure: bagpack is empty
```python
def f1():
    x= 88
    print(x)
    def f2():
        print(10)
    return f2
myf=f1()
print("Nested function : ")
myf()
print("Got clousure: ",myf.__closure__[0].cell_contents if myf.__closure__ else myf.__closure__)
```
OUTPUT:
```bash
88
Nested function : 
10
Got clousure:  None
```

### Working of `print()` 
`print()` goes left to right, runs everything, turns them into text, and shows them concatenated in one line with spaces.

```python
def funct():
    print("Executed")
    return 200
print("Func:\n",funct())
```
OUTPUT:
```bash
Executed
Func:
 200
 ```