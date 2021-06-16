# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 21:54:25 2021

@author: prava
"""
# Front end web app

# Create a flask app

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import  flasgger
from flasgger import Swagger

app = Flask(__name__) # which point u want to strt the app
#load classifier pickle file
Swagger(app)

pickle_in=open('classifier.pkl','rb') # our model
classifier=pickle.load(pickle_in)

@app.route('/') #root page
def hello():
    return "Hello!"


# variables that will be passing as inputs
@app.route('/predict')
def predict_note_authentication():
    """Authenticating the Bank Notes by entering values
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
          200:
              description: The output values
              
    """
    
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
    """Upload a file to classify
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
          
    responses:
          200:
              description: The output values
    """
    df_test=pd.read_csv(request.files.get('file'))
    prediction= classifier.predict(df_test)
    return "The predicted Value is:"+ str(list(prediction))

if __name__ == '__main__':
    app.run(host='localhost')