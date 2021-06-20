# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:55:32 2021

@author: prava
"""

# Create a Streamlit app

#from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
#import  flasgger
import streamlit as st
#from flasgger import Swagger


pickle_in=open('classifier.pkl','rb') # our model
classifier=pickle.load(pickle_in)

#@app.route('/') #root page
def hello():
    return "Hello!"


# variables that will be passing as inputs
#@app.route('/predict')
def predict_note_authentication(variance, skewness, curtosis, entropy):
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
    prediction= classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "The predicted Value is:"+ str(prediction)

# giving a file of test inputs
#@app.route('/predict_file', methods=['POST'])

def main():
    st.title('Bank Note Authenticator')
    html_temp = '''
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Note Authenticator using Streamlit </h2>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type Here")
    skewness=st.text_input("Skewness", "Type Here")
    curtosis=st.text_input("Curtosis", "Type Here")
    entropy=st.text_input("Entropy", "Type Here")
    result=""
    if st.button("Predict"):
        result= predict_note_authentication(variance, skewness, curtosis, entropy)
    st.success('The output is {} '.format(result))
    if st.button("About"):
        st.text("Built using Streamlit")
    
if __name__ == '__main__':
    main()
    
    # In order to run this file, type in as:
    # streamlit run Streamlit_api.py 
    # in anaconda prompt by choosing the environment.
