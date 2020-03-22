import sqlite3
import pandas as pd
from sklearn import svm
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from odds_data import getOddsDataForSpanish,getTeamsPower,getOddsHistoryByTeam
from model_helper import predictBySVM,predictByARDRegression,predictByLR,predictGAP,result_accuracy

#@Author:   Qin Zhi Guo
#@Version:  1.0
#@Description: Function for predicting 2 teams betting odds result: win/draw/lose
def predictOdds(team1_id,team2_id):

    merged_data = getOddsDataForSpanish()
    #Shuffle and Slice Data for feeding the model
    #merged_data = shuffle(merged_data)

    X = merged_data[['power','power_t']]
    y_win = merged_data[['mean_win']]
    y_draw = merged_data[['mean_draw']]
    y_lose = merged_data[['mean_lose']]

    X_train_win, X_test_win, y_train_win, y_test_win = train_test_split(X, y_win, test_size=0.2)
    X_train_draw, X_test_draw, y_train_draw, y_test_draw = train_test_split(X, y_draw, test_size=0.2)
    X_train_lose, X_test_lose, y_train_lose, y_test_lose = train_test_split(X, y_lose, test_size=0.2)

    team_data = getTeamsPower(team1_id,team2_id)

    #Predict using SVM
    a_y1 = predictBySVM(X_train_win,team_data,y_train_win)
    a_y2 = predictBySVM(X_train_draw,team_data,y_train_draw)
    a_y3 = predictBySVM(X_train_lose,team_data,y_train_lose)

    #Predict using ARD_Regression
    b_y1 = predictByARDRegression(X_train_win,team_data,y_train_win)
    b_y2 = predictByARDRegression(X_train_draw,team_data,y_train_draw)
    b_y3 = predictByARDRegression(X_train_lose,team_data,y_train_lose)

    #Ensemble model using voting with corresponding accuracy weight
    y1 = (a_y1*1 + b_y1*0)/1
    y2 = (a_y2*1 + b_y2*0)/1
    y3 = (a_y3*2 + b_y3*1)/3

    #Gambling Strategy
    if y2 - y1 > y1*0.7:
        y1 = y1*0.8
        y2 = y2*2
        y3 = y3*3

    print("----------------------")
    print("Win  = %.3f" % y1)
    print("Draw = %.3f" % y2)
    print("Lose = %.3f" % y3)
    print("----------------------")

    getOddsHistoryByTeam(team1_id,team2_id)

    #Predict using SVM model
    y_test_predict_win = predictBySVM(X_train_win,X_test_win,y_train_win)
    y_test_predict_draw = predictBySVM(X_train_draw,X_test_draw,y_train_draw)
    y_test_predict_lose = predictBySVM(X_train_lose,X_test_lose,y_train_lose)

    y_gap_win = predictGAP(y_test_predict_win,y_test_win)
    y_gap_draw = predictGAP(y_test_predict_draw,y_test_draw)
    y_gap_lose = predictGAP(y_test_predict_lose,y_test_lose)

    print("SVM Win  Accuracy = %.3f" % result_accuracy(y_gap_win, 0.4))
    print("SVM Draw Accuracy = %.3f" % result_accuracy(y_gap_draw, 0.6))
    print("SVM Lose Accuracy = %.3f" % result_accuracy(y_gap_lose, 1.5))

    #Predict using Linear Regression model
    y_test_predict_win  = predictByARDRegression(X_train_win,X_test_win,y_train_win)
    y_test_predict_draw = predictByARDRegression(X_train_draw,X_test_draw,y_train_draw)
    y_test_predict_lose = predictByARDRegression(X_train_lose,X_test_lose,y_train_lose)

    y_gap_win = predictGAP(y_test_predict_win,y_test_win)
    y_gap_draw = predictGAP(y_test_predict_draw,y_test_draw)
    y_gap_lose = predictGAP(y_test_predict_lose,y_test_lose)

    print("LR Win  Accuracy = %.3f" % result_accuracy(y_gap_win, 0.4))
    print("LR Draw Accuracy = %.3f" % result_accuracy(y_gap_draw, 0.6))
    print("LR Lose Accuracy = %.3f" % result_accuracy(y_gap_lose, 1.5))

    y1=y1.sum()
    y2=y2.sum()
    y3=y3.sum()
    predict_result = [y1,y2,y3]

    return predict_result

if __name__ == '__main__':
    predictOdds(8634,8315)




