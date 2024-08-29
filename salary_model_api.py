import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()


# Define the request body
class SalaryPredictionRequest(BaseModel):
    time_in_company: int
    level: int


# Define the response body
class SalaryPredictionResponse(BaseModel):
    salary: float
    currency: str


# Load the model
model = joblib.load("models/salary_model.pkl")


# Endpoint to predict salary using the model
@app.post("/predict_salary", response_model=SalaryPredictionResponse)
def predict_salary(request: SalaryPredictionRequest):
    # Extract the data from the request
    data = {
        "tempo_na_empresa": [request.time_in_company],
        "nivel_na_empresa": [request.level],
    }

    # Create a DataFrame from the data
    df_data = pd.DataFrame(data)

    # Make a prediction
    prediction = model.predict(df_data)

    # Return the prediction
    return SalaryPredictionResponse(salary=prediction[0], currency="BRL")


# Run the API with Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
