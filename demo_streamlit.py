import streamlit as st

st.write("Hello, world!")

import pandas as pd

df = pd.read_csv('houses.csv')

st.write(df)
st.line_chart(df['price'])

name = st.text_input("Your name")
if name:
    st.write(f"Hello, {name}!")

# run with streamlit run demo_streamlit.py
