from pymongo_get_database import get_players
from datetime import date

def insertPlayer(i, score: list):
    dbname = get_players()
   
    if i not in dbname.list_collection_names():
        return False
    
    player = dbname[i]
    currentScores = dbname["current"]

    currentScores.update_one({"_id": i}, {"$inc": {"score": score[1]}}, upsert=True)





    d = str(date.today())
    # Insert the score for the player in their respective collection
    player.insert_one({"date": d, "score": score[1]})
    return True


async def register_player(ctx, name):
    dbname = get_players()

    if name in dbname.list_collection_names():
        await ctx.send(f'{name} is already registered')
        return
    
    player = dbname[name]
    currentScores = dbname["current"]
    
    d = str(date.today())
    print(d)
    # Insert a record indicating the player joined
    player.insert_one({"date": d, "score": None})
    # Initialize the player's score to 0 in the "current" collection
    currentScores.insert_one({"_id": name, "score": 0})

    await ctx.send(f'{name} is now registered')
