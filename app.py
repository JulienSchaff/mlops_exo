import joblib
from fastapi import FastAPI
app = FastAPI()

model = joblib.load("regression.joblib")

@app.post("/predict")
def predict(data: dict):
    size = data['size']
    nb_rooms = data['nb_rooms']
    garden = data['garden']
    price = model.predict([[size, nb_rooms, garden]])[0]
    return {"price": price}