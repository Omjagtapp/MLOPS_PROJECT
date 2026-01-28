from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


def main():
    # Load iris dataset (built-in, no file needed)
    iris = load_iris()
    X = iris.data  # 4 features: sepal_length, sepal_width, petal_length, petal_width
    y = iris.target  # 0, 1, 2 (setosa, versicolor, virginica)

    # Simple train/test split for sanity check
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train a small random forest classifier
    clf = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )
    clf.fit(X_train, y_train)

    # Quick evaluation
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test accuracy: {acc:.3f}")

    # Save model to disk as model.pkl
    model_path = Path("model.pkl")
    joblib.dump(
        {
            "model": clf,
            "target_names": iris.target_names,
        },
        model_path,
    )
    print(f"Saved model to {model_path.resolve()}")


if __name__ == "__main__":
    main()