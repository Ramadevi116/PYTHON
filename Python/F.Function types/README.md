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

**A function with out name is called ```Anonymous function```.**

```python
lambda argument_list : Expression
lambda x : x+x
```


