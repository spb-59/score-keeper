from table2ascii import table2ascii as t2a, PresetStyle

def printGame(scores:dict):

    
    player=[]
    for key,item in scores.items():
        if key=="_id": break
        player.append([key,item[0],item[1]])



    out=t2a(
    header=["Name","Score","Point"],
    body=[[player[0][0],player[0][1],player[0][2]], [player[1][0],player[1][1],player[1][2]],[player[2][0],player[2][1],player[2][2]],[player[3][0],player[3][1],player[3][2]] ],
    style=PresetStyle.thin_compact
    )


    return f"```\n{out}\n``` id:{scores["_id"]}"

