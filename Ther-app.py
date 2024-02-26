import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
   page_title="Therap-easy peasy",
   page_icon="📝",
   layout="wide",
   initial_sidebar_state="expanded",
)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover 
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('app.jpg') 


st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title('This is a _Demo_ of how the models can be used.')