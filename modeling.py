# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:24:28 2021

@author: prava
"""
import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/prava/Downloads/BankNote_Authentication.csv')

df.head()

# X and y

X= df.iloc[:,:-1] #all cols except last col
y= df.iloc[:,-1]

y.head()

# Doing train, test, split
import sklearn
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

### Implement Random Forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)

## Prediction
y_pred=classifier.predict(X_test)


### Check Accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)
print(score)

### Create a Pickle file using serialization 
import pickle
pickle_out = open("classifier.pkl","wb") #opening a file in wr mode
pickle.dump(classifier, pickle_out) #dumping this file in pickle
pickle_out.close() #close pickle

classifier.predict([[2,3,4,1]])
