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