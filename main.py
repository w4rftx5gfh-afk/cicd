from fastapi import FastAPI, status 
from pydantic import BaseModel, Field

app = FastAPI()

class FeatureInput(BaseModel):
    feature_1: float = Field(..., gt=0)
    feature_2: float = Field(..., gt=0)

@app.get("/healthz", status_code=status.HTTP_200_OK)
def healthcheck():
    return {"status":"ok"}

@app.post("/predict")
def predict(data: FeatureInput):
    prediction  = data.feature_1 * 1.5 + data.feature_2 * 2.0
    return {"predicion": prediction} 