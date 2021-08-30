# List of Vegetables:
List_of_item=[lst for lst in input("Vegetables:").split(',')] 
print(List_of_item)
# Hayoo I forgot one item...
# to add that..we can use append..
List_of_item.append("cucumber")
print(List_of_item)  
# list of fruits:
List_of_fruits=[lst for lst in input("fruits:").split(',')]
print(List_of_fruits)
# Both vegetables and fruits in one list:
print(List_of_item+List_of_fruits)
# Repetition of list:
print(List_of_item*2)
print(List_of_fruits*2)
# Membership of list:
print("cucunber" in List_of_item)


'''o/p:
Vegetables:carrot,tomato,potato,chili,sweet potato,radish,brinijal
['carrot', 'tomato', 'potato', 'chili', 'sweet potato', 'radish', 'brinijal']
['carrot', 'tomato', 'potato', 'chili', 'sweet potato', 'radish', 'brinijal', 'cucumber']
fruits:apple,mango,banana,orange,lemon,grapes
['apple', 'mango', 'banana', 'orange', 'lemon', 'grapes']
['carrot', 'tomato', 'potato', 'chili', 'sweet potato', 'radish', 'brinijal', 'cucumber', 'apple', 'mango', 'banana', 'orange', 'lemon', 'grapes']
# Repetition of list:
['carrot', 'tomato', 'potato', 'chili', 'sweet potato', 'radish', 'brinijal', 'cucumber', 'carrot', 'tomato', 'potato', 'chili', 'sweet potato', 'radish', 'brinijal', 'cucumber']
['apple', 'mango', 'banana', 'orange', 'lemon', 'grapes', 'apple', 'mango', 'banana', 'orange', 'lemon', 'grapes']
# Membership of list:
False
'''
