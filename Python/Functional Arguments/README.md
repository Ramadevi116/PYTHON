# Formal and actual Arguments.

## Formal arguments.

**When we are defining a functon,we will pass some parameters.These parameters are useful to recive values from outside of function.They are called ```formal arguments```.**

## Actual arguments.

**When we call the funtion,we should pass data or values to the function.These values are called ```actual arguments```.**

```python
def name(str1,str2):  # str1,str2 are formal arguments...
    print(str1,"and",str2,"Both are frnds")
# call the function...
n1="Ramadevi"
n2="Rupesh"
name(n1,n2)     # n1,n2 are actual arguments...
```

## acutal arguments are clasiffied into 4 types:

* Positional arguments.

* Keyword arguments.

* Default arguments.

* Variable length arguments.

## Positional arguments:

**These are the argumnets passed the function in correct positional order.**

**Count of Formal arguments is equal to count of actual arguments.**

```python
def Books(B1,B2):
    print(B1,B2)
Books("python","java")
```

## Keyword arguments:

**This arguments that identify the paramenters by there names.**

```python
def BOOK_PAGE(book="python",pages="200"):
```

## Default arguments:

**In function defination we can mention some default values to the function.**

```python
def Name_age(name,age=20): 
```

## Variable length arguments:

**Variable length arguments is used to get more than one input.It is denoted by ```*```.**

```python
def persons(*names): *names can take zero or more values...
```

## keyword variable length arguments:

**It can accept any number of values that provides in the format of keys and values.It is denoted by ```**```.**

```python
def name_age(**kwargs): 
```

# Local and Global Varables:

**When we declare a variable inside a function,it becomes a ```local veriable```.**

**When we declare a variable outside a function,it becomes a ```gobal variable```.**

```python
a=10 # Global variable...
def mul():
    a=20 # local variable...
    b=2
    mul=a*b
    print(mul)
    print(a)    # Display local variable..
mul()
print(a) # Display Global variable...
```
## Global keyword:

**If the user want to use Global variable inside local variable User can use keyword ```global```.**

```python
a=10
def fun():
    global a
    print(a)
fun()
```



