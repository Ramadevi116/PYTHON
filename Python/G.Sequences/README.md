# Sequences:

* String

* List

* Tuple

* Dictionary

* Set

## string:[Immutable]

**In string we are assigning a group of characters to a variable.The Group of characters is enclosed inside single quotes or double quotes.**

```python
jyothi='Hi rama! How are u?'
rama="Hi! I am fine..."
```
**When we want to represent a string with several lines we will use triple or triple double quotes.**

```python
Msg='''Never quit. It is the easiest cop-out in the world. Set a goal and don’t quit until you attain it. When you do attain it, set another goal, and don’t quit until you reach it. Never quit.'''

Msg2="""True success is all about working towards meaningful goals and dreams.Achieving our goals and dreams is fantastic but that's not the most important thing about setting goals. The most important thing is the type person that we become along the way."""
```

### Length of the string:

**TO know the length of the string.we can use the ```len()``` function.**

```python
Name="Achalakuchala rajaroja padmalela harijatha vendikonda ragabala swapna setha kumari Ramadevi"
length_of_Name=len(Name)
print(length_of_Name)
```

### Indexing:

**Represents the position number.```str[]```index value starts from 0 in positive index and -1 from negative index**

```python
Name="Achalakuchala rajaroja padmalela harijatha vendikonda ragabala swapna setha kumari Ramadevi"
print(Name[2])  # refers to third element of string...
print(Name[-2]) # refers to second element from last...
```
### Slicing:

**A part or piece of a string.```stringName[start:stop:stepsize]```.

* str[::] -> String from 0th to last element.

```python
Name="Achalakuchala rajaroja padmalela harijatha vendikonda ragabala swapna setha kumari Ramadevi"
print(Name[14:33:1]) # o/p:rajaroja padmalela
print(Name[14:33:2]) #o/p:rjrj amll
print(Name[-14:-33:-1]) #o/p:uk ahtes anpaws ala
```

### Repeatition:

**It is denoted by "*" symbol and it is useful to repeat the string several times.**

```python
Name="Achalakuchala rajaroja padmalela harijatha vendikonda ragabala swapna setha kumari Ramadevi"
print(Name*2)
```

### Concatenation:

**It is denoted by "+".Addition of strings**

```python
str1="Rama"
str2="Devi"
print(str1+str2)
```

### Checking Membership:

**We can check if a string is a member of another string or not using ```in``` or ```not in``` operator.**

```python
Name="Achalakuchala rajaroja padmalela harijatha vendikonda ragabala swapna setha kumari Ramadevi"
Name2="vendikonda"
Check=Name2 in Name
print(Check) #o/p:True
```

### Comparing strings.

### Removing spaces from the string.

**```strname.strip()```.This methods do not remove spaces from middle of the string.It removes Only unnecessary spaces from starting and ending.**

* strname.lstrip -> remove spaces at left side of string... 

* strname.rstrip -> remove spaces at right side of string...

### Finding substring.

**find(),rfind(),index(),rindex() Methods are useful to locate substrings.**

```python
Mainstring.find(substring,Beginning,ending)
```

### Counting substrings in a string.

```python
Stringname.count(substring)
stringname.count(substring,beginning,ending) 
```

### Replacing a string with another string.

```python
stringname.replace(old,new)
```

### splitting and joining strings.

```python
str.split(',')
```
### Changing case of string.

```python
str.upper()
str.lower()
str.swapcase()
str.title()
```

### Checking starting and ending of the string.

```python
str.startswith(substring)
str.endswith(substring)
```

### Formatting the string.

```python
{}.format(Stringname)
```

# List[Mutable]

**Group of elements or items known as list and it is stored in square braces[].**

* Updating the elements.->list.append(New element or item)

### operations:

* Concantenation

* Repetition

* Membership

* Methods:

    * sum()

    * index()

    * append()

    * insert()

    * copy()

    * extend()

    * count()

    * remove()

    * pop()

    * sort()

    * reverse()

    * clear()

## List comprehensions:

**List comprehensions is a single statement that performs code.**

```python
list=[x*x for i in range(1,10)]
print(list)
````

## Tuple[immutable].

**Tuple values is arranged between parentheses []**

* methods:
    
    * len()

    * min()

    * max()

    * count()

    * index()

    * sorted()

**Inserting elements in a tuple**

**Modifying elements of a tuple**

**Deleting elements from a tuple**

# Set[Mutable].

**Written set as a comma separated between  curly brackets.{}**

### Methods:

* add()

* remove()

* clear()

* pop()

* isdisjoint()

* issubset()

* issuperset()

* Union()==A|B

* Intersection()==A&B

* Difference()==A-B

* Symmetric _difference()==A^B

# Dictionary/dict.[mutable]

**hold only single value as an element, Dictionary holds key:value pair.b/w {}**

### Methods:

* clear()

* copy()

* fromkeys()

* get()

* items()

* keys()

* values()

* updates()

* pop()

* setdefaults()

### using loops,functions in dict.

### Converting list,strings into dict.

### passing dict to functions.















