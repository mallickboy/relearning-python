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
