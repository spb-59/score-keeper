
from pymongo_get_database import get_games
from insertPlayer import insertPlayer



def calculateScores(scores:dict):
    target=30000
    uma=[20,10,-10,-20]

    for i,score in enumerate(scores.items()):
        score[1].append(((score[1][0]-target)/1000)+uma[i])
    



async def insertGame(ctx,args):
    #getting the database
    dbname = get_games()

    #splitting the input into indivisual scores

    scores=args.split()

    #setting collection as default
    gameName="default"

    #if user has specified gameName storing that in the db
    if len(scores)>4: gameName=scores.pop()
    if gameName[0]=="-" : gameName=gameName[1:]
        
    games = dbname['games']

    #dict that is populated to be insterted into the db
    insert={}

    #populating the db
    for score in scores:
        curr=score.split(":")
        insert[curr[0]]=[int(curr[1])]

    insert=dict(sorted(insert.items(),key=lambda x:x[1],reverse=True))
    calculateScores(insert)

    fail=False
    for i,score in insert.items():
        if not insertPlayer(i,score):
            await ctx.send(f' ``` {i} is not registered ``` \n Please register using /register username')
            fail=True
            
    





    if gameName!="default": insert["_id"]=gameName
    if fail: insert=None
    else:games.insert_one(insert)

    return insert

