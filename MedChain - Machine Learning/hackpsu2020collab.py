# -*- coding: utf-8 -*-
"""HACKPSU2020Collab

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lj9x9Sn010pGn4-QMJ5G_u0q1MwMRGXi
"""

#import os
#os.path.abspath("C:\Users\JP\Documents\Hack")
#import dependencies
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
#from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

#Load the data
from google.colab import files
uploaded = files.upload()

#Store the data into data frame
df = pd.read_csv('COVID_PA_SouthernRegion.csv')
df.head(36)
#df.tail()

#get the number of tracking days for the state of Pennsylvania
df.shape

#visualize the daily growth of the Pennsylvania COVID data
#On the x-axis 0 = ADAMS and 30 = WESTMORELAND.

plt.figure(figsize=(16,8))
plt.title('PA COVID DATA TRACKER')
plt.xlabel('Northern Region Counties of Pennsylvania')
plt.ylabel('Infection Trend (+/-) in the # of Confirmed Cases')
plt.plot(df['Confirmed'])
plt.show()

#get the confirmed growth per county
df = df[['Confirmed']]
df.head(36)
#df.tail()

#get the daily confirmed growth
df = df[['Confirmed']]
df.head()
#df.tail(13)

#Create a variable to predict 'x' months out into the future
future_trend = 3
#create a new column (target) shifted 'x' units/months up
df['Prediction'] = df[['Confirmed']].shift(-future_trend)
df.head(36)
#df.tail(10)

#Create the feature data set (X) and convert it to a numpy array and remove the last 'x' rows/days
X = np.array(df.drop(['Prediction'], 1))[:-future_trend]
print(X)

#Create the feature data set (X) and convert it to a numpy array and remove the last 'y' rows/days
Y = np.array(df.drop(['Prediction'], 1))[:-future_trend]
print(Y)

#create the target data set (y) and convert it to a numpy array and get all of the target values except the last 'x' rows/days
Y = np.array(df['Prediction'])[:-future_trend]
print(Y)

#split the data into 75% train and 25% test
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.25)

#Create and train the Support Vector Machine (Regressor)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

#Create the models
#Create the decision tree regression model
tree = DecisionTreeRegressor().fit(x_train, y_train)
#Create the linear regression model
lr = LinearRegression().fit(x_train, y_train)

#get the last 'x' rows of the feature data set
x_future = df.drop(['Prediction'], 1)[:-3]
x_future = x_future.tail(3)
x_future = np.array(x_future)
x_future

#show the tree prediction model
tree_prediction = tree.predict(x_future)
print(tree_prediction)

#show the linear regression prediction model
lr_prediction = lr.predict(x_future)
print(lr_prediction)

#show the SVR prediction model 
svr_rbf_prediction = svr_rbf.predict(x_future)
print(svr_rbf)

#visualize the data
predictions = tree_prediction

valid = df[X.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Decision Trees Model')
plt.xlabel('Northern Pennsylvania Region COVID Tracker')
plt.ylabel('Infection Trend (+/- in the # of Confirmed Cases)')
plt.plot(df['Confirmed'])
plt.plot(valid[['Confirmed', 'Predictions']])
plt.legend(['Orig', 'Val', 'Pred'])
plt.show()

tree.score(x_test, y_test)

#visualize the data
predictions = lr_prediction

valid = df[X.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Linear Regressor Model')
plt.xlabel('Northern Pennsylvania Region COVID Tracker')
plt.ylabel('Infection Trend (+/- in the # of Confirmed Cases)')
plt.plot(df['Confirmed'])
plt.plot(valid[['Confirmed', 'Predictions']])
plt.legend(['Orig', 'Val', 'Pred'])
plt.show()

lr.score(x_test, y_test)

#visualize the data
predictions = svr_rbf_prediction

valid = df[X.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Support Vector Regressor Model')
plt.xlabel('Northern Pennsylvania Region COVID Tracker')
plt.ylabel('Infection Trend (+/- in the # of Confirmed Cases)')
plt.plot(df['Confirmed'])
plt.plot(valid[['Confirmed', 'Predictions']])
plt.legend(['Orig', 'Val', 'Pred'])
plt.show()

svr_rbf.score(x_test, y_test)

County 	Region 	Cases 	Confirmed 	Probable 	PersonsWithNegativePCR

feature_cols = ['Confirmed'] 
Y = df[feature_cols] # Features
X = df.Confirmed # Target variable

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

# import the class and create classifier/model
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(30, 30, 20),activation='relu',random_state=101)

x_train = x_train.values.reshape(-1, 1)
y_train = y_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)

#train model
model.fit(x_train, y_train)

#predict
Y_predict = model.predict(x_test)

# import confusion_matrix and classification_report classes
from sklearn.metrics import classification_report, confusion_matrix

#computer performance measures
print(confusion_matrix(y_test, Y_predict))  
print(classification_report(y_test, Y_predict))

from sklearn import metrics
#Calculate performance measures:
print("Accuracy:",metrics.accuracy_score(y_test, Y_predict))
print("Precision:",metrics.mean_squared_error(y_test, Y_predict))
print("Recall:",metrics.mean_absolute_error(y_test, Y_predict))
print("ConfuusionMatrix:",metrics.multilabel_confusion_matrix(y_test, Y_predict))
print("ConfuusionMatrix:",metrics.plot_confusion_matrix(y_test, Y_predict))

# import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

# create heatmap
cnf_matrix =confusion_matrix(y_test, Y_predict)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')



