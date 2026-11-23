import pandas as pd
from pathlib import Path

# Find the CSV file inside the dataset folder
files = list(Path("dataset").glob("*.csv"))

if len(files) == 0:
    print("Dataset file not found!")
else:
    # Load the dataset
    data = pd.read_csv(files[0])

    print("Dataset loaded successfully!")
    print("Number of rows and columns:", data.shape)

    print("\nColumn names:")
    print(data.columns.tolist())

    print("\nFirst five records:")
    print(data.head())