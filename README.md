# relearning-python
After 3 years of experience in python revisioning core fundamentals of Python



## Internal Working ( 13th February 2025 )

When we import a Python module, Python compiles it into bytecode and stores it in the `__pycache__` folder for faster execution in the future. However, if we modify the code of the imported module, Python will continue using the old version unless we explicitly reload the module.

To apply the changes we’ve made to a module without restarting the Python runtime, we can use `importlib.reload()`. This allows us to dynamically apply updates during runtime.


```python
import a.b.my_module as lib

lib.hellow("World")

from importlib import reload
reload(lib)     # reloading the imported module after making changes

lib.hellow("World Reloaded")
```

OUTPUT:
```bash
Hellow World
Hellow World Reloaded
```

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

### Global
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


 # Object Oriented Programming (OOPs) in Python

### Idea
OOP is like creating a metal casting mold—the class is the mold, designed with code (Python, C++, Java) to define structure and features. When we create an object, it's like making a doll from the mold—allocating memory, applying the class design, and getting a fully shaped base.
We then customize the doll—adding hair, paint, clothes—similar to calling methods on the object with specific parameters. Each object becomes a unique, independent, self-sufficient product, ready to be shipped or combined into larger systems.
OOP helps us build reusable, modular, and organized code—just like a factory producing various custom dolls from the same reliable mold.

```Python
class MetalMold:
    def __init__(self, name="a Doll"):
        self.doll = f"I am {name}."

    def add_hair(self, color="Black"):      #  Adds hair color to the doll
        self.doll += f" I have {color} hair."

    def add_costume(self, costume_name):            # Adds a costume to the doll.
        self.doll += f" I have a {costume_name} costume."

    def add_decorations(self, items):       # Adds accessories or decorations to the doll.
        self.doll += f" I have {', '.join(items)}."

    def know_about_me(self):                # Returns the doll's final description.
        return self.doll

# Creating objects / base body
doll_1, doll_2 = MetalMold("Cinderella"), MetalMold("Rosey")

# Now decorating using methods
doll_1.add_hair(color="Blond")  
doll_1.add_costume(costume_name="Annabelle")  

doll_2.add_hair()  
doll_2.add_costume(costume_name="Chucky")  
doll_2.add_decorations(items=["Purse", "Hat", "Chain"])  

# Displaying final details
print("Doll 1:\n", doll_1.know_about_me())  
print("Doll 2:\n", doll_2.know_about_me())  
```

OUTPUT:
```bash
Doll 1:
 I am Cinderella. I have Blond hair. I have a Annabelle costume.
Doll 2:
 I am Rosey. I have Black hair. I have a Chucky costume. I have Purse, Hat, Chain.
```
### Topics
### 1. Basic Class and Object
TAsk: Create a Car class with attributes brand and model. Then create an instance of that class.

- Attributes : Variables (brand, model)
- Instance : A4 copy of pdf form or a doll of a doll mold. A memory image of that class.

```python
class Car:
    def __init__(self, brand, model)->None:     # Automatically called at begining
        self.brand= brand   # Attributes     
        self.model= model

my_car=Car("Toyota", "Corolla")        # instance of class (object 1) : usable memory image of class Car
print(my_car.brand, my_car.model)

new_car=Car("Tata", "Safari")          # object 2
print(new_car.brand, new_car.model) 
```

OUTPUT:
```bash
Toyota Corolla
Tata Safari
```

### 2. Class Method and self
Task: Add method to the class to display full name.

- self works as a connection line to reach different componentsof the class. Like using Telephone line to call them.

```python
class Car:
    def __init__(self, brand, model)->None:
        self.brand= brand   # Attributes     
        self.model= model

    def full_name(self):    # self works as a connection line to reach different componentsof the class.
        return f"Full Name : {self.brand} {self.model}"
my_car=Car("Toyota", "Corolla")        # instance of class (object 1) : usable memory image of class Car
print(my_car.full_name())

new_car=Car("Tata", "Safari")          # object 2
print(new_car.full_name())
```

