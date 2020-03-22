
from sklearn.model_selection import train_test_split

from gap_data import getMatchHistory
from classifier_helper import predictByMultinomialNB, predictByDecisionTree, predictBySGDClassifier, getAccuracy, getMatrix, getReport

def predictGap(team1_id, team2_id, predicted):
    #TrainSet
    #x_train,x_test, y_train, y_test = train_test_split(train_set, test_set, test_size=0.33, random_state=12)

    #xs = getMatchHistory()
    #print(xs)

    predict_gap = 0
    return predict_gap

if __name__ == '__main__':
    #[gap, H, D, A, HP1, HP2, HP3, HP4, HP5, HP6, HP7, HP8, HP9, HP10, HP11, AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10, AP11]
    predicted = [1, 2.5, 4.5, 1.5, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50]
    print(predicted)
    predictGap(9864,8306, predicted)