from pathlib import Path
import joblib

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

OUTPUT_PATH = Path("model.pkl")

def main():
    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names.tolist()

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )
    model.fit(X, y)

    artifact = {
        "model": model,
        "target_names": target_names,
    }

    joblib.dump(artifact, OUTPUT_PATH)
    print(f"✅ Saved model artifact to: {OUTPUT_PATH.resolve()}")
    print(f"Target names: {target_names}")

if __name__ == "__main__":
    main()