OUTPUT:
```code
Full Name : Toyota Corolla
Full Name : Tata Safari
```

### 3. Inheritance
Task: Create an Elecrtic car class that inherits from Car class and has additional attribute battery_size.

```python
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # self.brand= brand                 # no need predefined
        super().__init__(brand, model)      # Taking parental access
        self.battery_size= battery_size
tesla_car=ElectricCar("Tesla", "Model S", "85 kWh")
print(tesla_car.brand, tesla_car.model, tesla_car.battery_size)
print(tesla_car.full_name())
```

OUTPUT:
```bash
Tesla Model S 85 kWh
Full Name : Tesla Model S
```

### 4. Encapsulation
Restricting the direct access on class attributes. Only permitting some custom access though class methods.

Task: Modify the Car class to encapsulate the brand attribute, making it private and provide a getter method for it.

##### Not encapsulated
```python
class Car:
    def __init__(self, brand, model):
        self.model= model
        self.brand= brand

    def get_brand(self):
        return self.brand + "!"
    
tesla_car=Car("Tesla", "Model S")
print(tesla_car.brand, tesla_car.model)
tesla_car.brand= "Tata"     # Overwritten outside of the class ,Open access --> Not secure
print(tesla_car.get_brand())
```

OUTPUT:
```bash
Tesla Model S
Tata!
```

##### After encapsulation
```python
class Car:
    def __init__(self, brand, model):
        self.model= model
        self.__brand= brand     # private class attribute

    def get_brand(self):        # custom access on private attributes
        return self.__brand + "!"
    
tesla_car=Car("Tesla", "Model S")
print(tesla_car.get_brand())
```

OUTPUT:
```bash
Tesla!
```
##### Try to edit
```python
tesla_car=Car("Tesla", "Model S")
tesla_car.__brand= "Tata Motors"
print(tesla_car.get_brand())
```

OUTPUT:
```bash
Tesla!
```

##### Try to read directly

```python
tesla_car=Car("Tesla", "Model S")
print(tesla_car.get_brand())
print(tesla_car.__brand)
```
OUTPUT:
```bash
Tesla!
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[79], line 11
      9 tesla_car=Car("Tesla", "Model S")
     10 print(tesla_car.get_brand())
---> 11 print(tesla_car.__brand)

AttributeError: 'Car' object has no attribute '__brand'
```

##### Try to write first then read private attributes
```python
tesla_car=Car("Tesla", "Model S")
print(tesla_car.get_brand())           # Output: Tesla!

tesla_car.__brand= "Tata Motors"       # This does NOT overwrite the private __brand instaed creates new one. also if not created raed attemp gives error
print(tesla_car.__brand)               # Output: Tata Motors (new attribute created)

print(tesla_car.get_brand())           # Output: Tesla!

print("All instances of this Object:",tesla_car.__dict__)       # all the instance attributes of an object
```

OUTPUT:
```bash
Tesla!
Tata Motors
Tesla!
All instances of this Object: {'model': 'Model S', '_Car__brand': 'Tesla', '__brand': 'Tata Motors'}
```

Hence created new instance `__brand` for external use, the original `__barnd` is donoted by `_Car__brand` : `_<class name><private attribute>` . Private attribute starts with `self.__<attribute name>`.

We can still use `__brand` freely inside the class.

### 5. Polymorphism
Taking different forms like BahuRupi. Water --> Vapour --> Ice
Example : standard `+` of python as it adds strings as well as numbers.

```python
class Car:
    def __init__(self, brand, model):
        self.model= model
        self.__brand= brand     # private class attribute

    def get_brand(self):        # custom access on private attributes
        return self.__brand + "!"
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size= battery_size
    def fuel_type(self):        # Also overwrites the method of parent, Car class
        return "Etectricity"

tesla_car=ElectricCar("Tesla", "Model S", "85 kWh")
print(tesla_car.model, tesla_car.fuel_type())

safari_car=Car("Tata Motors", "Safari")
print(safari_car.model, safari_car.fuel_type())
```

