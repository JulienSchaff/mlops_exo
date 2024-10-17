import streamlit as st
import joblib

model = joblib.load("regression.joblib")

size = st.number_input("Size")
nb_rooms = st.number_input("Number of rooms")
garden = st.number_input("Garden")

price = model.predict([[size, nb_rooms, garden]])[0]

st.write(f"The price of the house is {price}")