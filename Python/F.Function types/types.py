# recursive function...

def count_down(start):
    print("Hi rama")
    next = start - 1
    if next > 0:
        return count_down(next) 
count_down(3)

# Anonymous functions or lambdas function:

lambda x,y : x if x>y else y
print(max(10,20))

# filter() function:

def family(count):
    f=True if count%2==0 else False
    return f
Family_list=[1,2,3,4,5]
print(list(filter(family,Family_list)))
            # or
lst=[1,2,3,4,5]
fun=list(filter(lambda count:(count%2==0),lst))
print(fun)

# map() function:

def family(count):
    return count*count
Family_list=[1,2,3,4,5]
print(list(map(family,Family_list)))
                # or
lst=[1,2,3,4,5]
fun=list(map(lambda count:(count*count),lst))
print(fun)

# function decorators:

def songs(Allmix):
    def music():
        remix=Allmix()
        return remix + " To perform Sai Pallavi's Telugu song 'Saranga Dariya' from the movie Love Story🎼🎼"
    return music

def dress_costume(costume):
    def colour():
        BB=costume()
        return BB + " your costume 👗."
    return colour

@songs
@dress_costume
def Be_Ready():
    return " Be ready with,"

print(Be_Ready())