OUTPUT:
```bash
Model S Etectricity
Safari Petrol or Diesel
```

### 6. Class Variables
Task: Add a class variable to Car that keeps tarck of the number of car created.

```python
# Task: Add a class variable to Car that keeps tarck of the number of car created.
class Car:
    total_car=0
    def __init__(self, brand, model):
        self.model= model
        self.__brand= brand     # private class attribute
        Car.total_car += 1      # class variable
        # self.total_car += 1   # Alternate

    def get_brand(self):        # custom access on private attributes
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
x=Car("Tata Motors", "Jaguar")
Car("Tata Motors", "Safari")
Car("Tata Motors", "Nano")
Car("Tata Motors", "Sumo")

print(Car.total_car, x.total_car)
```

OUTPUT:
```bash
4 4
```

### 7. Static Method
A method that belongs to the class itself, not to any specific instance of the class (object).

```python
class Car:
    total_car=0
    def __init__(self, brand, model):
        self.model= model
        self.__brand= brand     # private class attribute
        Car.total_car += 1      # class variable
        # self.total_car += 1   # Alternate
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def general_description(self):
        return "Cars are means of transportation."
    
my_car=Car("Tata Motors", "Jaguar")

print(my_car.general_description())
print(Car.general_description())
```

OUTPUT:
```bash
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[32], line 19
     16 my_car=Car("Tata Motors", "Jaguar")
     18 print(my_car.general_description())
---> 19 print(Car.general_description())

TypeError: Car.general_description() missing 1 required positional argument: 'self'
```

```python
class Car:
    total_car=0
    def __init__(self, brand, model):
        self.model= model
        self.__brand= brand     # private class attribute
        Car.total_car += 1      # class variable
        # self.total_car += 1   # Alternate
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "Cars are means of transportation."
    
my_car=Car("Tata Motors", "Jaguar")

print(Car.general_description())
print(my_car.general_description())
```

OUTPUT:
```bash
Cars are means of transportation.
Cars are means of transportation.
```
So, Imagine a school (class) that has a notice board (static method).
The notice board belongs to the school, not any individual student (object).

However, any student who walks by can still read the notice — but that doesn’t mean the notice belongs to them.

##### For Python :
- Static methods belong to the class.
- Python's design says: "Hey, for convenience, I'll let objects access their class-level tools too."

### 8. Property Decorators
Task: Use the Property Decorator in yhe Car class to make the model attribute read-only.

The @property decorator allows controlled, read-only access to private attributes using simple attribute-like syntax without direct modification from outside the class.

##### Why ?
```python
class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__model= model
        self.__brand= brand     # private class attribute
        Car.total_car += 1      # class variable

    def model(self):
        return self.__model
    
my_car=Car("Tata Motors", "Jaguar")

print(my_car.__dict__)
my_car.model= "Safari"

print(my_car.__dict__)
print(my_car.model())
```

OUTPUT:
```bash
{'_Car__model': 'Jaguar', '_Car__brand': 'Tata Motors'}
{'_Car__model': 'Jaguar', '_Car__brand': 'Tata Motors', 'model': 'Safari'}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[21], line 18
     15 my_car.model= "Safari"
     17 print(my_car.__dict__)
---> 18 print(my_car.model())

TypeError: 'str' object is not callable
```
As __model is now private so model craetes a new attribute for oject stroing model ="Safari" so it got overwritten to str an no more a method of class.

##### Fix 
@property decorator makes sure to to keep that method name unique and prevent accidental variable declearation useing exact same attribute name.
```python
class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__model= model
        self.__brand= brand     # private class attribute
        Car.total_car += 1      # class variable

    @property       # Hiding, access through method | Read-only
    def model(self):
        return self.__model
    def ch(self):
        self.__model="xyz"
    
my_car=Car("Tata Motors", "Jaguar")

print(my_car.__dict__)
print(my_car.__dict__)
print(my_car.model)
my_car.model= "Safari"      # Unable to overwrite
```

