
from pymongo_get_database import get_games

def insertPlayer(player,score):
    return


def calculateScores(scores:dict):
    target=30000
    uma=[20,10,-10,-20]

    for i,score in enumerate(scores.items()):
        score[1].append(((score[1][0]-target)/1000)+uma[i])
    




def insertGame(args):
    #getting the database
    dbname = get_games()

    #splitting the input into indivisual scores

    scores=args.split()

    #setting collection as default
    gameName="default"

    #if user has specified gameName storing that in the db
    if len(scores)>4: gameName=scores.pop()
    if gameName[0]=="-" : gameName=gameName[1:]
        
    games = dbname[gameName]

    #dict that is populated to be insterted into the db
    insert={}

    #populating the db
    for score in scores:
        curr=score.split(":")
        insert[curr[0]]=[int(curr[1])]

    insert=dict(sorted(insert.items(),key=lambda x:x[1],reverse=True))
    calculateScores(insert)



    games.insert_one(insert)
    return insert

