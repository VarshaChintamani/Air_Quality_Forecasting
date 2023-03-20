# -*- coding: utf-8 -*-

#import pandas as pd
#import numpy as np
import streamlit as st 
from pickle import dump
from pickle import load
import pickle


loaded_model = load(open('final_model1.sav', 'rb'))

# creating a function for Prediction

def CO2_prediction(date):
    Prediction=loaded_model.predict(date)[0]
    return Prediction
  
    
  
def main():
    
    
    # giving a title
    st.title('CO2 Estimate Prediction')
    
    
    # getting the input data from the user
    
    
    number1 = st.text_input('Enter The Year')
    
    
    
#     # code for Prediction
    co2 = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        co2 = CO2_prediction(str(number1))
        
        
    st.success(co2)
    
    
    
    
    
if __name__ == '__main__':
    main()
    


