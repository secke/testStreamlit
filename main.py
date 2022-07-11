import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.title("CECI EST UN SIMPLE TEST AVEC STREAMLIT")

st.sidebar.button("clicker")
mon_text=st.sidebar.text_input('entrer ici votre texte clossard!')
print(mon_text)
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
    
mat=np.random.randn(20,3)
tab=pd.DataFrame(mat,columns=['a','b','c'])
st.line_chart(tab)
st.bar_chart(tab['a'])
loca=pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(loca)
