from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal
import pickle
import pandas as pd
from datetime import datetime


with open("LRmodel.pkl", "rb") as f:
    pipe = pickle.load(f)


app = FastAPI()

class UserInput(BaseModel):
    name: Annotated[str, Field(..., description='Name of the car', examples=['Maruti Suzuki Swift'])]
    company: Annotated[str, Field(..., description='Model of the car')]
    year: Annotated[int, Field(...,description='Model is of year')]
    kms_driven: Annotated[int, Field(..., gt=0, description='Mileage of car')]
    fuel_type: Annotated[Literal['Petrol', 'Diesel', 'LPG'], Field(..., description='Fuel type', examples=['Petrol'])]

    @field_validator('year') 
    @classmethod
    def validate_year(cls, value):
        if value not in range(1950, datetime.now().year + 1):
            raise ValueError("Year is not valid")
        return value

@app.get("/")
def root():
    return {"message":"Hello"}

@app.post("/predict")
def predict_car_price(data: UserInput):
    inputed_data = pd.DataFrame([{
        "name": data.name,
        "company": data.company,
        "year": data.year,
        "kms_driven": data.kms_driven,
        "fuel_type": data.fuel_type
    }])

    prediction = pipe.predict(inputed_data)
    if prediction[0]<0:
        prediction = 0.0
    final_prediction = (f"{round(float(prediction[0]), 2)} Rs.")
    return {"prediction": final_prediction}
