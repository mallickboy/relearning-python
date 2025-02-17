# relearning-python
After 3 years of experience in python revisioning core fundamentals of Python



## Internal Working ( 13th February 2025 )

#### Copy, Reference Coutn, Slice

## Numbers in Depth

## String in Python

## List in Python

#### List Slicing
```
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
```
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
```
    >>> [ x*x for x in range(1,6) ] 
    [1, 4, 9, 16, 25]
```

## Dictionary in Python

```
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
```
    >>> chai.pop("ginger")
    'zesty'
    >>> chai
    {'masala': 'spicy', 'green': 'Fresh'}
```

#### Pop last entry of dict & delete operation
```
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
```
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
```
    >>> square={x:x*x for x in range(1,5)}
    >>> square
    {1: 1, 2: 4, 3: 9, 4: 16}
    >>> square.clear()
    >>> square
    {}
```
#### Creating new dict
```
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
```
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
```
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
```
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