import joblib
from fastapi import FastAPI
app = FastAPI()

model = joblib.load("regression.joblib")

@app.get("/predict")
def predict(size: float, nb_rooms: float, garden: float):
    price = model.predict([[size, nb_rooms, garden]])[0]
    return {"price": price}