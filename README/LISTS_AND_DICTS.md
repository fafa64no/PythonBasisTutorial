# Lists and dictionaries

Lists and dictionaries are both variable types which can contain other variables.

# Lists

## Basics

Lists are defined with ```[]```, they can contain different elements of any types.

```python
empty_list = []
another_empty_list: list # Less frequently used

simple_list = [34, 78, 97]

weird_but_possible_list = [
    23,
    [87, 45],
    "Madoka",
    43.0
]
```

## Accessing elements

You can access an element of a list through its index, with the ```[]``` operator.

The first index is 0.

```python
example_list = [34, 78, 97]

print(example_list[0]) # -> Will print the first element of list_2, in this case 34
```

If you want to access all elements of the list (in order), you can do it with a ```for``` loop.

```python
example_list = [34, 78, 97]

for element in example_list:
    print(element) 

# -> Will print:
# 34
# 78
# 97
```

## Additional stuff

Some important stuff to know:
- You can get the length of a list with the ```len``` function.
- You can generate some basic lists with the ```range``` function.
- You can easily convert a string to a list

```python
example_list = [34, 78, 97]

print(len(example_list)) # -> Will print "3"
```

```python
for i in range(4):
    print(i)

# Equivalent to:
for i in [0, 1, 2, 3]:
    print(i)
```

```python
example_str = "Rem"

example_list = list(example_str) # -> Is equal to ['R', 'e', 'm']
```

Example of using range to access multiple lists at once:
```python
list_1 = [34, 78, 97]
list_2 = [11, 23, 53]
list_3 = [52, 24, 80]

for i in range(3):
    value = list_1[i] + list_2[i] + list_3[i]
    print(value)
```

# Dictionaries 

## Basics

Dictionaries are defined with ```{}```, they can contain different pairs.

Each pair consists of:
- A "key" of any type
- A "value" of any type

Each key can only exist once in the same dictionary, 
while there can be as many times the same value as you want.

All keys must be the same type.

```python
empty_dict = {}
another_empty_dict: dict  # Less frequently used

simple_dict = {
    "euro": 12.0,
    "dollar": 11.9,
    "gringo": 666.666,
}

dict_containing_dicts = {
    "Rem" : {
        "age" : 12,
        "credit card number" : 89329487329874,
        "exists" : False,
        "diseases" : [
            "cholera",
            "ebola",
            "ginger"
        ],
    },
    "Dio" : {
        "age" : 2912,
        "credit card number" : 88755590629874,
        "exists" : True,
        "diseases" : [
            "tractopelliose",
        ],
    },
}

weird_but_possible_dict = {
    "Gregory" : {
        "age" : 12,
        "life expectancy" : -14,
    },
    "Tomiko" : [{3 : 4}, {"why" : "because"}],
}
```

## Accessing elements

You can access an element of a dictionary through a key, with the ```[]``` operator.

```python
example_dict = {
    "euro": 12.0,
    "dollar": 11.9,
    "gringo": 666.666,
}

print(example_dict["euro"]) # -> Will print "12.0"
```

If not sure whether the key exists, you can check its existence with the ```in``` operator.

```python
example_dict = {
    "euro": 12.0,
    "dollar": 11.9,
    "gringo": 666.666,
}

example_key = "tartomiel"

if example_key in example_dict:
    print("Key exists")
else:
    print("Key doesn't exists")
```

There's also the possibility to access all keys or all pairs of a dictionary.

```python
example_dict = {
    "euro": 12.0,
    "dollar": 11.9,
    "gringo": 666.666,
}

# Print all keys
for key in example_dict.keys():
    print(f"key is {key}")

# Print all pairs
for key, value in example_dict.items():
    print(f"key is {key}, value is {value}")
```













