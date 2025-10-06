# Functions

## Overview

Functions are blocks of code defined after a ```def``` statement,
and they can be executed from somewhere else.

There are two steps when using functions:
- Defining them, with the ```def``` statement. This part tells the computer
what the function does
- Calling them, with the ```()``` operator. This executes the function, 
it runs all operations inside the function

> [!WARNING]
> 
> Defining a function doesn't execute it.
> 
> It is common to define a function but to forget calling it,
> then complaining that nothing happens

```python
# Defining the function
def simple_function():
    print("Who's Rem ?")

# Calling the function
simple_function() # -> Will print in the terminal: "Who's Rem ?"
```

## Arguments

Functions can have arguments, which are defined within the ```()```
when defining them.

Arguments are variables which will be different each time you call the function
(They can have the same value, but the variable being different means they will not retain
their value from a previous execution).

```python
def simple_function_with_args(a, b):
    c = a + b
    print(f"c = {c}")

simple_function_with_args(3, 20)    # -> Will print: "23"
simple_function_with_args(12, 87)   # -> Will print: "99"
```

You can also give those arguments default values with the ```=``` operator,
but an argument must have a default value if the preceding argument does.

```python
# This works
def simple_function_with_args(a, b = 2):
    c = a + b
    print(f"c = {c}")

simple_function_with_args(3)        # -> Will print: "5"
simple_function_with_args(3, 20)    # -> Will print: "23"
simple_function_with_args(12)       # -> Will print: "14"
```

```python
# This wouldn't work, because 'a' has a default value but 'b' doesn't
def simple_function_with_args(a = 2, b):
    c = a + b
    print(f"c = {c}")

# Below code can't be reached, the program crashes at the function definition
```

## Return values

Functions can have a ```return``` statement.

The return statement serves two purposes:
- It stops the function
- It allows you to return values (see the 
["Variable range"](VARIABLE_RANGE.md) documentation for more details)

Return statements have a type:
- An empty return statement has the "None" type
- A return statement with an int has the "int" type
- A return statement with a list has the "list" type
- etc ...

It is heavily advised for all return statements of a function to have the same type.

```python
def empty_return_function(do_execute):
    if not do_execute:
        return 
    print("Executing")

def simple_return_statement_function(a, b):
    sum_value = a + b
    return sum_value

def tuple_return_statement_function(a, b):
    value_1 = a // b
    value_2 = a % b
    return value_1, value_2


empty_return_function(True)     # -> Will print: "Executing"
empty_return_function(False)    # -> Won't print anything

print(simple_return_statement_function(1, 2)) # -> Will print: "3"

print(tuple_return_statement_function(7, 3)) # -> Will print: "2, 1"
```

## Recursivity

Functions can call other functions.

```python
def function_1():
    print("Executing function_1")

def function_2(n):
    for _ in range(n):
        function_1()


function_2(10) # -> Will print "Executing function_1" 10 times
```

> [!NOTE]
> 
> There is a rare case where functions infinitely calling other functions can cause an issue.
> 
> This issue is called "Stack overflow", and is explained in the
[loops](LOOPS.md) documentation

## Type hints

You can add type hints to your functions.

Those are purely decorative, they change nothing to the functions behaviour
and only serve to make your code easier to understand.

```python
def empty_return_function(do_execute: bool) -> None:
    if not do_execute:
        return 
    print("Executing")

def simple_return_statement_function(a: int | float, b: int | float) -> int | float:
    sum_value = a + b
    return sum_value

def tuple_return_statement_function(a: int, b: int) -> tuple[int, int]:
    value_1 = a // b
    value_2 = a % b
    return value_1, value_2

def list_return_statement_function() -> list:
    return []

def dict_return_statement_function() -> dict:
    return {}
```




