# functions...
# Dance performance....judges grades...And the final winner...
# with out parameters and with out return type...
def dance():           
    Contestants=["Ramadevi","Akshaya","Bhavitha"]
    judges=["Monal","Baba bhaskar","Anee master","Mumaith khan","Yash master"]
    len1=len(Contestants)
    len2=len(judges)
    Ramadevi_score=[]
    Akshaya_score=[]
    Bhavitha_score=[]
    print("Judges score:")
    print("Ramadevi..score🧍‍♀️")
    for i in range(1):
         for j in range(len2):
            score=int(input("Enter score of 10:"))
            print(Contestants[i],"got score",score,"from",judges[j])
            Ramadevi_score.append(score)
            print(Ramadevi_score)
    print("Akshaya..score🧍‍♀️")
    for i in range(1,2):
         for j in range(len2):
            score=int(input("Enter score of 10:"))
            print(Contestants[i],"got score",score,"from",judges[j])
            Akshaya_score.append(score)
            print(Akshaya_score)
    print("Bhavitha..score🧍‍♀️")
    for i in range(2,3):
         for j in range(len2):
            score=int(input("Enter score of 10:"))
            print(Contestants[i],"got score",score,"from",judges[j])
            Bhavitha_score.append(score)
            print(Bhavitha_score)
    score1=0
    for i in Ramadevi_score:
        score1+=i
    print(score1)
    score2=0
    for j in Akshaya_score:
        score2+=j
    print(score2)
    score3=0
    for k in Bhavitha_score:
        score3+=k
    print(score3)

    if(score1>score2):
        if(score1>score3):
            print("Today dance + winner is Ramadevi...🎉🎉")
        else:
            pass
    elif(score2>score1):
        if(score2>score3):
            print("Today dance + winner is Akshaya...🎉🎉")
    elif(score3>score1):
        if(score3>score2):
            print("Today dance + winner is Bhavitha...🎉🎉")
    else:
        print("Tiebreak......Wait and watch in next episode....Byee..Byee.....🤠")

dance()
