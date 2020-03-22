import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn import tree
from sklearn import metrics

#@Author:Hyuntae Kim
#@Version:1.0

#MultinomiaNB build Model
def predictByMultinomialNB(x_train, y_train):
    clf = MultinomialNB().fit(x_train, y_train)
    predicted = clf.predict(x_test)
    return predicted

#DecisionTree build Model
def predictByDecisionTree(x_train,x_test,y_train):
    clf = tree.DecisionTreeClassifier().fit(x_train, y_train)
    predicted = clf.predict(x_test)
    return predicted

#SGDClassifier build Model
def predictBySGDClassifier(x_train,x_test,y_train):
    clf = SGDClassifier().fit(x_train, y_train)
    predicted = clf.predict(x_test)
    return predicted

#Get Accuracy
def getAccuracy(ytest, predicted):
    accuracy = metrics.accuracy_score(y_test, predicted)
    return accuracy

#Get Confusion Matrix
def getMatrix(ytest, predicted):
    confusion_matrix = metrics.confusion_matrix(y_test, predicted)
    return confusion_matrix

#Get Classification Report
def getReport(y_test, predicted):
    report = metrics.classification_report(y_test, predicted)
    return report