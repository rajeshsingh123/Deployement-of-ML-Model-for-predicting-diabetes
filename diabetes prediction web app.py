# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 05:35:05 2022

@author: sandeep singh
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model = pickle.load(open('C:/Users/sandeep singh/Documents/New folder/trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data) :
    

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
 
    
def main() :
     #giving title
    st.title('dibetes prediction web app')
     
     #getting the inpt data from user
     
    Pregnancies=st.text_input('number of pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure value')
    SkinThickness=st.text_input('SkinThickness value')
    Insulin=st.text_input('Insulin value')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    Age=st.text_input('Age of the person')
     
     
     #code for prediction
     
    diagnosis=''
     
     #creating button fot prediction
    if st.button('diabetes test result'):
         diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
     
     
    st.success(diagnosis)
     
    
if __name__ == '__main__':
    main()
     
     
     
     

     