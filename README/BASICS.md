# Basics

## Variable types

### Overview

The basic variable types in python are:
- int (integer): a number like 1, 2, -12, ... No decimals
- float: a number like 1.2, 3.14, -4.5, ... It can have decimals
- bool (boolean): a value which can be either "True" or "False"
- str (string): a chain of character like "Tractopelliose"
- list: a list (see [LISTS_AND_DICTS](LISTS_AND_DICTS.md))
- dict: a dictionary (see [LISTS_AND_DICTS](LISTS_AND_DICTS.md))

You can get the type of variable with the ```type``` function.

```python
a = 1
b = 1.0
c = True
d = "Gringo"
e = []
f = {}

print(type(a)) # -> Will print 'int'
print(type(b)) # -> Will print 'float'
print(type(c)) # -> Will print 'bool'
print(type(d)) # -> Will print 'str'
print(type(e)) # -> Will print 'list'
print(type(f)) # -> Will print 'dict'
```

### Cast

If a variable allows it, you can cast it to another type.

```python
gringo_str = "Gringo"

gringo_list = list(gringo_str)

print(type(gringo_list)) # -> Will print "list"
```

### Type hints

Instead of giving a default value to a variable, you can just tell it its type.

```python
a: int
b: float
c: bool
d: str
e: list
f: dict
```

## Operators

### Basic operations

Integers and floats support basic mathematical operations.

```python
a = 1 + 2 # Addition
b = 3 - 1 # Substraction
c = 3 * 2 # Multiplication
d = 7 / 3 # Division

e = 5 ** 2 # Power, in this case it is 5 squared (5²)
```

These operations return floats if there's any float in them,
or return integers if there's only integers in them.

### Euclidian division

Euclidian division is done with integers, and return integers.

You can get either the result or the remainder of the division with
the basic python operators.

```python
a = 7
b = 3

# 7 = 3 * 2 + 1
result = a // b     # Equals 2
remainder = a % b   # Equals 1
```

### Conditions

Conditions are operators that convert types to booleans, and are
usually used within ```if``` statements.

```python
a = 1
b = 1

c = []

d = True
e = True

# With anything
equals_cond = (a == b)
different_cond = (a != b)

# With numbers
inf_cond = (a < b)
sup_cond = (a > b)
inf_or_equals_cond = (a <= b)
sup_or_equals_cond = (a >= b)

# With booleans
not_cond = (not d )
or_cond = (d or e)
and_cond = (d and e)

# With lists or dictionaries
inside_list_cond = (a in c)
not_inside_list_cond = (a not in c)

# Use case example
if a > b:
    print("a is greater than b")
```

### Concatenation

Concatenation can be done between two lists or two strings, and it allows you to combine two lists
into a bigger one.

```python
list_1 = [1, 3]
list_2 = [2, 4]

list_concatenated = list_1 + list_2

print(list_concatenated) # -> Will print [1, 3, 2, 4]
```






