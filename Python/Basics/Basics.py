#print function.
print("Helo Rama")
#Variables.
a=10 
num=123
#Here a,num are variables.
#It can be single or multiple variables.
a,num=10,123
# Data Types:
#Numbers.[Immutable]
#integer
a=10
#Float
f=2.5
#Boolean
#complex
c=2+3j
#To check the type of a value.
type(a) #int
type(f) #Float
type(c) #Complex
print(a)
print(f)
#del use for delete the value.
del a
#strings:[Immutable]
Name="Ramadevi"
Dept="CSE"
Clg="Saveetha"
print(Name)
print(Dept)
print(Clg)
#Indexing
print(Name[0]) #Positive indexing
print(Name[-5]) #Negative indexing
#To find length of the string
print(len(Name))
#Slicing
print(Name[2:6])
print(Name[2:8:2]) #Alternative positions
#List[Mutable]
l=[18,"Rama",12.7]
print(l)
#Tuple[Immutable]
T=(1,2,3,5,6)
print(T)
#set[Mutable]
S={1,2,3,5,6,6,2} #set won't allow any duplicate values
print(S)
#Dictionary/Dict:[Mutable]
Dict={"Name":"rama","age":19,"Height":150}
print(Dict)
Dict2={"Names":["Rama","Akshaya","Jyothi"]}
print(Dict2)