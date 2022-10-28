import streamlit as st
import pandas as pd 
import numpy as np 
codea=1457
codeb=2479
codec=7841
coded=6397
codee=4278
form = st.form("my_form")
title= int(form.text_input("Code"))
submitted = form.form_submit_button("Submit")
if submitted:
    if title == codea: 
        st.write('You are a registered user.')
    elif title == codeb: 
        st.write('You are a registered user.')
    elif title == codec: 
        st.write('You are a registered user.')
    elif title == coded: 
        st.write('You are a registered user.')
    elif title == codee: 
        st.write('You are a registered user.')
    else:
        st.write('Not a registered user')
