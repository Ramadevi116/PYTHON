# set:
s={1,2,3,4,4}
print(type(s))
s={1,3,2,4}
print(min(s))
print(max(s))
print(len(s))
print(sum(s))
print(sorted(s))
print(s.pop())
print(s.remove(2))
print(s.add(12))
print(s.clear())
# isdisjoint(), issubset(), issuperset()
'''If A and B are two sets:
Union()==A|B
Intersection()==A&B
Difference()==A-B
Symmetric _difference()==A^B
'''
# dict:
dict={'name':'Rama','Hobbies':'Sleeping','Timing':12}
print(dict)
print(dict.clear())
d=dict.copy()
print(d)
print(d.keys())
print(d.values())


# creating a dictionary with cricket players names and scores
dict={}
n=int(input("How many players?"))
for i in range(n):
    key=input("Player name:")
    values=int(input("Enter runs:"))
    dict.update({key:values})
for i in dict.keys():
    print(i)
name=input("Enter player name:")
runs=dict.get(name,-1)
result='player not found' if(runs==-1) else '{} made runs {}.'.format(name,runs)
print(result)

