# Variable range

## Overview

Variables have a range, which means they cannot be accessed from anywhere.

The range depends on which block contains the variables.

The key points to understand are:
- A block is preceded by a statement suck as 
```if```, ```for```, ```def```, ... Anything which requires indentation after it
- Everything inside a block has the same indentation
- A block can contain blocks
- When exiting a block, all variables created inside that block are deleted
- A block can access its own variables and the variables of the parent block
- Variables which aren't in any block are "global variables", 
they can be accessed from anywhere
- Non global variables are called "local variables"

```python
a = 1                   # 'a' defined as global variable

if True:                # Start of block 1
    b = 1               # 'b' defined in block 1
    if True:            # Start of block 2, with block 1 as parent
        c = 1           # 'c' defined in block 2
        b += c          # variable from parent block accessed from block 2
    # End of block 2
    # -> 'c' gets deleted here
    a += b              # Global variable accessed from block 1
# End of block 1
# -> 'b' gets deleted here

# 'a' never gets deleted because it is global
```

Global variables are easy to work with, 
but they might interfere with other parts of your program due to them never getting destroyed.

A common example is two different exercises using the same variable name.
If theses two exercises aren't in different blocks, they will use the same variable
and might interfere with each other.

## Transferring variables from a block to a parent block

As you've understood, local variables are deleted at the end of their block, 
which means you often cannot directly get values computed in block from outside that block.

If you want to get local variables from outside their block, the common practices are:
- Use the ```return``` statement in the case of functions
- Define a variable in the parent block and use it 

```python
# When dealing with functions
def example_function():
    a = 1
    return a
# 'a' is deleted at the end of the function,
# but its value is returned beforehand

# By storing the returned value in a new variable, it effectively is like
# if 'a' didn't get deleted
a = example_function()
```

```python
# When dealing with other block types
a = 0   # By defining 'a' outside the 'for' block, it will still exist when exiting that block

for _ in range(55):
    a += 1

# 'a' still exists
print(f"a = {a}")
```



