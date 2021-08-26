# Functional Arguments...
# set an alarm...

# positional argument...with arguments without return type...
def alarm(time,Noon):
    if(time>=1 and time<=12):
        if(Noon=="AM" or Noon=="am" or Noon=="Am"):
            print("Good morning Rama","Now time is",'{: .2f}'.format(time),Noon,"Alert....⏰⏰")
        elif(time>=1 and time<=4):
            if(Noon=="PM" or Noon=="pm" or Noon=="Pm"):
                print("Good Afternoon Rama","Now time is",'{: .2f}'.format(time),Noon,"Alert..⏰⏰")
        elif(time>=4 and time<=7):
            if(Noon=="PM" or Noon=="pm" or Noon=="Pm"):
                print("Good Evening Rama","Now time is"'{: .2f}'.format(time),Noon,"Alert..⏰⏰")
        else:
            print("Good night rama u can sleep ....Sweet dreams...Take care...😴😴")
set_a_time=float(input("Enter Your alert⏰ time:"))
set_a_Noon=input("Enter AM or PM:")
print(alarm(set_a_time,set_a_Noon))

# Keyword argument...Nested function...with arguments...with return type...
def Shapes_Colours(shape="Heart",colour="Red"):
    def Msg():
        if(shape=="Heart" and colour=="Red"):
            return "Structure is : "
        else:
            return "Check your shape and colour"
    msg=Msg() + "💘💘"
    return msg
My_Favarate=Shapes_Colours()
print(My_Favarate)

# Default arguments...with argument...with return type...
def Dress_Colours(colour,dress="jeans"):
    def Msg():
        if(colour=="blue"):
            return "I Love "
        elif(colour=="black"):
            return "I will try once this "
        else:
            return "Change the colour...I hate "
    msg=Msg() + colour + " jeans"
    return msg
colour=input("Select u r colour:")
My_Favorite=Dress_Colours(colour)
print(My_Favorite)

# Variable length arguments...
# We can passmore than one input...
def Cute(*Smile):
    print("Always keepsmiling....🤗")
    print(Smile)
Cute("Rama","Rupesh")
Cute("Rama","Rupesh","Jyothi")
Cute("Rama","Akshaya","Bhavitha","Jaya","Keerthi")
print("Never stop smiling....😛")
