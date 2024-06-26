import os
import pandas as pd
from fastapi import FastAPI
from ml.data import apply_label, process_data
from ml.model import inference, load_model
from pydantic import BaseModel, Field

#define Data class and use base model
class Data(BaseModel):
    age: int = Field(..., example=37)
    workclass: str = Field(..., example="Private")
    fnlgt: int = Field(..., example=178356)
    education: str = Field(..., example="HS-grad")
    education_num: int = Field(..., example=10, alias="education-num")
    marital_status: str = Field(
        ..., example="Married-civ-spouse", alias="marital-status"
    )
    occupation: str = Field(..., example="Prof-specialty")
    relationship: str = Field(..., example="Husband")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    capital_gain: int = Field(..., example=0, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., example=40, alias="hours-per-week")
    native_country: str = Field(..., example="United-States", alias="native-country")
    
path =  "model/encoder.pkl"
encoder = load_model(path)

path = "model/model.pkl"
model = load_model(path)

app = FastAPI() 


#Posted at root "/" domain and will return friendly greeting to request "Hello World!"
@app.get("/")
async def get_root():
    """ Say hello!"""
    return {"greeting": "Hello World!"}

#Posted at the domain of /"data/" and 
@app.post("/data/")
async def post_inference(data: Data):
    data_dict = data.dict()
    data = {k.replace("_", "-"): [v] for k, v in data_dict.items()}
    data = pd.DataFrame.from_dict(data)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    data_processed, _, _, _ = process_data(
        data,     
        cat_features,
        training=False,
        encoder=encoder,
    )        
        
    _inference = inference(model, data_processed)
    return {"result": apply_label(_inference)}
