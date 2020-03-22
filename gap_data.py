import sqlite3

#@Author:Hyuntae Kim
#@Version:1.0

def getMatchHistory():
    db_con = sqlite3.connect("database.sqlite")
    c = db_con.cursor()
    sql = "select player_api_id, overall_rating from Player_Attributes;"
    c.execute(sql)
    rs = c.fetchall()
    d = {}
    for r in rs:
        d[r[0]] = r[1]
    #hda = "BWH,BWD,BWA,IWH,IWD,IWA,LBH,LBD,LBA,PSH,PSD,PSA,WHH,WHD,WHA,SJH,SJD,SJA,VCH,VCD,VCA,GBH,GBD,GBA,BSH,BSD,BSA"
    hda = "BWH,BWD,BWA"

    sql = "select home_team_goal-away_team_goal, {0}, {1}, {4} from match where ({2} and {3} and {5});".format(
        ",".join(map((lambda i: "home_player_%s" % i), range(1, 12))),
        ",".join(map((lambda i: "away_player_%s" % i), range(1, 12))),
        " and ".join(map((lambda i: "home_player_%s is not null" % i), range(1, 12))),
        " and ".join(map((lambda i: "away_player_%s is not null" % i), range(1, 12))),
        hda,
        " and ".join(map((lambda i: "%s is not null" % i), hda.split(","))),
        )
    print("sql:" + sql)
    c.execute(sql)
    ms = c.fetchall()
    xs = []
    for m in ms:
        x = list(m)
        for i in range(1, 23):
            if d[m[i]] is None:
                break
            x.append(d[m[i]])
        else:
            xs.append(x)
    return xs