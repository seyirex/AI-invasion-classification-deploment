from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import datetime,time
import streamlit.components.v1 as stc


model = load_model('AI_invasion_classification_model_25_06_2021')
def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    if predictions[0] == 0:
        prediction = 'not-purchased'
    else:
        predictions[0] == 1
        prediction = 'purchased'
    return predictions

def run():

    # from PIL import Image
    # image = Image.open('Images\logo.png')
    # image_sidebar = Image.open('renager.jpg')

    # st.image(image,use_column_width=False)
    # st.sidebar.image(image_sidebar)  
    add_selectbox = st.sidebar.selectbox("Please select the option of your choice",("Classification model","About"))

    st.sidebar.info("")

    if add_selectbox == 'Classification model':
        stc.html("""
		<div style="background-color:#31333F;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Classification model</h1>
		</div>	""")
        
        with st.form(key='mlform'):
            Gender= st.selectbox('Gender', ['Male','Female'])
            Age=st.slider('Age',18,60)
            EstimatedSalary=st.slider('Estimated Salary',15000,150000)

            submit_message = st.form_submit_button(label='Prdict')
            
            output=""
            input_dict = {
                        'Gender': Gender,
                        'Age':Age,
                        'EstimatedSalary':EstimatedSalary,
                        }
            input_df = pd.DataFrame([input_dict])   
        if submit_message:
            output = predict(model=model, input_df=input_df)
            st.success('The Client would {} the insurance'.format(output))
             
if __name__ == '__main__':
    run()