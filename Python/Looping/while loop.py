# looping....
# To display name b/w the range x,y...

# while loop:
# user inputs
Name=input("Enter your name:")
x=int(input("start:"))
y=int(input("end:"))
# indexing variable to assign a starting point/value...
i=x
while(i<=y):  # to check the condition true/false...
    print(Name) # condition true Print statement..
    i+=1      # Incrementing value by 1...
z=y-x+1
print("My Name is printed",z,"times")

            # or

# Getting inputs in one expression by using split....
Name,start,end=input("Enter the name and start point,end point:").split(',')  # inputs:Rama,2,6
count=x
while(count>=x and count<=y): # and operator mix two conditions...
    print(Name)
# incrementing count by 1...
    count+=1
z=y-x+1
print("My Name is printed",z,"times")

# infinite loop...
# always the condition is true...
i=1
while(i>=10):
    print("Ramadevi") 
    # Here the increment is not done...so the condition is true for all time...
    # infinite loop is drawback ...


