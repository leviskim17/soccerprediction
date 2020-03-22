import sqlite3
import pandas as pd

#@Author:   Qin Zhi Guo
#@Version:  1.0
#@Description: Function for predicting the score versus result
def predictScore(team1_id,team2_id):

a#Get the score data
    db_con = sqlite3.connect("database.sqlite")
    score_match_history = pd.read_sql_query("select season,home_team_api_id,away_team_api_id,home_team_goal,away_team_goal from Match where home_team_api_id= %s  and away_team_api_id= %s"  % (team1_id,team2_id), db_con)

    #print("Team Versus History : %s" % score_match_history)

    #Need update the column name when the data format is ready
    team1 = score_match_history[['home_team_goal']]
    team2 = score_match_history[['away_team_goal']]

    score_x = team1.mean()
    score_y = team2.mean()

    score_x = round(score_x)
    score_y = round(score_y)

    print("----------------------")
    print("Predict Score  = %s : %s " %(score_x,score_y))
    print("----------------------")

    #getScoreHistoryByTeam(team1_id,team2_id)

    predict_result = [score_x,score_y]

    return predict_result

if __name__ == '__main__':
    predictScore(8634,8633)




