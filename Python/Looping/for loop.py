# for loop...
# To display each character from a string,list,tuple,set,dict...
str="Rama devi"
length=len(str)
for i in range(length):
    print(str[i])

list=["rama",123,45,98]
length=len(list)
for i in range(length):
    print(list[i]) 

#**********************or*********************#

str="Rama devi"
for i in str:
    print(i)

list=["rama",123,45,98]
for i in list:
    print(i)

# To display numbers in given range...
# for i in range(start:end:difference)...

for i in range(1,10):       # To display numbers from 1 to 9...
    print(i)
for i in range(1,10,2):     # To display numbers in alternative from 1 to 9...
    print(i)
for i in range(10,1):       # To display numbers in descending order...
    print(i)
for i in range(10,1,-2):    # To display numbers alternative in descending order...
    print(i)

# Nested for loop...
for i in range(4):        
    for j in range(2):
        print(i,j)      # if both the condition true...print statement will execute...

#***************************************************************************************
# Provide gifts in rank wise....
Top_rankers=["Akshaya","Ramadevi","Bhavitha","Jayasri","Keerthi","Vijji"]
Gifts=["Gold medal","Silver medal","10000","Certificate+7000","5000","2000"]
len1=len(Top_rankers)
len2=len(Gifts)
for i in range(len1):
    for j in range(len2):
        if(i==j):
            print(Top_rankers[i],"You Got",Gifts[j],"congratulations...👏👏")

# User inputs...
RankList=int(input("Enter count of list:"))
Top_rankers=[]
Gifts=[]
for i in range(RankList):
    i=input("Enter rankers list:")
    Top_rankers.append(i)
    print(Top_rankers)
for j in range(RankList):
    j=input("Enter Gifts list:")
    Gifts.append(j)             # assigning Literals to the empty list...
    print(Gifts)
len1=len(Top_rankers)           # Length of the list...
len2=len(Gifts)
for i in range(len1):
    for j in range(len2):
        if(i==j):
            print(Top_rankers[i],"You Got",Gifts[j],"congratulations...👏👏")
