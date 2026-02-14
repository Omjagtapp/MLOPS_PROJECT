from pathlib import Path
from typing import List

import joblib
import numpy as np
import logging
from fastapi import FastAPI
from pydantic import BaseModel

# ----------------------------------------------------
# Logging (Cloud Run captures stdout/stderr automatically)
# ----------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("iris-api")

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
# Model loading (runs at container startup)
# ----------------------------------------------------
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"

logger.info("Loading model from %s", MODEL_PATH.resolve())
artifact = joblib.load(MODEL_PATH)

model = artifact["model"]
target_names = artifact["target_names"]  # e.g. ['setosa', 'versicolor', 'virginica']

MODEL_VERSION = "iris-rf-v0.1"


# ----------------------------------------------------
# Endpoints
# ----------------------------------------------------
@app.get("/health")
def health():
    """Simple health check endpoint."""
    status = {"status": "ok", "model_loaded": MODEL_PATH.exists()}
    logger.info("health_check: %s", status)
    return status


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """
    Predict the iris species using the trained RandomForest model.
    Feature order must match training data:
    [sepal_length, sepal_width, petal_length, petal_width]
    """
    logger.info(
        "predict_request: sepal_length=%s sepal_width=%s petal_length=%s petal_width=%s",
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    )

    features = np.array(
        [[
            request.sepal_length,
            request.sepal_width,
            request.petal_length,
            request.petal_width,
        ]]
    )

    class_idx = int(model.predict(features)[0])
    probs = model.predict_proba(features)[0].tolist()
    label = str(target_names[class_idx])

    response = PredictionResponse(
        prediction=label,
        probabilities=probs,
        model_version=MODEL_VERSION,
    )

    logger.info(
        "predict_response: prediction=%s probabilities=%s model_version=%s",
        response.prediction,
        response.probabilities,
        response.model_version,
    )

    return response