OUTPUT:
```bash
{'_Car__model': 'Jaguar', '_Car__brand': 'Tata Motors'}
{'_Car__model': 'Jaguar', '_Car__brand': 'Tata Motors'}
Jaguar
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[32], line 19
     17 print(my_car.__dict__)
     18 print(my_car.model)
---> 19 my_car.model= "Safari"

AttributeError: property 'model' of 'Car' object has no setter
```

### 9. Class Inheritance and isinstance() Function
Task: Demonstrate the use of isinstance() to check if `tesla_car` is an instance of Car and ElectricCar.

```python
tesla_car=ElectricCar("Tesla", "Model S", "85 kWh")

print(isinstance(tesla_car, Car))

print(isinstance(tesla_car, ElectricCar))
```

OUTPUT:
```bash
True
True
```

### 10. Multiple Inheritance
Task: Craete 2 class Battery and Engine, and let the ElectricCar class inherit from both.

```python
class Car:
    def __init__(self, brand, model):
        self.model= model
        self.__brand= brand     # private class attribute

class Battery:
    battery="I have 85 kWh Battery."

class Engine:
    engine="I have X41 Brushless motors."

class ElectricCar(Battery, Engine, Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size= battery_size
    def fuel_type(self):
        return "Etectricity"

tesla_car=ElectricCar("Tesla", "Model S", "85 kWh")

print(tesla_car.__dict__)       # only contains instance-level attributes
print(tesla_car.battery, tesla_car.engine)
```

OUTPUT:
```bash
{'model': 'Model S', '_Car__brand': 'Tesla', 'battery_size': '85 kWh'}
I have 85 kWh Battery. I have X41 Brushless motors.
```

- Python supports multiple inheritance.
- The `__dict__` of an object (`tesla_car.__dict__`) only contains instance-level attributes, which are the attributes directly defined in the object itself via self. in the `__init__()` method or elsewhere.


# Decorators
A decorator is a function that wraps another function to modify or extend its behavior without changing its actual code.

- Decorators take a function as input, wrap it inside another function (called a wrapper), add extra behavior before or after the original function runs, and then return this new wrapped function to replace the original. 

- From that point onward, whenever we call the original function, we’re actually calling and executing the wrapper, which contains both the original logic and the added functionalities provided by the decorator.

- Decorators replace the original function's reference with a new wrapped object in memory, so every future call executes the wrapper, not the original function directly.

### 1. Timing Function Execution
```python
import time

def runtime(fun):
    def wrapper(*args, **kwargs):
        start= time.time()
        res= fun(*args, **kwargs)
        print(f"Function `{fun.__name__}` executed in ",time.time()-start)
        return res
    return wrapper

@runtime
def example_function(n):
    print("Hellow")
    time.sleep(n)

example_function(1)
```

OUTPUT:
```bash
Hellow
Function `example_function` executed in  1.0008952617645264
```

### 2. Debugging Function Call
Create a decorator to print the function name and values of its arguments every time function is called.
```python
def debug(function):
    def wrapper(*args, **kwargs):
        args_values= ', '.join(str(arg) for arg in args)
        kwargs_values= ', '.join(f"{key}: {value}" for key, value in kwargs.items())
        print(f"Callibg `{function.__name__}` with args: `{args_values}` and kwargs: `{kwargs_values}`")
        res= function(*args, **kwargs)
        return res
    return wrapper

def helo():
    print("Hellow!")

@debug
def greet(name, greeting="Hellow!"):
    print(f"{greeting} {name}")
    
greet("Tamal", greeting="Yoo")
```

OUTPUT:
```bash
Callibg `greet` with args: `Tamal` and kwargs: `greeting: Yoo`
Yoo Tamal
```

### 3. Cache Return Values
Implement a decorator that caches the return values of a function, so that when it called with same arguments again, the cached value is returned instead of reexecuting the function.

