# Looping:

**A loop is used for executing a block of statements repeatedly until a particular condition is satisfied**

## Types of looping:

* while loop

* for loop

* infinite loop

* for/while loop using else statements

* Nested for loop

## while loop:

**while loop is useful to execute a group of statements several times repeatedly depending on whether a condition is true or false.**

* syntax of while loop:

```python
while condition:
    statements
```

* Exp:

```python
n=int(input("Enter a range:"))
i=0                      # Indexing variable
while(i<n):              # condition
    print("Ramadevi")
    i+=1                 # increment
```

## For loop:

**for loop is useful to execute a group of statements several times repeatedly depending upon the number of elements in a sequence**

* syntax of for loop:

```python
for var in sequence/range:
    statements
```

* exp:

```python
str="Ramadevi"
for i in str:
    print(i)
for i in range(4):
    print("Ramadevi")
```

## infinite loop:

**Infinite loop is continuous repetitive conditional loop**

**Infinite loops are drawbacks in a program**

* Syntax of infinite loop:

```python
while(#Condition true):
    statements
```

* exp:

```python
while(True):
    print("Ramadevi")
        # or
i=0
while(i<10):
    print("Rama")
# Here the condition is true always...   
```

## Nested loop:

**One loop inside another loop.**

* exp:

```python
for i in range(4):
    for j in range(2):
        print(i,j)
```

## for with else / While with else:

**Along with loop statements Else statements also executed.**

* syntax :

```python
# for loop
for i in range(count):
    statements
else:
    statements
# while loop
while(condition):
    statements
else:
    statements
```

* exp:

```python
str="Ramsdevi"
for i in str:
    print(i)
else:
    print(str)
    # or
str="Ramadevi"
for i in range str:
    print(i)
print(str)
```



