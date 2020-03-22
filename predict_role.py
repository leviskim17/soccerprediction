# coding: utf-8

import sklearn
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import sqlite3
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets

#from players import getplayers
"""
fd = pd.read_csv('/Users/apple/Desktop/player_label.csv')

df_obj = fd.label
fd.label = df_obj.apply(lambda x: str(x).strip())

print(fd.label)
test_set = fd[['label']]
train_set = fd[['overall_rating','potential','preferred_foot','attacking_work_rate','defensive_work_rate','crossing',
                'finishing','heading_accuracy','short_passing','volleys','dribbling','curve','free_kick_accuracy','long_passing','ball_control','acceleration',
                'sprint_speed','agility','reactions','balance','shot_power','jumping','stamina','strength','long_shots',
                'aggression','interceptions','positioning','vision','penalties','marking','standing_tackle','sliding_tackle','gk_diving','gk_handling','gk_kicking','gk_positioning',
                'gk_reflexes']]
train_set = train_set[1:]
test_set=test_set[1:]



from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test = train_test_split(train_set, test_set, test_size=0.33, random_state=12)




from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(x_train, y_train)
predicted = clf.predict(x_test)
import numpy as np
from sklearn import metrics 
print("#################### NB ######################")
confusion_matrix_NB = metrics.confusion_matrix(y_test,predicted)
print(confusion_matrix_NB)
accuracy_NB = metrics.accuracy_score(y_test,predicted)
print(accuracy_NB)
print("##############################################")


from sklearn import tree
clf = tree.DecisionTreeClassifier().fit(x_train, y_train)
predicted = clf.predict(x_test)
print("#################### Decision Tree ######################")
print(metrics.confusion_matrix(y_test, predicted))
print(metrics.accuracy_score(y_test,predicted))
print(metrics.classification_report(y_test, predicted))
print("##############################################")


from sklearn.linear_model import SGDClassifier
clf = SGDClassifier().fit(x_train, y_train)
predicted = clf.predict(x_test)
print("#################### SGD Classifier ######################")
print(metrics.confusion_matrix(y_test, predicted))
print(metrics.accuracy_score(y_test,predicted))
print("##############################################")



#print(metrics.classification_report(y_test, predicted))

#get the data to predict the role 

###### array transfer to datafram
from pandas.core.frame import DataFrame


predict_set = pd.read_excel('C:/Users/CHU/Desktop/text_mining_project/osha.xlsx')
predict_set.shape

predict_osha = predict_set.iloc[:,3]
predict_osha = predict_osha.apply(pre_process)
predict_count = count_vect.transform(predict_osha)
predict_count.shape

predicted = clf.predict(predict_count)
pd.value_counts(predicted)

"""
def predict_role(ps):
	fd = pd.read_csv('player_label.csv')

	df_obj = fd.label
	fd.label = df_obj.apply(lambda x: str(x).strip())
	print(fd.label)
	test_set = fd[['label']]
	train_set = fd[['overall_rating','potential','preferred_foot','attacking_work_rate','defensive_work_rate','crossing',
                'finishing','heading_accuracy','short_passing','volleys','dribbling','curve','free_kick_accuracy','long_passing','ball_control','acceleration',
                'sprint_speed','agility','reactions','balance','shot_power','jumping','stamina','strength','long_shots',
                'aggression','interceptions','positioning','vision','penalties','marking','standing_tackle','sliding_tackle','gk_diving','gk_handling','gk_kicking','gk_positioning',
                'gk_reflexes']]
	train_set = train_set[1:]
	test_set=test_set[1:]

	from sklearn.model_selection import train_test_split
	x_train,x_test, y_train, y_test = train_test_split(train_set, test_set, test_size=0.33, random_state=12)

	from sklearn.naive_bayes import MultinomialNB
	clf = MultinomialNB().fit(x_train, y_train)
	predicted = clf.predict(x_test)
	import numpy as np
	from sklearn import metrics 
	print("#################### NB ######################")
	confusion_matrix_NB = metrics.confusion_matrix(y_test,predicted)
	print(confusion_matrix_NB)
	accuracy_NB = metrics.accuracy_score(y_test,predicted)
	print(accuracy_NB)
	print("##############################################")


	from sklearn import tree
	clf_tree = tree.DecisionTreeClassifier().fit(x_train, y_train)
	predicted = clf_tree.predict(x_test)
	print("#################### Decision Tree ######################")
	print(metrics.confusion_matrix(y_test, predicted))
	print(metrics.accuracy_score(y_test,predicted))
	print(metrics.classification_report(y_test, predicted))
	print("##############################################")


	from sklearn.linear_model import SGDClassifier
	clf = SGDClassifier().fit(x_train, y_train)
	predicted = clf.predict(x_test)
	print("#################### SGD Classifier ######################")
	print(metrics.confusion_matrix(y_test, predicted))
	print(metrics.accuracy_score(y_test,predicted))
	print("##############################################")

	from pandas.core.frame import DataFrame
	predict_data = DataFrame(ps)

	print("----------------------&&&&&&&&&&&&&&&&&&&&&&&&&&&&&-----------------------")
	print(predict_data)
	print("----------------------&&&&&&&&&&&&&&&&&&&&&&&&&&&&&-----------------------")

	predict_data = predict_data.iloc[:,4:]
	print("---------------------- become 38  ----------------------------------------")
	print(predict_data)
	print("---------------------- become 38  ----------------------------------------")

	predicted = clf_tree.predict(predict_data)
	#pd.value_counts(predicted)
	print predicted
	print type(predicted)
	return predicted.tolist()
