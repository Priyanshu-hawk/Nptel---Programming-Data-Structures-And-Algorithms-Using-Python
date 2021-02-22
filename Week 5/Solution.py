names = []
while True:
    data = input()
    if data != "":
        names.append(data)
    else:
        break
the_data = {}
for name in names:
    start = 0
    opt = []
    for i in range(len(name)):
        if name[i] ==":":
            opt.append(name[start:i])
            start = i+1
    for j in range(len(name)-1,0,-1):
        if name[j] == ":":
            opt.append(name[j+1:])
    the_data[opt[0]] = {"best_of_5":0,"best_of_3":0,"set_won":0,"game_won":0,"set_lost":0,"game_lost":0}
    the_data[opt[1]] = {"best_of_5":0,"best_of_3":0,"set_won":0,"game_won":0,"set_lost":0,"game_lost":0}

for name in names:
    val = name.split(":")
    player1 = val[0]
    player2 = val[1]
    allscore = val[2].split(",")
    set3_won1, set3_won2, set5_won2, set5_won1 = 0,0,0,0
    for score in allscore:
        the_data[player1]['game_won'] = int(the_data[player1]['game_won']) + int(score[0])
        the_data[player1]['game_lost'] = int(the_data[player1]['game_lost']) + int(score[-1])
        the_data[player2]['game_won'] = int(the_data[player2]['game_won']) + int(score[-1])
        the_data[player2]['game_lost'] = int(the_data[player2]['game_lost']) + int(score[0])
        #print( the_data[player1]['game_won'], the_data[player1]['game_lost'], the_data[player2]['game_won'], the_data[player2]['game_lost'])

        if len(allscore)>3 and len(allscore) <= 5 and (int(score[0])>=6 or int(score[-1])>=6):
            if int(score[0]) > int(score[-1]):
                the_data[player1]['set_won'] = int(the_data[player1]['set_won']) + 1
                the_data[player2]['set_lost'] = int(the_data[player2]['set_lost']) + 1
                set5_won1 += 1 
            elif  int(score[0]) < int(score[-1]):
                the_data[player2]['set_won'] = int(the_data[player2]['set_won']) + 1
                the_data[player1]['set_lost'] = int(the_data[player1]['set_lost']) + 1
                set5_won2 += 1
        if len(allscore)<=3 and (int(score[0]) >=6 or int(score[-1])>=6):
            if int(score[0]) > int(score[-1]):
                the_data[player1]['set_won'] = int(the_data[player1]['set_won']) + 1
                the_data[player2]['set_lost'] = int(the_data[player2]['set_lost']) + 1
                set3_won1 += 1
            elif int(score[-1]) > int(score[0]):
                the_data[player2]['set_won'] = int(the_data[player2]['set_won']) + 1
                the_data[player1]['set_lost'] = int(the_data[player1]['set_lost']) + 1
                set3_won2 += 1
    if set5_won1 >= (set5_won2+1):
        the_data[player1]["best_of_5"] = int(the_data[player1]["best_of_5"]) + 1
    if set5_won2 >= (set5_won1+1):
        the_data[player2]["best_of_5"] = int(the_data[player5]["best_of_5"]) + 1
    if set3_won1 >= (set3_won2 + 1 ):
        the_data[player1]["best_of_3"] = int(the_data[player1]["best_of_3"]) + 1
    if set3_won2 >= (set3_won1 + 1):
        the_data[player2]["best_of_3"] = int(the_data[player2]["best_of_3"]) + 1

#print(the_data) 
theAns = []
for apdLst in the_data:
    theAns.append([])

index = 0
for single_data in the_data:
    theAns[index].append(single_data)
    theAns[index].append(the_data[single_data]["best_of_5"])
    theAns[index].append(the_data[single_data]["best_of_3"])
    theAns[index].append(the_data[single_data]["set_won"])
    theAns[index].append(the_data[single_data]["game_won"])
    theAns[index].append(the_data[single_data]["set_lost"])
    theAns[index].append(the_data[single_data]["game_lost"])
    index += 1

theAns.sort(key=lambda x: (x[1],x[2],x[3],x[4],x[6],x[5]))
theAns = theAns[::-1]

for pr in theAns:
    count = 0
    for ans in pr:
        if count <= 5:
            print(ans, end=" ")
            
        if count == 6:
            print("",end="")
            print(ans,end="")
        count += 1
    print("")
