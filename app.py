import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()