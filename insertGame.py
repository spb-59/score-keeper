from pymongo_get_database import get_games
from insertPlayer import insertPlayer,searchPlayer


def calculateScores(scores: dict):
    target = 25000
    uma = [30, 10, -10, -30]

    for i, score in enumerate(scores.items()):
        score[1].append(((score[1][0] - target) / 1000) + uma[i])


async def insertGame(ctx, args):
    # getting the database
    dbname = get_games()

    # splitting the input into indivisual scores

    scores = args.split()

    if len(scores) < 4:
        await ctx.send(
            "Please provide all 4 players, like `!game [player]:[score]....-[game name:optional]`"
        )
        return

    # setting collection as default
    gameName = "default"

    # if user has specified gameName storing that in the db
    if len(scores) > 4:
        gameName = scores.pop()
    if gameName[0] == "-":
        gameName = gameName[1:]

    games = dbname["games"]

    # dict that is populated to be insterted into the db
    insert = {}

    # populating the db
    for score in scores:
        curr = score.split(":")
        if len(curr)<=1:
            ctx.send('Provide score with name as [player]:[score]')
            return
        try:
            value=int(curr[1])
        except ValueError:
            ctx.send(f'Invalid value {curr[1]}, please provide number')
            return

        insert[curr[0]] = [value]

    insert = dict(sorted(insert.items(), key=lambda x: x[1], reverse=True))
    if len(insert)<4:
        await ctx.send('Please provide 4 different players')
        return
    calculateScores(insert)

    fail = False
    for i, score in insert.items():
        if not searchPlayer(i):
            await ctx.send(
                f" ``` {i} is not registered ``` \n Please register using !register username"
            )
            return

    for i, score in insert.items():
        if not insertPlayer(i, score):
            await ctx.send(
                f" ``` {i} is not registered ``` \n Please register using !register username"
            )
        

    if gameName != "default":
        insert["_id"] = gameName
    if fail:
        insert = None
    else:
        games.insert_one(insert)

    return insert
