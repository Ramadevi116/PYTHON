# Oops(Object oriented programming system):

**Python use classes and objects in their programs are called Object Oriented programming language.**

**Some other languages they use the main program is composed of several procedures and functions this is known as Procedures oriented programming language.**

**A class is a module which itself contains data and methods to achieve the task.**

## features of OOPs:

* classes and objects.

* Encapsulation.

* Abstraction.

* Inheritance.

* Polymorphism.

## classes and objects:

**Everything in this world is an object.ex:table,phone,ball etc...**

**Something doesnot really exists, then it is not an object.exp:our thoughts,immagination etc...**

**Every object has some behaviour(attributes(variables) and actions(Methods)).s0 an object contains variables and methods.**

**Method:A function written inside a class.**

**A class is a group name and does not exist physically,but object exits physically.**

**An object does not exit without a class.but a class can exit without any object.**

```python
class Rooms:
    type="4 in 1"
    cost=92000
    def fee(self):
        print(self.type)
        print(self.cost)
r1=Rooms()
r1.fee()
```

## Encapsulation:

**Encapsulation is a mechanism where the data(Variables) and the code(Methods) that acts on the data will bind together.Exp:class**

```python
# a class is an example for encapsulation.
class Rooms:
    # to declare and initialize the variables.
    def __init__(self):
        self.type="4 in 1"
        self.cost=92000
    # To display the details.
    def fee(self):
        print(self.type)
        print(self.cost)
r1=Rooms()
r1.fee()
```

## Abstraction:

**There may be a lot of data, a class contains and the user does not need the entire data.The user requires only some part of the available data.In this case we can hide the unnecessary data and expose only required data.This is called abstraction.**

**In python everything written in the class will comes under public.**

**If we start with double underscore before variable this indicates as private variable.**

```python
class Rooms:
    def __init__(self):
        self.__type="4 in 1"
        self.cost=92000
    def fee(self):
        print(self.__type) # or print(self._Rooms__type)
        print(self.cost)
r1=Rooms()
r1.fee()
```

## Inheritance:

**Creating new classes from existing classes,so that the new classes will acquire allthe features of the existing classes is called Inhertance.**

**Ex:Parents and Chindren.**

```python
class A:
    type="4 in 1"
    cost=92000
    def m1(self):
        print(self.type)
        print(self.cost)
class B(A):
    TimePeriod="1 year"
    def m2(self):
        print(self.TimePeriod)
X=B()
X.m2()
X.m1()
```

## Polymorphism:

**Poly means many.**

**morphos means forms.**

**Polymorphism represents the ability to assume several different forms.**

**Ex:adding......We can add integers and concatenation two strings.**

```python
def add(a,b):
        print(a+b)
add(2,8)
add("Hi"," Rama")
```


















