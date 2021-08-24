# Flow control:

### input statement:

> Name=input("Enter Your Name:")

**For particular data type like int,float,etc.. Input will be:**

> Age=int(input("Enter Your Age:"))

> Height=float(input("Enter Your Height:"))

## 1) Conditional Statement:

**It performs different actions,based on that action it will change the flow of execution**

## Types of conditional statement:

* if [Conditional statement]

* if-else [Alternative conditional statement]

* if-elif-else [Chain conditional statement]

* Nested if


## if Statement:

**This statement is used to execute one or more statements depending whether a codition is true or false**

* Syntax of if statement: 

''' python
 if condition:
    statements
'''
* exp:

''' python
  a=input("Entre Your Name:")
  if(a=="Ramadevi"):
     print("Hi Ramadevi")
'''

## if-else Statement:

**The if-else statement execute a group of statements when a condition is true otherwise, it will execute another group of statements.**

* syntax of if-else: 

'''python
 if condition1:
    statement1
 else:
    statement2
'''

* exp: 

'''python
 a=input("Entre Your Name:")
 if(a=="Ramadevi"):
     print("Hi Ramadevi")
 else:
     print("Unknown Person")
'''

## if-elif-else statement:

**To check multiple conditions and execute the statements depending on those conditions**

**If the previous condition was not true then it will check the elif conditions....till the condition true it goes on...then stops.**

* syntax for if-elif-else : 

'''python
if condition1:
    statement1
elif condition2:
    statemnet2
elif condition3:
    statemnet3
else:
    statemnet4
'''

* exp:

'''python
a=input("Entre Your Name:")
if(a=="Ramadevi"):
    print("Hi Ramadevi")
elif(a=="Akshaya"):
    print("Hi Akshaya")
elif(a=="Jyothi"):
    print("Hi Jyothi")
else:
    print("Unknown Person")
'''

## Nested if Statement:

**if statement inside if statement**

* Syntax for Nested if statement.

'''python
if condition1:
    if condition2:
        statement1
'''

* exp:

'''python
a=input("Entre Your Name:")
b=input("Entre Your Name:")
if(a=="Ramadevi"):
    if(b=="Akshaya"):
        print("Hi Ramadevi....Helo Akshaya")
'''