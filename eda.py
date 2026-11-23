import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create results folder if it does not exist
Path("results").mkdir(exist_ok=True)

# Load dataset
files = list(Path("dataset").glob("*.csv"))
data = pd.read_csv(files[0])

print("EDA STARTED")

# 1. Missing values
print("\nMISSING VALUES")
print(data.isnull().sum())

plt.figure(figsize=(10, 5))
sns.heatmap(data.isnull(), cbar=False, yticklabels=False)
plt.title("Missing Values in Water Quality Dataset")
plt.savefig("results/missing_values.png")
plt.close()

# 2. Potability distribution
print("\nPOTABILITY DISTRIBUTION")
print(data["Potability"].value_counts())

plt.figure(figsize=(6, 4))
sns.countplot(x="Potability", data=data)
plt.title("Water Potability Distribution")
plt.savefig("results/potability_distribution.png")
plt.close()

# 3. Feature distribution graphs
features = data.drop(columns=["Potability"])

features.hist(figsize=(14, 10), bins=30)
plt.suptitle("Distribution of Water Quality Parameters")
plt.tight_layout()
plt.savefig("results/feature_distributions.png")
plt.close()

# 4. Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("results/correlation_heatmap.png")
plt.close()

# 5. Statistical summary
summary = data.describe()
summary.to_csv("results/statistical_summary.csv")

print("\nSTATISTICAL SUMMARY")
print(summary)

print("\nEDA COMPLETED SUCCESSFULLY!")
print("All graphs and summary saved in results folder.")