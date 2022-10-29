import streamlit as st
import pandas as pd 
import numpy as np 
codea = "AZ3D"
codeb = "X4HG"
codeC = "UVB5"
coded = "BT7D"
codee = "A2XY"
st.title("Authenticate Yourself!")
form = st.form("my_form")
title = form.text_input('Enter your code here:')
submitted = form.form_submit_button("Submit")
if submitted:
    if title == codea : 
        st.write('You are a registered user.')
    elif title == codeb : 
        st.write('You are a registered user.')
    elif title == codec : 
        st.write('You are a registered user.')
    elif title == coded : 
        st.write('You are a registered user.')
    elif title == codee : 
        st.write('You are a registered user.')
    else:
        st.write('Not a registered user')