```python
import time

def cache(function):
    cached_value= {}                    # O(1) access time 
    print("cached values: ",cached_value)
    def wrapper(*args, **kwargs):
        print("cached growth: ",cached_value)
        if args in cached_value:
            return cached_value[args]
        res= function(*args, **kwargs)
        cached_value[args]= res         # caching the args: result

        return res
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(2)                       # let it performing database calls
    return a+ b   

```

OUTPUT:
```bash
cached values:  {}
```
##### What happens at runtime:
- Python runs the script top to bottom.
- It sees `@cache` on `long_running_function`.
- It executes `cache(long_running_function)` and prints `"cached values: {}"`.
- The returned wrapper function replaces `long_running_function`.
- Now every time we call `long_running_function()`, we are actually calling `wrapper()`, which uses the same `cached_value`.

```python
print(long_running_function(2,3))
print(long_running_function(3,3))
print(long_running_function(2,3))
```

OUTPUT:
```bash
cached growth:  {}
5
cached growth:  {(2, 3): 5}
6
cached growth:  {(2, 3): 5, (3, 3): 6}
5
```

### ✅ Function From Memory Perspective
A function name (like fun) is just a reference (label) to a function object stored in memory, which holds the actual definition — all the code we wrote inside (like if-else, loops, arrays, etc.).

When we call the function (fun()), Python uses that reference to locate the function object, passes the argument objects to it, executes the code, and finally returns the result to the caller (for example, in x = fun(1, 2), the caller is the line of code x = fun(1, 2), and x stores the returned result).

### ✅ Decorators Effect on Functions From Memory Perspective

As Python executes code from top to bottom, when the interpreter finds a `@decorator`, it takes the original function object from memory, passes it into the decorator, which wraps it inside a new function object (the wrapper) that adds extra behavior.

This new wrapper function is created as a **separate object in memory**, and Python updates the original function's name reference to now point to this new wrapper object (overwriting the old reference).

So, from that moment onward, whenever we call the original function name, we are actually triggering the new wrapper function object in memory — which runs both the original logic and the added decorator logic.

This reference swap happens only once, during decoration, meaning the function name now permanently points to the modified, enhanced version until changed again.

```python
def decorator(function):
    print(f"Original Function Object in Memory:\t {function}")
    def wrapper():
        return function()
    print(f"New Function Object in Memory:\t\t {wrapper}")
    return wrapper

@decorator
def say_hi():
    print("Hiiii Tamal !!!")

print(f"Updated Function Object in Memory:\t {say_hi}")
```

OUTPUT:
```bash
Original Function Object in Memory:	 <function say_hi at 0x00000191E19C2700>
New Function Object in Memory:		 <function decorator.<locals>.wrapper at 0x00000191E19C36A0>
Updated Function Object in Memory:	 <function decorator.<locals>.wrapper at 0x00000191E19C36A0>
```

### ✅ Nested Function Call or Function Call Chaining
When we call function `B()` within another function `A()`

- `A` just holds a pointer (reference) to call `B` when needed.
- `B`'s full code (object) stays separate in memory — nothing is "injected" into `A`'s object.

At runtime, when `A` executes and reaches `B()`, Python locates `B`'s object, runs it, and then returns control back to `A`.

### PENDING: Decorator with parameters `@decorator(show= True)`


# Others

### Python API request Handeling
We use request library to handle API request in python

```python
import requests

r= requests.get("https://api.freeapi.app/api/v1/public/randomusers/user/random")
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.text)
print(r.json())
type(r.text)
```

OUTPUT:
```bash
200
{'Server': 'nginx/1.18.0 (Ubuntu)', 'Date': 'Thu, 06 Mar 2025 19:41:23 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '1123', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'RateLimit-Limit': '5000', 'RateLimit-Remaining': '4977', 'RateLimit-Reset': '244', 'ETag': 'W/"463-FpvT2CVnFdGYijQU4URrxJGbJPU"', 'Set-Cookie': 'connect.sid=s%3AAwc9UaPWT17QokOT_G1pGEILplycpXPN.UUcuK9D2bp07wc2VeRWFipq97p2hZMFOuUuvfFM%2B16I; Path=/; HttpOnly'}
utf-8
{'statusCode': 200, 'data': {'gender': 'female', ... }'success': True}
{'statusCode': 200, 'data': {'gender': 'female', ... }'success': True}
```

