# -*- coding: utf-8 -*-
"""NPK predictionAI .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rnIUYfWhvsEK_upE1nju1r6mYEi5IEBv
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn.tree  import DecisionTreeRegressor

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor

Data = pd.read_csv('https://raw.githubusercontent.com/Edie738/ProjectStuff/master/Soil-Analysis-and-Yield-Prediction-master/Soil-Analysis-and-Yield-Prediction-master/TestingAndTrainingDataSet.csv?token=AM5B2M3ZTHLLT5T5EMZRLYS5PTVPO')

#Data

import matplotlib.pyplot as plt

plt.figure(figsize=(15,10))
sns.heatmap(Data.corr(), annot = True)

X = Data.drop(['name','Aval N','Aval P','Aval K','mg kg','Cu','m..Fe','mg..Mn','S'], axis =1)
y1 = Data['Aval N']
y2 = Data['Aval P']
y3 = Data['Aval K']

X

import tensorflow as tf

X_train, X_test, y1_train, y1_test, y2_train, y2_test, y3_train, y3_test = train_test_split(X,y1,y2,y3, test_size = 0.2, random_state = 0)

#y2_train, y2_test = train_test_split(y2, test_size = 0.2, random_state = 0)

#y3_train, y3_test = train_test_split(y3, test_size = 0.2, random_state = 0)

from sklearn.neighbors  import KNeighborsRegressor

modelA1 = KNeighborsRegressor() #LinearRegression()
modelA2 = KNeighborsRegressor() #LinearRegression()
modelA3 = KNeighborsRegressor()   #LinearRegression()

modelA1.fit(X_train, y1_train)

L1_pred = modelA1.predict(X_test)

L1_pred

modelA2.fit(X_train, y2_train)

L2_pred = modelA2.predict(X_test)

L2_pred

modelA3.fit(X_train, y3_train)

L3_pred = modelA3.predict(X_test)

L3_pred

a= modelA1.score(X_test, y1_test)
b= modelA2.score(X_test, y2_test)
c= modelA3.score(X_test, y3_test)
print('Score for Aval N is {}, Score for Aval P is {}, Score for Aval K is{} '.format(a, b, c))

from sklearn.externals import joblib
filename2 = 'npk_modelA2.sav'
joblib.dump(modelA2, filename2)

filename3 = 'npk_modelA3.sav'
joblib.dump(modelA3, filename3)

filename = 'npk_modelA1.sav'
joblib.dump(modelA1, filename)