import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from tensorflow import keras
from keras.models import load_model

navigation = st.sidebar.selectbox('Pilih Halaman : ', ('EDA', 'Predict a Churn'))

# Load the Models


with open('final_pipeline.pkl', 'rb') as file_1:
  model_pipeline = pickle.load(file_1)

with open('list_num_cols (2).txt', 'r') as file_2:
  list_num_cols = json.load(file_2)

with open('list_cat_cols (2).txt', 'r') as file_3:
  list_cat_cols = json.load(file_3)

model_ann = load_model('churn_model (1).h5')


def run():
    with st.form(key='form_Churn'):
        min_date = pd.to_datetime('2016-10-18')
        joining_date = st.date_input('joining_date:', key='joining_date', min_value=min_date)
        last_visit_time = st.date_input('last_visit_time:', key='last_visit_time', min_value=min_date)
        avg_transaction_value = st.number_input('avg_transaction_value:')
        avg_frequency_login_days = st.number_input('avg_frequency_login_days:')
        points_in_wallet = st.number_input('points_in_wallet:')
        feedback = st.selectbox('feedback:', ('Poor Website', 'Poor Customer Service', 'Too many ads', 'Poor Product Quality', 'No reason specified', 'Products always in Stock', 'Reasonable Price', 'Quality Customer Care', 'User Friendly Website'), index=1)
        submitted = st.form_submit_button('Predict')

    avg_transaction_value = float(avg_transaction_value)
    points_in_wallet = float(points_in_wallet)
    

    if avg_transaction_value != '':
        avg_transaction_value = float(avg_transaction_value)
    if points_in_wallet != '':
        points_in_wallet = float(points_in_wallet)


    data_inf = {
        'joining_date': joining_date, 
        'last_visit_time': last_visit_time, 
        'avg_transaction_value': avg_transaction_value, 
        'avg_frequency_login_days': avg_frequency_login_days,
        'points_in_wallet': points_in_wallet, 
        'feedback': feedback, 
    }

    data_inf = pd.DataFrame([data_inf])

    if submitted:
        # Split between Numerical Columns and Categorical Columns
        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # Transform Inference-Set
        data_inf_transform = model_pipeline.transform(data_inf)

        # Predict using Neural Network
        y_pred_inf = model_ann.predict(data_inf_transform)
        y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)

        # Display prediction result
        if y_pred_inf[0][0] == 1:
            st.write('Hasil prediksi: Customer will churn')
        else:
            st.write('Hasil prediksi: Customer will not churn')

if navigation == 'Predict A Churn':
    run()
