# Functions.
## Defining a function:

**If the code execute bunch of times or n number of times then the function is used to short the code.**

**we can define a function using the key word ```def``` followed by function name.After the function we should write the parentheses``` () ``` which may contain parameters.**

**After parentheses ``` : ``` colon represents the beginning of the function body.**

* syntax of function defination:

```python
def functionname(p1,p2,p3, .......): # p parameters...
    """function docstring."""
    function statements
```

* Exp:

```python
def add(a,b):                   # def indicates starting of function defination.
    """Sum of two numbers"""
    c=a+b
    print(c)
```

## calling a function:

**After defining a function ,it runs only when we call it.So,the next step is to call the function using its name.**

```python
add(20,50)  # passing arguments...
```

**We can call a function again and again it is know as reuseable code.**

```python
def add(a,b):                   
    """Sum of two numbers"""
    c=a+b
    print(c)
add(10,30)
add(12343546,8723649)
add(12.3,34.9)
.
.
.
etc...
```

## Return statement:

**We can return result or output of the function.**

* Exp:

```python
def add(a,b):                   
    """Sum of two numbers"""
    return a+b  # return result...
res=add(1,5)    # Result returned to the var res...
print(res)
```

## Returning Multiple values from a function.

**We can return Multiple results or Multiple outputs of the function.**

* Exp:

```python
def cal(a,b):
    """Calculate add,sub,mul,did...."""
    add=a+b
    sub=a-b
    mul=a*b
    did=a/b
    return add,sub,mul,did  # Returned multiple results...
res=cal(20,10)
print(res)
```

## Nested function:

**Function inside other function**

* syntax for Nested function:

```python
# function defination...
def Functionname1(parameters):
    def functionname2(parameters):
        statements
        return statement/print statement
    statements    
    return statement/print statement
# function call...
print(functionname1(arguments))
```

* Exp:

```python
def Name(str):
    def msg():
        return ' helo! How are u?'
    result=str+msg()
    return result
print(Name("Ramadevi"))
```

## functions are first class objects:

* It is possible to assign a function to the variable.

* It is possible to define one function inside another function.

* It is possible to pass function as parameter to another function.

* It is possible that a function can return another function.

