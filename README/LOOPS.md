# Loops

Loops are means of executing a code block multiple times, 
without writing multiple times the same code.

The three ways of creating a loop are:
- ```for``` loop
- ```while``` loop
- Recursive functions

## For loop

Those are the most common loops, usually used with the range function.

They take a list as input, and offer you to name a variable corresponding 
to which element you are currently reading.

```python
for i in range(4):
    print(f"i currently is '{i}'")

# -> Will print:
# i currently is '0'
# i currently is '1'
# i currently is '2'
# i currently is '3'

# Without the range function
for x in [0, 1, 2, 3]:
    print(f"x = {x}")
```

## While loops

These loops take a condition as argument, and will continue to loop while
the condition is true. 

This means that they can loop forever.

```python
# Finite loop example
x = 1
while x < 1000:
    x = x * 2
    print(f"x = {x}")
    
# Infinite loop example
while True:
    print("Executing stuff ...")
```

## Recursive functions

Those are slightly more complex, and less likely to be used in business related applications.

They work by having a function calling itself, and can cause the program to crash
if there's too much recursion.

```python
def recursive_function_example(iteration = 0):
    print(f"Iteration {iteration}: This will eventually crash")
    recursive_function_example(iteration + 1)

recursive_function_example() # Will print a lot of stuff, then crash
```







