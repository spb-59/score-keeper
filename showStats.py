from pymongo_get_database import get_players
from table2ascii import table2ascii as t2a, PresetStyle

def showLeaderboard():
    dbname = get_players()
    leaderboard=dbname["current"]
    stats=[]
    n=0

    for x in leaderboard.find():
        if n>10: break
        else: n+=1

        stats.append([x["_id"],x["score"]])
    
    stats.sort(key=lambda x:x[1],reverse=True)

    out=t2a(
    header=["Name","Points"],
    body=stats,
    style=PresetStyle.ascii_minimalist
    )

    return f"```{out}```"

    
    
def showStat(args):
    dbname = get_players()

    if args not in dbname.list_collection_names():
        return f"``` Player not registered ```" 

    stat=dbname[args]
    stats=[]

    num = stat.count_documents({}) - 1 
    n=0

    for x in stat.find():
        if n>min(6,num): break
        else: n+=1       

        if x["score"]:stats.append([x["date"],x["score"]])
    
    out=t2a(
    header=["Date","Points"],
    body=stats,
    style=PresetStyle.ascii_minimalist
    )


    return f' ``` {args} has {num} games and last games: \n  {out}``` '




