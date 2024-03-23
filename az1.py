
import pandas as pd
import streamlit as st
import os
from streamlit_option_menu import option_menu
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

import pickle
with open(r"C:\Users\ADMIN\Desktop\Final\xgboost_model1.pkl", 'rb') as file:
    loaded_model = pickle.load(file)
    
    
Quantity = st.number_input('Quantity:')
Amount = st.number_input('Amount')
Category = st.selectbox('Category', options=['Set', 'kurta', 'Western Dress', 'Top', 'Ethnic Dress', 'Bottom','Saree', 'Blouse', 'Dupatta'])
Size = st.selectbox('Size', options=['S', '3XL', 'XL', 'L', 'XXL', 'XS', '6XL', 'M', '4XL', '5XL','Free'])
Month = st.selectbox('Month', options=['4', '3', '5', '6'])
Fulfilment = st.selectbox('Fulfilment', options=['Merchant', 'Amazon'])


data = {
        "Qty":[Quantity],
        "Amount": [Amount],
        "Category": [Category],
        "Size": [Size],
        "Month": [Month],
        "Fulfilment": [Fulfilment]}

if st.button("Confirm"):
    df1 = pd.DataFrame(data)
    df1["Category"] = df1['Category'].map({'Set':3.56339430e-01, 'kurta':3.53583303e-01, 'Western Dress':1.20788780e-01, 
                                           'Top':8.77558898e-02, 'Ethnic Dress':2.36742488e-02, 'Bottom':1.88053172e-02,
                                           'Saree':1.69362976e-02 ,'Blouse':2.20964170e-02,'Dupatta':2.03154309e-05})
    df1["Size"]  = df1["Size"].map({'Small':7, 'Triple XL':0, 'XL':8, 'L':5,'XXL':10,'XS':9,'6XL':3,'M':6 ,'4XL':1,'5XL':2,'Free':4})
    df1["Month"]  = df1['Month'].map({'4':4, '3':3, '5':5, '6':6})
    df1["Fulfilment"]  = df1["Fulfilment"].map({'Merchant':1,"Amazon":2})
    
    Influence = loaded_model.predict(df1)
    #st.write("Influence:", Influence)
    #st.write(df1)
    
    for i, pred in enumerate(Influence):
        if pred == 0:
            st.success("Less Impactful")
        elif pred == 1:
            st.success("Moderately Impactful")
        elif pred == 2:
            st.success("Highly Impactful")


