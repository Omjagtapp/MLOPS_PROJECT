from pathlib import Path
from typing import List

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# ----------------------------------------------------
# FastAPI app
# ----------------------------------------------------
app = FastAPI(
    title="Iris Classifier API",
    version="0.2.0",
)


# ----------------------------------------------------
# Request & Response schemas
# ----------------------------------------------------
class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictionResponse(BaseModel):
    prediction: str
    probabilities: List[float]
    model_version: str


# ----------------------------------------------------
# Model loading
# ----------------------------------------------------
MODEL_PATH = Path("model.pkl")

print(f"Loading model from {MODEL_PATH.resolve()}")
artifact = joblib.load(MODEL_PATH)
model = artifact["model"]
target_names = artifact["target_names"]  # e.g. ['setosa', 'versicolor', 'virginica']


# ----------------------------------------------------
# Endpoints
# ----------------------------------------------------
@app.get("/health")
def health():
    """Simple health check endpoint."""
    return {"status": "ok", "model_loaded": MODEL_PATH.exists()}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """
    Predict the iris species using the trained RandomForest model.
    The feature order must match the training data:
    [sepal_length, sepal_width, petal_length, petal_width]
    """
    features = np.array(
        [
            [
                request.sepal_length,
                request.sepal_width,
                request.petal_length,
                request.petal_width,
            ]
        ]
    )

    # Predict class index and probabilities
    class_idx = int(model.predict(features)[0])
    probs = model.predict_proba(features)[0].tolist()
    label = str(target_names[class_idx])

    return PredictionResponse(
        prediction=label,
        probabilities=probs,
        model_version="iris-rf-v0.1",
    )
