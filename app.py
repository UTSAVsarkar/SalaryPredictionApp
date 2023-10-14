import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

page =  st.sidebar.radio("Predict Or Explore the data", ("Predict Page", "Explore Page"))

if page == "Predict Page":
    show_predict_page()
else:
    show_explore_page()