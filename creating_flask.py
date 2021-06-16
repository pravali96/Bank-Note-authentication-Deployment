# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:10:22 2021

@author: prava
"""
# Create a flask app

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__) #whihc point u want to strt the app
#load classifier pickle file
pickle_in=open('classifier.pkl','rb') # our model
classifier=pickle.load(pickle_in)

@app.route('/') #root page
def hello():
    return "Hello!"


# variables that will be passing as inputs
@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction= classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "The predicted Value is:"+ str(prediction)

# giving a file of test inputs
@app.route('/predict_file', methods=['POST'])
def predict_note_file():
    df_test=pd.read_csv(request.files.get('file'))
    prediction= classifier.predict(df_test)
    return "The predicted Value is:"+ str(list(prediction))

if __name__ == '__main__':
    app.run(host='localhost')