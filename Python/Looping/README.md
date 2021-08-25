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

## Break statements:

**The break statement can be used inside a for loop or while loop to come out of the loop.**

**When 'break' is executed,it jumps out of the loop to process the next statement.**

```python
i=1
while(i>10):
    print("rama")
    i+=1
    if(i==5):
        break
```

## Continue statement:

**It is used in a loop to go back to the beginning of the loop.**

**If continue is executed,the next repetition will start.**

```python
x=0
while(x<10):
    x+=1
    if(x>5):
        continue
    print(x)
```

## Pass statement:

**pass statement does not do any thing.it is used with 'if' statement or inside a loop to represent no operation.**

```python
list=[1,2,3,4,5,6,7,8,9]
for i in list:
    if(i>5):
        pass
    else:
        print(i)
```