```python
import requests
from mylib.runtime import runtime

@runtime            # my personal library containing decorator to evaluate performence
def fetch_random_user():
    url= "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response= requests.get(url)
    data= response.json()
    if data["success"] and "data" in data:
        user_data= data["data"]
        user_name= user_data["login"]["username"]
        user_country= user_data["location"]["country"]
        return user_name, user_country
    else:
        raise Exception("Failed to fetch user data")
# fetch_random_user()

def main():
    try:
        user_name, user_country= fetch_random_user()
        print(f"\nUsername: {user_name}, Country: {user_country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()
```

OUTPUT:
```bash
Runtime Report for 'fetch_random_user':
- Memory Used During Execution : 0.04 MB
- Memory Currently Occupied    : 0.005 MB
- Memory Freed After Execution : 0.036 MB
- Time Required for Execution  : 332.993 ms

Username: smallkoala605, Country: Mexico
```

### Python Virtual Environment (.venv)

- `pip install virtualenv`
- `python -m venv .venv` or `py -3.11 -m venv .venv`
- `Remove-Item -Recurse -Force .venv`
<!-- - `C:\msys64\ucrt64\bin`
- `%USERPROFILE%\AppData\Local\Microsoft\WindowsApps` -->
- `pip freeze > requirements.txt`
In `.gitignore` add *.venv to ignore virtual environment files.

In Windows, for multiple Python versions, the py launcher keeps track of Python versions from **Registry Editor (Win + R -> regedit)** at `Computer\HKEY_CURRENT_USER\Software\Python\PythonCore\{ 3.1x /3.13 / 3.12 / 3.11 ... sub-folder}` and `Computer\HKEY_LOCAL_MACHINE\Software\Python\PythonCore\{ 3.1x /3.13 / 3.12 / 3.11 ... sub-folder}`. To validate any changes in destination paths, we should update the **User/System PATH** and assign the new path in the **Registry Editor** as well.  

At this point, the existing pip within `Python31x\Scripts\` will have old paths, so we need to open CMD with Administrator privileges and run `py -3.1x -m pip install --upgrade --force-reinstall pip` for each modified version. Then validate.


- py -0
- where python
- which python
- python --version
- py --version
- where pip
- which pip
- pip --version

### Anaconda
Anaconda is a powerful tool used to manage libraries and dependencies, especially for complex environments. For example, when we run `pip install seaborn`, only the `seaborn` library is installed, and its dependencies, like `numpy`, may be missed. However, Anaconda ensures that all dependencies, including `numpy`, are automatically installed when you install `seaborn`.

It is generally preferred to use **`conda install`** to manage packages because it handles dependencies more efficiently. Mixing both `pip` and `conda` for installations can lead to conflicts and complications in managing the environment. Therefore, for a specific project, it's best to choose either `conda` or `pip` to manage dependencies, but not both.

We use **conda** or **Spyder** mainly for Data Science work. For production environments and backend frameworks like **Flask**, **FastAPI**, or **Django**, we generally use Python’s built-in `venv` (virtual environments).


#### Jupyter Note Book
Jupyter Notebooks (`.ipynb`) are widely used in data science for exploratory coding, visualization, and documentation. While the full form of `.ipynb` is "Interactive Python Notebook," it is also used in other languages like R and Julia.

Despite their advantages in data science, Jupyter Notebooks are not ideal for production use. They are relatively slow due to their JSON-based format for code and output. Furthermore, handling crashes and long-running processes in Jupyter Notebooks can be challenging. However, they remain popular for trial and error, prototyping, and building models, especially in data science.
