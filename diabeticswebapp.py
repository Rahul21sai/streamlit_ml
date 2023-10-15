# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 00:07:46 2023

@author: nagas
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/nagas/Downloads/ML projects days/day 1/diabetes_model.sav', 'rb'))


# creating a function for prediction
def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'



def main():
    
    #giving the title
    
    st.title('Diabetes Prediction Web App')
    
    #getting the input data from user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('glucose level')
    BloodPressure = st.text_input('bloodpresure')
    SkinThickness = st.text_input('skin thickness value')
    Insulin = st.text_input('insulin value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('AGe of the person')


    #code for  prediction
    diagnosis = ''
   
   
    #create a button for prediction
   
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]) 
   
    st.success(diagnosis)

 
if __name__ == '__main__':
     main()

 


    
    
    
    
    