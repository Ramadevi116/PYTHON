# classes and objects...
class mobile:
	def call_make(self):
		print("Someone calling...")
R=mobile()
R.call_make()

#-----------------------------------------------------------------------------------------------------------------------

# Encapsulation...
class mobile:
        def __init__(self):
		        self.msg="Someone calling..."
        def call_make(self):
                print(self.msg)
R=mobile()
R.call_make()
#----------------------------------------------------------------------------------------------------------------------
# Abstraction:
class mobile:
        def __init__(self):
                self.__NewMsg="Many times someone is calling..."
                self.msg="Someone calling..."
        def call_make(self):
                print(self.msg)
                print(self.__NewMsg)
R=mobile()
R.call_make()
#-----------------------------------------------------------------------------------------------------------------------
# Inheritance:
# Single Inheritance:
class mobile:
	def call_make(self):
		print("Someone calling...")

class Samsung(mobile):
	def design(self):
		print("screen is better")

s1=Samsung()
s1.design()
s1.call_make()
#------------------------------------------------------------------------------------------------------------------------
# Multi level Inheritance:
class mobile:
	def call_make(self):
		print("Someone calling...")

class Samsung(mobile):
	def design(self):
		print("screen is better")

		
class SamsungGalaxy(Samsung):
	def smartfeatures(self):
		print("This phone has smart features.A long-lasting battery.")

		
sg1=SamsungGalaxy()
sg1.smartfeatures()
sg1.design()
sg1.call_make()
#------------------------------------------------------------------------------------------------------------------------
# Multiple Inheritance:
class mobile:
	def call_make(self):
		print("Someone calling...")
	def feature(self):
		print("mobile should have calling features")

		
class Samsung(mobile):
	def design(self):
		print("screen is better")
	def feature(self):
		print("mobile should have Plenty of storage space and smart features")

		
class SamsungGalaxy(Samsung,mobile):
	def smartfeatures(self):
		print("This phone has smart features")

		
sg1=SamsungGalaxy()
sg1.feature()
#------------------------------------------------------------------------------------------------------------------------
#Polymorphism.
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("My name is",self.name,".I am",self.age, "years old.")

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
       print("My name is",self.name,".I am",self.age, "years old.")


p1 = Person1("Rama", 14)
p2 = Person2("Bhavitha", 15)

for animal in (p1, p2):
    animal.info()
    