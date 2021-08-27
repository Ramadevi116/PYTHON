## Passing a group of elements to a function...

**To pass a group of elements like numbers or string,we can accept them into a list and then pass list to the function.**

```python
list=[int(x) for x in input().split()]  # for numbers...
str=[x for x in input().split]          # for strings...
```
## Recursive function:

**A function that calls itself is known as ```recursive function```.**

```python
fact(n)=n*fact(n-1)
```

## Anonymous functions or lambdas function:

**A function with out function name is called ```Anonymous function```.**

```python
lambda argument_list : Expression
lambda x : x+x
```
## using lambdas with filter() function:

**The filter() function useful to filter out the elements of a sequence deponding on the result of a function.**

```python
filter(function,sequence)
```

## using lambdas with map() function:

**The map() function is similar to filter() function but it acts an each element of the sequence.**

```python
map(function,sequence)
```

## Using lambdas with reduce() function:

**The reduce() function reduces a sequence of elements to a single value by processing the elements accordind to a function supplied.**

```python
reduce(function,sequence)
```

## function decorators:

**A decorators is a function that accepts a function as parameter and returns a function.A decorators takes the results of the function ,modifie the result and returns it.Thus decoraors are useful to perform some additional processing required by a function.**

```python
def fun(game):
    def inner():
        msg=game()
        return msg+" Hi! How are u?"
    return inner
def name():
    return "rama"
result_fun=fun(name)
print(result_fun())
```
**To apply the decorator to any function,we can use the ```@``` symbol and decorator name just above the function definition.**

```python
def fun(game):
    def inner():
        msg=game()
        return msg+" Hi! How are u?"
    return inner
@fun
def name():
    return "rama"
print(name())
```



