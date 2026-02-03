import json
import logging
from pathlib import Path

import joblib
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("iris-function")

MODEL_PATH = Path("model.pkl")

# Load model at cold start (recommended for performance)
logger.info("Loading model from %s", MODEL_PATH.resolve())
artifact = joblib.load(MODEL_PATH)
model = artifact["model"]
target_names = artifact["target_names"]

MODEL_VERSION = "iris-rf-v0.1"


def predict(request):
    """
    Google Cloud Function HTTP entry point.
    Expects JSON body:
    {
      "sepal_length": 5.1,
      "sepal_width": 3.5,
      "petal_length": 1.4,
      "petal_width": 0.2
    }
    """
    try:
        data = request.get_json(silent=True)
        if data is None:
            return (json.dumps({"error": "Request body must be JSON"}), 400, {"Content-Type": "application/json"})

        required = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        missing = [k for k in required if k not in data]
        if missing:
            return (json.dumps({"error": f"Missing fields: {missing}"}), 422, {"Content-Type": "application/json"})

        # Validate numeric
        try:
            sl = float(data["sepal_length"])
            sw = float(data["sepal_width"])
            pl = float(data["petal_length"])
            pw = float(data["petal_width"])
        except (TypeError, ValueError):
            return (json.dumps({"error": "All feature values must be valid numbers"}), 422, {"Content-Type": "application/json"})

        logger.info("predict_request: %s", {"sepal_length": sl, "sepal_width": sw, "petal_length": pl, "petal_width": pw})

        features = np.array([[sl, sw, pl, pw]])
        class_idx = int(model.predict(features)[0])
        probs = model.predict_proba(features)[0].tolist()
        label = str(target_names[class_idx])

        resp = {
            "prediction": label,
            "probabilities": probs,
            "model_version": MODEL_VERSION,
        }

        logger.info("predict_response: %s", resp)
        return (json.dumps(resp), 200, {"Content-Type": "application/json"})

    except Exception as e:
        logger.exception("Unexpected error")
        return (json.dumps({"error": str(e)}), 500, {"Content-Type": "application/json"})
