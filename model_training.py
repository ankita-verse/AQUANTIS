import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Load dataset
files = list(Path("dataset").glob("*.csv"))
data = pd.read_csv(files[0])

print("DATASET LOADED SUCCESSFULLY")
print("Dataset shape:", data.shape)

# Separate input features and target
X = data.drop("Potability", axis=1)
y = data["Potability"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Define three machine learning models
models = {

    "Logistic Regression": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000))
    ]),

    "KNN": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", KNeighborsClassifier(n_neighbors=5))
    ]),

    "Decision Tree": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", DecisionTreeClassifier(random_state=42))
    ]),

    "SVM": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", SVC(kernel="rbf", C=1.0, gamma="scale"))
    ])

}

# Train and evaluate each model
results = []

for name, model in models.items():

    print("\nTraining:", name)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    f1 = f1_score(y_test, predictions, zero_division=0)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    print("Accuracy:", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall:", round(recall, 4))
    print("F1 Score:", round(f1, 4))

    print("\nClassification Report:")
    print(classification_report(y_test, predictions, zero_division=0))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))

# Compare all models
results_df = pd.DataFrame(results)

print("\nFINAL MODEL COMPARISON")
print(results_df)

# Save comparison results
Path("results").mkdir(exist_ok=True)
results_df.to_csv("results/model_comparison.csv", index=False)

print("\nMODEL TRAINING COMPLETED SUCCESSFULLY!")
print("Comparison saved in results/model_comparison.csv")

joblib.dump(models["SVM"], "results/svm_model.pkl")
print("SVM model saved successfully!")